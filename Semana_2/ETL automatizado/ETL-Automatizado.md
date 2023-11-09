<p align='center'>
<img src ="/src/data.jpg">
<p>

<h1 align='center'>
 <b>ETL Automatizado</b>

 <b>Carga Incremental</b>
</h1>
 




# **Flujo de trabajo**

Para la extracción, transformación y carga de datos del proyecto, se siguió el siguiente flujo:

<p align='center'>
<img src ="/src/pipeline.png">
<p>

<h1 align="center">Tecnologias utilizadas</h1>

<p align='center'>
<img src="/src/python.png" width="60" height="60">
<img src="/src/jupyter.png" width="60" height="60">
<img src="/src/pandas.png" width="60" height="60">
<img src="/src/gcloud.png" width="60" height="60">
<p>

# **Data Lake**


 Como primera instancia, dentro de la plataforma GCP se crea un datalake utilizando Cloud Storage Bucket. Se realiza la carga manual de los archivos crudos a traves de Google Cloud SDK Shell y con la ingesta de las APIs de Gmaps y Yelp!(mostraremos una simulación).



<p align='center'>
<img src ="/src/bucket.png">
<p>

# **Cloud Function**

Para la automatizacion del proceso de ETL, implementamos Google Cloud Functions, al ingresar un archivo al Bucket indicado se inicia el proceso de ETL, que incluye la validacion, transformacion, limpieza y carga de datos al Data Warehouse en Big Query.



<p align='center'>
<img src ="/src/cloud_function.png">
<p>



# **Data Warehouse**

Elegimos Big Query como nuestra estructura de base de datos, donde se almacenan y gestionan todos los datos limpios desde esta estructura se van a tomar los datos para los modelos de machine learning y para las consultas que requieran los analistas de datos para generar las visualizaciones

<p align='center'>
<img src ="/src/bigquery.png">
<p>



# **Video Carga Incremental**

Video carga incremental con etl automatico automatica
En el video se puede ver: una consulta para ver la cantidad de registros de reviews, a continuacion se ingresa manualmente un archivo con 100 registros de un dataset sintetico, se observa la actividad en el Cloud Function y para finalizar se hace una nueva consulta para verificar el incremento en los registros.


<a href="https://drive.google.com/file/d/18R-IQxnabxLFVNuzl6xtp4X0Iz63pCyg/view?usp=drive_link"><video src ="/src/video_carga.mp4" style="width: 1024px; max-width: 100%; height: auto" title="Click en la imagen" >


<video width="1024" controls>
  <source src="https://github.com/sebasdines/PF_DS_Henry/blob/master/src/video_carga.mp4" type="video/mp4"> </video>