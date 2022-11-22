![Logo ITESO](./Data/Imagenes/logo.png)


# Examen Final
### Materia: Proyecto de Ciencia de Datos
#### José Manuel Haces López - 734759 - Ing. Y Ciencia de Datos - ITESO
_________________
#### Instrucciones:
Lea cuidadosamente las siguientes **indicaciones** antes de comenzar el examen:
- El objetivo de este examen es poder evaluar sus conocimientos como **Científico de Datos** a la hora de desarrollar un proyecto de inicio a fin.
- Usted, como líder de este proyecto, tendrá toda la autoridad y potestad de tomar cualquier decisión y asumir lo que considere necesario, siempre y cuando tenga razones concretas para justificar dichas decisiones.
- Se le planteará un escenario de la vida real y se le compartirá el conjunto de datos respectivos para atacar el problema.
- Antes de iniciar a resolver el examen, deberá crear un repositorio en su cuenta de `GitHub` y nombrarlo de la siguiente manera: `examen-final-pdcd`.
- Dicho repositorio deberá contener un archivo `README.md` y un archivo `.gitignore`.
- Podrá trabajar en todo momento sobre la rama principal: `master` ó `main`.
- La solución del problema deberá contener, **como mínimo** los aspectos básicos de un proyecto de ciencia de datos:
    - Análisis Exploratorio de Datos.
    - Ingeniería de Características - Data Wrangling
    - Entrenamiento, validación, evaluación y selección del modelo
    - Microservicio (API) para servir el modelo
    - Creación de imagen para dicha API. Explicar el procedimiento utilizado para crear la imagen y correr el contenedor. (Adjunte imagenes como prueba del funcionamiento del contenedor de la API)
- Deberá estructurar el proyecto de una manera asertiva. Hará parte de la evaluación la selección de la estructura del proyecto.
- Recuerde la importancia de los archivos `requirements.txt` y `Dockerfile` para el desarrollo del proyecto. Ubiquelos en la carpeta correcta.
- Este archivo `ExamenFinal.ipynb` póngalo en la carpeta raíz del repositorio.
- El `dataset` será brindado a usted a través de un enlace. Dicho dataset **NO** es necesario sincronizarlo en el repositorio ya que es muy pesado.
- Para resolver cada uno de los aspectos básico del proyecto, use y cree los cuadernos de `jupyter` y/o `scripts` de Python que considere necesario, acorde a la estructura del proyecto que escogió.
- El formato de presentación de todo el examen en general debe ser adecuado. Use tamaños de letra, colores, etiquetas, etcétera.
- No se resuelven dudas de ningún tipo por parte tanto del profesor de la asignatura como de ningún otro profesor. Por favor, absténgase de preguntar.
- Recuerde que también se está evaluando su capacidad de interpretar los resultados. Escriba sus interpretaciones/conclusiones
- La calificación del examen está distribuida de la siguiente manera:

|                      Aspecto a evaluar                       | Porcentaje |
|:------------------------------------------------------------:|------------|
|        Repositorio de Github debidamente configurado         | 10         |
|               Análisis Exploratorio de Datos.                | 10         |
|        Ingeniería de Características - Data Wrangling        | 10         |
| Entrenamiento, validación, evaluación y selección del modelo | 20         |
|          Micro-servicio (API) para servir el modelo          | 20         |
|              Creación de imagen para dicha API               | 20         |
|                         Conclusiones                         | 10         |


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

