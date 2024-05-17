
# Documentación del Proyecto

---

## Introducción
- **Descripción del Proyecto:** Breve descripción del proyecto y su propósito.
- **Contexto:** Antecedentes y contexto en los que se desarrolla el proyecto.
- **Alcance:** Alcance del proyecto y lo que se espera lograr.

## Objetivos
- **Objetivos Generales:** Metas amplias que el proyecto pretende alcanzar.
- **Objetivos Específicos:** Metas más detalladas y específicas que se deben cumplir para alcanzar los objetivos generales.

## Atributos de Calidad
- **Escalabilidad:** Cómo la arquitectura puede manejar un aumento en la carga de trabajo.
- **Rendimiento:** Expectativas de rendimiento y cómo se medirá.
- **Disponibilidad:** Nivel de disponibilidad requerido y cómo se logrará.
- **Seguridad:** Medidas de seguridad implementadas para proteger los datos.
- **Mantenibilidad:** Cómo se asegurará que la arquitectura sea fácil de mantener y actualizar.
- **Confiabilidad:** Nivel de confiabilidad y cómo se garantizará.

## Descripción de la Arquitectura
- **Diagramas de Arquitectura:** Diagramas que ilustren la arquitectura del sistema.
- **Componentes:** Descripción de los principales componentes del sistema y sus responsabilidades.
- **Flujo de Datos:** Cómo se mueven los datos a través del sistema.
### Arquitectura
- Componentes
![architecture.png](doc/img/architecture.png)
## Tecnologías Utilizadas
- **Lenguajes de Programación:** Lenguajes utilizados en el proyecto.
- **Frameworks y Librerías:** Herramientas y librerías clave utilizadas.
- **Plataformas y Servicios:** Plataformas (como bases de datos, servicios en la nube, etc.) que se están utilizando.

## Configuración e Instalación
- **Requisitos Previos:** Herramientas y software necesarios antes de la instalación.
- **Instrucciones de Instalación:** Pasos detallados para instalar y configurar el proyecto.
- **Configuración Inicial:** Configuraciones iniciales que deben ser realizadas antes de ejecutar el proyecto.

## Uso del Proyecto
- **Guía de Usuario:** Instrucciones sobre cómo usar el proyecto.
- **Ejemplos de Uso:** Ejemplos prácticos de cómo interactuar con el sistema.

## Pruebas y Validación
- **Estrategia de Pruebas:** Cómo se realizarán las pruebas para asegurar la calidad.
- **Casos de Prueba:** Ejemplos de casos de prueba que se utilizarán.
- **Resultados Esperados:** Resultados esperados de las pruebas.

## Mantenimiento y Soporte
- **Guía de Mantenimiento:** Procedimientos y mejores prácticas para mantener el sistema.
- **Soporte:** Cómo obtener ayuda y soporte para el proyecto.

## Contribuciones
- **Guía de Contribución:** Cómo otros pueden contribuir al proyecto.
- **Políticas de Código:** Normas y políticas para contribuir con código al proyecto.

## Licencia
- **Licencia del Proyecto:** Detalles sobre la licencia bajo la cual se distribuye el proyecto.

## Agradecimientos
- **Reconocimientos:** Agradecimientos a quienes han contribuido al proyecto.

---

# Estructura del repositorio:
``` 
boilerplate-database/
├── README.md
├── docker-compose.yml
├── db/
│   ├── postgres/
│   │   ├── Dockerfile
│   │   ├── init.sql
│   │   └── config/
│   │       └── postgres.conf
│   ├── mongo/
│   │   ├── Dockerfile
│   │   └── init.js
├── data/
│   ├── input/
│   │   └── sample.csv
│   └── output/
│       └── transformed.parquet
├── src/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── pipeline.py
│   │   └── transform.py
│   ├── main.py
│   └── requirements.txt
├── tests/
│   ├── test_database.py
│   ├── test_models.py
│   └── test_pipeline.py
└── .env

```

## Descripción de cada archivo y directorio

- **README.md**: Archivo de documentación que describe el propósito del proyecto, cómo configurarlo y cómo usarlo.

- **docker-compose.yml**: Archivo de configuración para Docker Compose, que define los servicios, redes y volúmenes necesarios para levantar el entorno de desarrollo.

- **db/**: Directorio que contiene las configuraciones y scripts de inicialización para las bases de datos.

  - **postgres/**: Contiene los archivos relacionados con la base de datos PostgreSQL.
    - **Dockerfile**: Archivo de definición de la imagen Docker para PostgreSQL.
    - **init.sql**: Script SQL para inicializar la base de datos PostgreSQL.
    - **config/**: Directorio que contiene archivos de configuración para PostgreSQL.
      - **postgres.conf**: Archivo de configuración de PostgreSQL.

  - **mongo/**: Contiene los archivos relacionados con la base de datos MongoDB.
    - **Dockerfile**: Archivo de definición de la imagen Docker para MongoDB.
    - **init.js**: Script JavaScript para inicializar la base de datos MongoDB.

- **data/**: Directorio que contiene datos de entrada y salida.

  - **input/**: Directorio para los archivos de datos de entrada.
    - **sample.csv**: Archivo CSV de muestra para los datos de entrada.

  - **output/**: Directorio para los archivos de datos transformados.
    - **transformed.parquet**: Archivo Parquet que contiene los datos transformados.

- **src/**: Directorio que contiene el código fuente del proyecto.

  - **app/**: Directorio que contiene los módulos de la aplicación.
    - **`__init__.py`**: Archivo de inicialización para el paquete `app`.
    - **database.py**: Archivo que maneja las conexiones a las bases de datos.
    - **models.py**: Archivo que define los modelos de datos.
    - **pipeline.py**: Archivo que contiene la lógica del pipeline de datos.
    - **transform.py**: Archivo que contiene funciones para transformar los datos.

  - **main.py**: Archivo principal para ejecutar la aplicación.
  - **requirements.txt**: Archivo que lista las dependencias de Python necesarias para el proyecto.

- **tests/**: Directorio que contiene los archivos de pruebas unitarias.

  - **test_database.py**: Archivo de pruebas unitarias para `database.py`.
  - **test_models.py**: Archivo de pruebas unitarias para `models.py`.
  - **test_pipeline.py**: Archivo de pruebas unitarias para `pipeline.py`.

- **.env**: Archivo que contiene variables de entorno necesarias para la configuración del proyecto.

***

## Instrucciones básicas
Clona el repositorio.
Crea el archivo .env con las variables de entorno necesarias.
Construye y levanta los servicios con Docker Compose:

```sh
docker-compose up --build
```