# README APP
En esta carpeta se encuentran los archivos necesarios para la ejecución de la API, su imagen y su contenedor docker.

- Estructura:
  - App
    - Modelos
      - CNN.h5 -> Red Neuronal (En caso de querer usarse)
      - Dict_trans.pkl -> Diccionario con las transformaciones para las etiquetas de la variable de categoría.
      - Logistic_Reg.pkl -> Modelo de Regresión Logística (Es el modelo a usar en la API).
      - Norm_Model.pkl -> Modelo para normalizar los inputs.
      - TfIdf_Model.pkl -> Modelo para crear las matrices Tf e Idf para el resultado del modelo 'Vectorizer'.
      - Vectorizer.pkl -> Modelo para vectorizar el texto de la variable de descripción.
    - dockerfile -> Manifiesto para el contenedor de docker
    - main.py -> Script para ejecutar la API
    - requirements.txt -> requerimientos para la API