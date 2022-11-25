![Logo ITESO](./Data/Imagenes/logo.png)


# Examen Final
### Materia: Proyecto de Ciencia de Datos
#### José Manuel Haces López - 734759 - Ing. Y Ciencia de Datos - ITESO
_________________
Este repositorio contiene el examen final para la materia de 'Proyecto de Ciencia de Datos' en otoño 2022 por ITESO.
_________________
#### Instrucciones:
Lea cuidadosamente las siguientes **indicaciones** antes de comenzar el examen:
- El objetivo de este examen es poder evaluar sus conocimientos como **Científico de Datos** a la hora de desarrollar un proyecto de inicio a fin.
- Usted, como líder de este proyecto, tendrá toda la autoridad y potestad de tomar cualquier decisión y asumir lo que considere necesario, siempre y cuando tenga razones concretas para justificar dichas decisiones.
- Se le planteará un escenario de la vida real y se le compartirá el conjunto de datos respectivos para atacar el problema.
- Antes de iniciar a resolver el examen, deberá crear un repositorio en su cuenta de `GitHub` y nombrarlo de la siguiente manera: `examen-final-pdcd`.
- Dicho repositorio deberá contener un archivo `README.md` y un archivo `.gitignore`.
- La solución del problema deberá contener, **como mínimo** los aspectos básicos de un proyecto de ciencia de datos:
    - Análisis Exploratorio de Datos.
    - Ingeniería de Características - Data Wrangling
    - Entrenamiento, validación, evaluación y selección del modelo
    - Microservicio (API) para servir el modelo
    - Creación de imagen para dicha API. Explicar el procedimiento utilizado para crear la imagen y correr el contenedor. (Adjunte imagenes como prueba del funcionamiento del contenedor de la API)
- Deberá estructurar el proyecto de una manera asertiva. Hará parte de la evaluación la selección de la estructura del proyecto.
- Recuerde la importancia de los archivos `requirements.txt` y `Dockerfile` para el desarrollo del proyecto. Ubiquelos en la carpeta correcta.
- Este archivo `ExamenFinal.ipynb` póngalo en la carpeta raíz del repositorio.

_________________
#### Descripción de la Base de Datos
<p>En escuelas de E.U.A los maestros desarrollan proyectos para mejorar las condiciones de los estudiantes, resolver problemáticas como el bullying, mejorar el prendizaje, etc. El dataset <b>Projects_cleansed.zip</b> esta formado por las siguientes columnas:<br>
</p>

<b>Project Title</b> - Nombre del Proyecto<br>
<b>Project Short Description </b> - Descripción corta (198 palabras aprox.) y el final de la descripción esta indicada por "..."<br>
<b>Project Subject Category Tree</b> - es una taxonomía que indica el área al que pertenece el proyecto<br>
    <b>Project Cost</b> - es un campo numérico que indica la cantidad que se busca fondear<br>
    <b>Project Current Status</b> - Si el proyecto fué fondedado o no<br>

El `dataset` se encuentra en la carpeta Data de este repo. Para descargar el archivo zp da click [AQUÍ](https://drive.google.com/file/d/1sQ7Fw0tO9GV-qnErJTQEbnqAACcPc18Q/view).

#### Especificaciones de Input y Output
<h5>Input</h5>
<p>El modelo recibirá como entrada:
    <ul>
        <li><b>descripción</b>: Es una descripción textual sobre la que haremos la predicción</li>
    </ul>
<h5>Output</h5>
<p>El output del modelo debe de ser una clasificación <b>1</b>:funded y <b>0</b>: not funded </p><br>

_________________
## Resultados
- Api -> Directorio con todo lo necesario para la APP.
- Data -> Directorio con todos los datos necesarios.
- Modelos -> Directorio con todos los modelos generados.
- ExamenFinal.ipynb -> Notebook con el EDA, Ingeniería de características, Modelado y Evaluación del modelo.
- Reporte_Contenedor -> Notebook con la evidencia de generación y uso de la imagen y contenedor de docker.
- requirements.txt -> Requerimientos para el notebook.

