# Sistema de Gestión de Torneo de Fútbol

## Información del Proyecto

**Autor:** Codrin Girdea  
**Versión:** 3.0  
**Fecha:** Enero 2026  
**Instituto:** IES Brianda de Mendoza  
**Asignatura:** Diseño de Interfaces - 2º DAM

## Descripción

Aplicación de escritorio para la gestión integral de un torneo de fútbol de eliminatorias en el instituto. Permite gestionar equipos, participantes (jugadores y árbitros), programar partidos, actualizar resultados y visualizar el bracket de eliminatorias.

## Características Principales

- Gestión completa de equipos (crear, editar, eliminar, asignar escudos)
- Gestión de participantes (jugadores y árbitros)
- Programación de partidos por eliminatorias
- Actualización de resultados en tiempo real
- Visualización gráfica del bracket de eliminatorias
- Sistema de tarjetas y goles
- Base de datos SQLite integrada
- Interfaz gráfica moderna con PySide6
- Integración de componente de reloj y cronómetro

## Estructura del Proyecto

```
TorneoFutbol/
│
├── main.py                      # Archivo principal de ejecución
├── requirements.txt             # Dependencias del proyecto
├── TorneoFutbol.spec           # Configuración de PyInstaller
│
├── views/                       # Interfaces gráficas
│   ├── __init__.py
│   ├── main_window.py          # Ventana principal
│   ├── equipos_window.py       # Gestión de equipos
│   ├── participantes_window.py # Gestión de participantes
│   ├── partidos_window.py      # Gestión de partidos
|   ├── clock_window.py         # Vista del reloj 
|   ├── clock_main_window.py    # Vista del componente general (aunque se llame main window es un QWidget)
│   ├── resultados_window.py    # Actualización de resultados
│   ├── clasificacion_window.py # Bracket de eliminatorias
|   ├── exportar_window.py      # Ventana para exportar datos en csv
│   ├── creditos_window.py      # Créditos
│   ├── ayuda_window.py         # Ayuda
│   └── ui_*.py                 # Archivos generados por Qt Designer
│
├── controllers/                 # Lógica de control
│   ├── __init__.py
│   ├── equipo_controller.py
│   ├── participante_controller.py
│   ├── partido_controller.py
|   ├── clock_controller.py
|   ├── exportar_controller.py
│   └── resultado_controller.py
│
├── models/                      # Modelos y base de datos
│   ├── __init__.py
│   ├── database.py             # Conexión y configuración de BD
│   ├── equipo.py               # Modelo de Equipo
│   ├── participante.py         # Modelo de Participante
│   ├── partido.py              # Modelo de Partido
│   ├── gol_partido.py          # Modelo de Gol
│   ├── tarjeta_partido.py      # Modelo de Tarjeta
|   ├── clock_model.py          # Modelo del componente
│   └── torneoFutbol_sqlite.db  # Base de datos SQLite
│
├── utils/                       # Utilidades
│   ├── __init__.py
│   └── icon_helper.py          # Gestión de iconos
│
└── resources/                   # Recursos
    ├── icons/                  # Iconos de la aplicación
    ├── images/                 # Imágenes
    └── qss/                    # Hojas de estilo Qt
```

## Base de Datos

### Estructura de Tablas

#### Tabla: `equipos`
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INTEGER PRIMARY KEY | Identificador único |
| nombre | TEXT NOT NULL UNIQUE | Nombre del equipo |
| curso | TEXT NOT NULL | Curso del equipo |
| color_camiseta | TEXT | Color de la camiseta |
| escudo | BLOB | Imagen del escudo |

#### Tabla: `participantes`
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INTEGER PRIMARY KEY | Identificador único |
| nombre | TEXT NOT NULL | Nombre del participante |
| fecha_nacimiento | TEXT NOT NULL | Fecha de nacimiento |
| curso | TEXT NOT NULL | Curso |
| es_jugador | INTEGER DEFAULT 0 | 1 si es jugador |
| es_arbitro | INTEGER DEFAULT 0 | 1 si es árbitro |
| posicion | TEXT | Posición (si es jugador) |
| equipo_id | INTEGER | FK a equipos |
| t_amarillas | INTEGER DEFAULT 0 | Tarjetas amarillas |
| t_rojas | INTEGER DEFAULT 0 | Tarjetas rojas |
| goles | INTEGER DEFAULT 0 | Goles marcados |

#### Tabla: `partidos`
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INTEGER PRIMARY KEY | Identificador único |
| equipo_local_id | INTEGER NOT NULL | FK a equipos |
| equipo_visitante_id | INTEGER NOT NULL | FK a equipos |
| arbitro_id | INTEGER NOT NULL | FK a participantes |
| fecha | TEXT NOT NULL | Fecha del partido |
| hora | TEXT NOT NULL | Hora del partido |
| eliminatoria | TEXT NOT NULL | Octavos/Cuartos/Semifinal/Final |
| goles_local | INTEGER DEFAULT 0 | Goles equipo local |
| goles_visitante | INTEGER DEFAULT 0 | Goles equipo visitante |
| jugado | INTEGER DEFAULT 0 | 1 si ya se jugó |

#### Tabla: `goles_partido`
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INTEGER PRIMARY KEY | Identificador único |
| partido_id | INTEGER NOT NULL | FK a partidos |
| jugador_id | INTEGER NOT NULL | FK a participantes |
| minuto | INTEGER NOT NULL | Minuto del gol |

#### Tabla: `tarjetas_partido`
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INTEGER PRIMARY KEY | Identificador único |
| partido_id | INTEGER NOT NULL | FK a partidos |
| jugador_id | INTEGER NOT NULL | FK a participantes |
| tipo | TEXT NOT NULL | amarilla/roja |
| minuto | INTEGER NOT NULL | Minuto de la tarjeta |

### Relaciones
- `participantes.equipo_id` → `equipos.id` (ON DELETE CASCADE)
- `partidos.equipo_local_id` → `equipos.id` (ON DELETE RESTRICT)
- `partidos.equipo_visitante_id` → `equipos.id` (ON DELETE RESTRICT)
- `partidos.arbitro_id` → `participantes.id` (ON DELETE RESTRICT)
- `goles_partido.partido_id` → `partidos.id` (ON DELETE CASCADE)
- `goles_partido.jugador_id` → `participantes.id` (ON DELETE CASCADE)
- `tarjetas_partido.partido_id` → `partidos.id` (ON DELETE CASCADE)
- `tarjetas_partido.jugador_id` → `participantes.id` (ON DELETE CASCADE)

## Instalación y Ejecución

### Para Desarrollo

1. **Clonar o descargar el proyecto**

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Ejecutar la aplicación:**
```bash
python main.py
```

### Ejecutable Distribuible (Windows)

#### Requisitos previos:
- Python 3.8 o superior
- pip

#### Generar el ejecutable:

1. **Instalar PyInstaller:**
```bash
pip install pyinstaller
```

2. **Generar el ejecutable:**
```bash
pyinstaller TorneoFutbol.spec
```

3. **Ubicación del ejecutable:**
```
dist/TorneoFutbol.exe (se encuentra subido también en el aula virtual)
```

#### Ejecutar el programa:
- Hacer doble clic en `TorneoFutbol.exe`
- No se requiere instalación de Python ni dependencias
- La base de datos se crea automáticamente en la primera ejecución

## Uso de la Aplicación

### 1. Gestión de Equipos
- Crear equipos con nombre, curso y color de camiseta
- Opcionalmente asignar un escudo (imagen)
- Editar o eliminar equipos existentes
- Ver listado completo de equipos

### 2. Gestión de Participantes
- Registrar jugadores y/o árbitros
- Asignar jugadores a equipos
- Especificar posición de juego
- Visualizar estadísticas (goles, tarjetas)

### 3. Gestión de Partidos
- Programar partidos seleccionando:
  - Equipo local y visitante
  - Árbitro asignado
  - Fecha y hora
  - Eliminatoria (Octavos, Cuartos, Semifinal, Final)
- Editar o eliminar partidos pendientes
- Ver calendario completo

### 4. Actualización de Resultados
- Seleccionar partido pendiente
- Registrar goles indicando:
  - Jugador que marca
  - Minuto del gol
- Registrar tarjetas indicando:
  - Jugador sancionado
  - Tipo (amarilla/roja)
  - Minuto (recogido del cronometro sumando 1 minuto si ha pasado un segundo ej: minuto 1:01 -> minuto 2 en la tabla)
- Finalizar partido (marca como jugado)
- Las estadísticas se actualizan automáticamente

### 5. Visualización de Eliminatorias
- Ver bracket completo del torneo
- Visualización gráfica de todas las rondas
- Identificación del campeón con escudo
- Actualización automática al finalizar partidos

### 6. Exportar datos en csv
- Exportar clasificación general
- Exportar goleadores
- Exportar jugadores con tarjetas
- Exportar partidos jugados
- Exportar calendario completo
- Exportar todos los jugadores
  
## Datos de Ejemplo

La aplicación incluye datos de ejemplo que se cargan automáticamente en la primera ejecución:
- 16 equipos (para Octavos de Final)
- 64 jugadores (4 por equipo)
- 8 árbitros
- 8 partidos de Octavos programados

## Notas Técnicas

### Arquitectura
- **Patrón MVC:** Separación clara entre Modelo, Vista y Controlador
- **Base de datos:** SQLite con integridad referencial
- **GUI:** PySide6 (Qt for Python)
- **Empaquetado:** PyInstaller

### Consideraciones
- La base de datos se crea automáticamente si no existe
- Los escudos se almacenan como BLOB en la base de datos, aunque los equipos no tienen asignados escudos originalmente
- No se permiten empates en eliminatorias
- Las claves foráneas están activas (PRAGMA foreign_keys = ON)

## Solución de Problemas

### La aplicación no inicia
- Verificar que todos los archivos estén en las carpetas correctas
- Si es el .exe, verificar que la carpeta `resources` esté junto al ejecutable

### Error al cargar iconos
- Los iconos deben estar en `resources/icons/`
- La aplicación funcionará sin iconos, solo mostrará advertencias en consola

### Error de base de datos
- Eliminar el archivo `torneoFutbol_sqlite.db` para recrear la base de datos
- Verificar permisos de escritura en la carpeta

## Créditos

**Desarrollado por:** Codrin Girdea  
**Proyecto:** Diseño de Interfaces - 2º DAM  
**Instituto:** IES Brianda de Mendoza  
**Fecha:** Enero 2026  
**Versión:** 3.0
