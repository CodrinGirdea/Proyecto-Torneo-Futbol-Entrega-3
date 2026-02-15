"""
Controlador de informes Jasper para Torneo de Fútbol
Genera informes PDF desde plantillas JRXML
"""
import subprocess
import sys
import os
from pathlib import Path


def get_db_path():
    """
    Obtiene la ruta de la base de datos del torneo
    Usa la misma lógica que models/database.py
    """
    # Si estamos en un ejecutable (PyInstaller)
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        # Si estamos en desarrollo
        base_path = Path(__file__).parent.parent
    
    db_path = os.path.join(base_path, "torneoFutbol.db")
    
    print(f"✓ Ruta de BD: {db_path}")
    
    if not Path(db_path).exists():
        # Intentar ruta alternativa en models/
        alt_path = Path(__file__).parent.parent / "models" / "torneoFutbol.db"
        if alt_path.exists():
            db_path = str(alt_path)
            print(f"✓ Usando ruta alternativa: {db_path}")
    
    return str(db_path)


def generate_pdf_from_jrxml(jrxml_file, output_pdf, parameters=None):
    """
    Genera un PDF directamente desde un archivo JRXML
    
    Args:
        jrxml_file: Ruta al archivo .jrxml
        output_pdf: Ruta donde guardar el PDF
        parameters: Diccionario con parámetros del informe (opcional)
        
    Returns:
        Path: Ruta al PDF generado
        
    Raises:
        FileNotFoundError: Si no existe el JRXML o la BD
        RuntimeError: Si falla la generación del PDF
    """
    jrxml_path = Path(jrxml_file)
    output_path = Path(output_pdf)
    
    # Validar que existe el JRXML
    if not jrxml_path.exists():
        raise FileNotFoundError(f"No existe el archivo JRXML: {jrxml_path}")
    
    # Crear directorio de salida si no existe
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Obtener ruta de la base de datos
    db_path = get_db_path()
    
    if not Path(db_path).exists():
        raise FileNotFoundError(
            f"No se encuentra la base de datos en: {db_path}\n"
            "Ejecuta la aplicación principal primero para crear la BD."
        )
    
    print(f"✓ Base de datos encontrada: {db_path}")
    
    # Directorio de librerías JAR
    base_dir = Path(__file__).parent.parent
    lib_dir = base_dir / "reports" / "lib"
    
    # Verificar que existan los JARs
    jars = list(lib_dir.glob("*.jar"))
    if not jars:
        raise FileNotFoundError(
            f"No se encontraron JARs en {lib_dir}\n"
            "Copia los archivos JAR necesarios en la carpeta reports/lib/"
        )
    
    print(f"✓ Encontrados {len(jars)} archivos JAR")
    
    # Construir classpath (separador ; en Windows, : en Linux)
    separator = ";" if sys.platform == "win32" else ":"
    classpath = separator.join(str(jar) for jar in jars)
    
    # Nombre de clase Java válido
    class_name = "JasperReportGenerator"
    
    # Crear script Java temporal
    java_code = _create_java_direct_generator(
        jrxml_path, output_path, db_path, parameters or {}, class_name
    )
    
    # Guardar código Java temporal
    java_file = output_path.parent / f"{class_name}.java"
    
    try:
        # Escribir el archivo Java
        java_file.write_text(java_code, encoding='utf-8')
        print(f"✓ Script Java creado: {java_file.name}")
        
        # Compilar el código Java
        compile_cmd = [
            "javac",
            "-encoding", "UTF-8",
            "-cp", classpath,
            str(java_file)
        ]
        
        print(f"Compilando script Java...")
        result = subprocess.run(
            compile_cmd, 
            check=True, 
            capture_output=True, 
            text=True
        )
        print(f"✓ Script Java compilado")
        
        # Ejecutar el código Java
        run_cmd = [
            "java",
            "-Dfile.encoding=UTF-8",
            "-cp", f"{classpath}{separator}{java_file.parent}",
            class_name
        ]
        
        print(f"Ejecutando generador de informes...")
        print(f"(Esto puede tardar unos segundos...)")
        result = subprocess.run(
            run_cmd,
            check=True,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        # Mostrar salida de Java
        if result.stdout:
            print("\n--- Salida de Java ---")
            print(result.stdout)
            print("--- Fin de salida ---\n")
        
        if output_path.exists():
            print(f"✓✓✓ PDF generado exitosamente: {output_path.name}")
            return output_path
        else:
            raise RuntimeError("El PDF no se generó correctamente")
            
    except subprocess.CalledProcessError as e:
        error_msg = f"Error al generar PDF:\n"
        if e.stdout:
            error_msg += f"STDOUT:\n{e.stdout}\n"
        if e.stderr:
            error_msg += f"STDERR:\n{e.stderr}\n"
        raise RuntimeError(error_msg)
    
    except subprocess.TimeoutExpired:
        raise RuntimeError(
            "La generación del PDF excedió el tiempo límite (60 segundos).\n"
            "Verifica que la consulta SQL en el JRXML sea correcta."
        )
    
    finally:
        # Limpiar archivos temporales
        try:
            if java_file.exists():
                java_file.unlink()
            class_file = java_file.with_suffix('.class')
            if class_file.exists():
                class_file.unlink()
        except Exception as e:
            print(f"⚠ No se pudieron limpiar archivos temporales: {e}")


def _create_java_direct_generator(jrxml_path, output_pdf, db_path, parameters, class_name):
    """
    Crea el código Java que compila JRXML y genera PDF
    """
    
    params_code = ""
    for key, value in parameters.items():
        # Escapar comillas en el valor
        value_escaped = str(value).replace('"', '\\"')
        params_code += f'            parameters.put("{key}", "{value_escaped}");\n'
    
    # Convertir rutas de Windows a formato Java (escapar backslashes)
    jrxml_path_java = str(jrxml_path.absolute()).replace('\\', '\\\\')
    output_pdf_java = str(output_pdf.absolute()).replace('\\', '\\\\')
    db_path_java = str(db_path).replace('\\', '\\\\')
    
    return f'''import net.sf.jasperreports.engine.*;
import java.sql.*;
import java.util.HashMap;
import java.util.Map;
import java.io.File;

public class {class_name} {{
    public static void main(String[] args) {{
        Connection conn = null;
        try {{
            System.out.println("========================================");
            System.out.println("  GENERADOR DE INFORMES - TORNEO FÚTBOL  ");
            System.out.println("========================================");
            System.out.println();
            
            // 1. Cargar driver JDBC de SQLite
            System.out.println("[1/5] Cargando driver SQLite...");
            Class.forName("org.sqlite.JDBC");
            System.out.println("      ✓ Driver cargado");
            System.out.println();
            
            // 2. Conectar a la base de datos
            System.out.println("[2/5] Conectando a base de datos...");
            String dbUrl = "jdbc:sqlite:{db_path_java}";
            System.out.println("      URL: " + dbUrl);
            conn = DriverManager.getConnection(dbUrl);
            System.out.println("      ✓ Conexión establecida");
            System.out.println();
            
            // 3. Compilar JRXML a JASPER
            System.out.println("[3/5] Compilando informe JRXML...");
            String jrxmlFile = "{jrxml_path_java}";
            System.out.println("      Archivo: " + jrxmlFile);
            
            JasperReport jasperReport = JasperCompileManager.compileReport(jrxmlFile);
            System.out.println("      ✓ Informe compilado exitosamente");
            System.out.println();
            
            // 4. Configurar parámetros
            System.out.println("[4/5] Configurando parámetros...");
            Map<String, Object> parameters = new HashMap<>();
{params_code}
            System.out.println("      ✓ Parámetros configurados");
            System.out.println();
            
            // 5. Llenar informe con datos y exportar a PDF
            System.out.println("[5/5] Generando PDF...");
            JasperPrint jasperPrint = JasperFillManager.fillReport(
                jasperReport,
                parameters,
                conn
            );
            System.out.println("      ✓ Datos cargados");
            
            String pdfFile = "{output_pdf_java}";
            JasperExportManager.exportReportToPdfFile(jasperPrint, pdfFile);
            System.out.println("      ✓ PDF exportado");
            System.out.println();
            
            // Verificar que el PDF se creó
            File pdf = new File(pdfFile);
            if (pdf.exists()) {{
                System.out.println("========================================");
                System.out.println("  ✓✓✓ PDF GENERADO EXITOSAMENTE ✓✓✓  ");
                System.out.println("========================================");
                System.out.println("Archivo: " + pdfFile);
                System.out.println("Tamaño: " + pdf.length() + " bytes");
            }} else {{
                System.err.println("ERROR: El archivo PDF no se creó");
                System.exit(1);
            }}
            
        }} catch (Exception e) {{
            System.err.println();
            System.err.println("========================================");
            System.err.println("  ERROR AL GENERAR INFORME");
            System.err.println("========================================");
            System.err.println("Mensaje: " + e.getMessage());
            System.err.println();
            System.err.println("Stack trace:");
            e.printStackTrace();
            System.exit(1);
        }} finally {{
            // Cerrar conexión
            try {{
                if (conn != null && !conn.isClosed()) {{
                    conn.close();
                    System.out.println("✓ Conexión cerrada");
                }}
            }} catch (SQLException e) {{
                e.printStackTrace();
            }}
        }}
    }}
}}
'''


# ============================================================================
# FUNCIONES DE CONVENIENCIA PARA LOS INFORMES ESPECÍFICOS
# ============================================================================

def generar_informe_equipos(equipo_id=None, output_dir="informes"):
    """
    Genera el informe de Equipos y Jugadores
    
    Args:
        equipo_id: ID del equipo específico (None = todos los equipos)
        output_dir: Directorio donde guardar el PDF
    
    Returns:
        Path: Ruta al PDF generado
    """
    base_dir = Path(__file__).parent.parent
    reports_dir = base_dir / "reports"
    output_path = base_dir / output_dir
    
    jrxml_file = reports_dir / "informe_equipos.jrxml"
    
    if equipo_id:
        pdf_file = output_path / f"informe_equipos_{equipo_id}.pdf"
    else:
        pdf_file = output_path / "informe_equipos.pdf"
    
    if not jrxml_file.exists():
        raise FileNotFoundError(
            f"No se encuentra el archivo: {jrxml_file}\n"
            "Asegúrate de tener informe_equipos.jrxml en la carpeta reports/"
        )
    
    print("=" * 60)
    print("GENERANDO INFORME DE EQUIPOS Y JUGADORES")
    print("=" * 60)
    
    parameters = {
        "TITULO": "Informe de Equipos y Jugadores - Torneo de Fútbol"
    }
    
    if equipo_id:
        parameters["EQUIPO_ID"] = str(equipo_id)
    
    return generate_pdf_from_jrxml(jrxml_file, pdf_file, parameters)


def generar_informe_partidos(eliminatoria=None, output_dir="informes"):
    """
    Genera el informe de Partidos y Resultados
    
    Args:
        eliminatoria: Filtrar por eliminatoria específica (Octavos, Cuartos, Semifinal, Final)
        output_dir: Directorio donde guardar el PDF
    
    Returns:
        Path: Ruta al PDF generado
    """
    base_dir = Path(__file__).parent.parent
    reports_dir = base_dir / "reports"
    output_path = base_dir / output_dir
    
    jrxml_file = reports_dir / "informe_partidos.jrxml"
    
    if eliminatoria:
        pdf_file = output_path / f"informe_partidos_{eliminatoria.lower()}.pdf"
    else:
        pdf_file = output_path / "informe_partidos.pdf"
    
    if not jrxml_file.exists():
        raise FileNotFoundError(
            f"No se encuentra el archivo: {jrxml_file}\n"
            "Asegúrate de tener informe_partidos.jrxml en la carpeta reports/"
        )
    
    print("=" * 60)
    print("GENERANDO INFORME DE PARTIDOS Y RESULTADOS")
    print("=" * 60)
    
    parameters = {
        "TITULO": "Informe de Partidos y Resultados"
    }
    
    if eliminatoria:
        parameters["ELIMINATORIA"] = eliminatoria
    
    return generate_pdf_from_jrxml(jrxml_file, pdf_file, parameters)


def generar_informe_clasificacion(eliminatoria=None, output_dir="informes"):
    """
    Genera el informe de Clasificación y Eliminatorias
    
    Args:
        eliminatoria: Filtrar por eliminatoria específica
        output_dir: Directorio donde guardar el PDF
    
    Returns:
        Path: Ruta al PDF generado
    """
    base_dir = Path(__file__).parent.parent
    reports_dir = base_dir / "reports"
    output_path = base_dir / output_dir
    
    jrxml_file = reports_dir / "informe_clasificacion.jrxml"
    
    if eliminatoria:
        pdf_file = output_path / f"informe_clasificacion_{eliminatoria.lower()}.pdf"
    else:
        pdf_file = output_path / "informe_clasificacion.pdf"
    
    if not jrxml_file.exists():
        raise FileNotFoundError(
            f"No se encuentra el archivo: {jrxml_file}\n"
            "Asegúrate de tener informe_clasificacion.jrxml en la carpeta reports/"
        )
    
    print("=" * 60)
    print("GENERANDO INFORME DE CLASIFICACIÓN Y ELIMINATORIAS")
    print("=" * 60)
    
    parameters = {
        "TITULO": "Tabla de Clasificación y Eliminatorias"
    }
    
    if eliminatoria:
        parameters["ELIMINATORIA"] = eliminatoria
    
    return generate_pdf_from_jrxml(jrxml_file, pdf_file, parameters)


# ============================================================================
# FUNCIÓN DE PRUEBA
# ============================================================================

def test_generacion_informes():
    """
    Función de prueba para verificar que funciona la generación de informes
    """
    try:
        print("\n" + "=" * 70)
        print("PRUEBA DE GENERACIÓN DE INFORMES")
        print("=" * 70 + "\n")
        
        # Verificar que existe la base de datos
        db_path = get_db_path()
        if not Path(db_path).exists():
            print("❌ No se encuentra la base de datos")
            print(f"   Buscada en: {db_path}")
            return False
        
        print("✓ Base de datos encontrada\n")
        
        # Verificar JARs
        base_dir = Path(__file__).parent.parent
        lib_dir = base_dir / "reports" / "lib"
        jars = list(lib_dir.glob("*.jar"))
        
        if not jars:
            print("❌ No se encontraron archivos JAR")
            print(f"   Buscados en: {lib_dir}")
            return False
        
        print(f"✓ Encontrados {len(jars)} archivos JAR\n")
        
        # Verificar JRXML
        reports_dir = base_dir / "reports"
        jrxml_files = list(reports_dir.glob("*.jrxml"))
        
        if not jrxml_files:
            print("⚠ No se encontraron archivos JRXML")
            print(f"   Buscados en: {reports_dir}")
            print("   (Esto es normal si aún no has creado las plantillas)\n")
        else:
            print(f"✓ Encontrados {len(jrxml_files)} archivos JRXML:")
            for jrxml in jrxml_files:
                print(f"   - {jrxml.name}")
            print()
        
        print("✓ Todo listo para generar informes")
        return True
        
    except Exception as e:
        print(f"❌ Error en la prueba: {e}")
        return False


if __name__ == "__main__":
    # Ejecutar prueba
    test_generacion_informes()
