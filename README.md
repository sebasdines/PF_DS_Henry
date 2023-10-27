# Proyecto final: Análisis de Yelp y Google Maps.

<br>


## Introducción

Somos parte de la consultora Mindful Data contratada por un inversor gastronómico proveniente del estado de Florida que planea instalar una franquicia de comida rápida en Florida y quiere que nuestra consultora realice un análisis de dos fuentes principales de información: las opiniones de los usuarios en Yelp y Google Maps para recomendarle qué franquicia de fast food le conviene adquirir y en qué lugar del estado de Florida. 

<br>

## Objetivos

El objetivo de este proyecto es realizar un análisis del mercado estadounidense específicamente del estado de Florida en el sector de restaurantes de comida rápida. El cliente que nos ha contratado es un inversor que planea instalar una franquicia de comida rápida en Florida y quiere que nuestra consultora de datos (Mindful Data) realice un análisis de dos fuentes principales de información: las opiniones de los usuarios en Yelp y Google Maps para recomendarle qué franquicia de fast food le conviene adquirir. 
Para cumplir con este objetivo, nuestro equipo se ha propuesto las siguientes metas:

Realizar un análisis de sentimientos y opiniones de las reseñas de Yelp y Google Maps para comprender la percepción de los usuarios sobre el sector fast food en Florida, Estados Unidos.

Predicción del crecimiento o declive del sector fast food basándonos en datos históricos. Para ello, utilizaremos diferentes técnicas de machine learning.

Sistema de recomendación de restaurantes de fast food.

Recomendación de sitios para nuevos locales mediante un modelo de machine learning, se identifican las ciudades dentro del estado de Florida para emplazar nuevos locales del sector en función de reseñas positivas.

<br>

## Alcance

Este proyecto se centrará en el análisis de las reseñas de los últimos 5 años de Yelp y Google Maps acerca de las cadenas de fast food más importantes de Estados Unidos con el objetivo de identificar cuál es la mejor opción a la hora de adquirir una franquicia y determinar en qué ciudad del estado de Florida conviene colocarla. 

<br>

## Roles

Dentro de nuestra Mindful Data Solutions hemos definido el grupo de trabajo para darle a curso a este proyecto, y los roles a cumplir por cada uno de los integrantes del mismo.
Cabe mencionar, que como la metodología de trabajo es por etapas, los roles pueden verse sujetos a modificación en función de las necesidades del proyecto. 

<br>

![roles](https://github.com/sebasdines/PF_DS_Henry/blob/master/src/Roles.png)

<br>

## Metodología de trabajo

Se adopta la metodología de trabajo Scrum con entregas parciales sobre los avances del proyecto. 

- Semana 1: Esta etapa constituye la puesta en marcha del proyecto y el tratamiento de los datos. Se trazan los objetivos, los alcances del proyecto así como los KPIs a evaluar. Además, se realiza el EDA preliminar de los datos. 

- Semana 2: Etapa de Data Engineering. Se crea, se implementa y se automatiza el datawarehouse. Además, se plantean los MVPs del dashboard y de los modelos de Machine Learning preliminares.

- Semana 3: Etapa final. Se completa principalmente el dashboard y se presenta el producto de Machine Learning. Además se realiza la entrega de la documentación y del repositorio completo. 

<br>

## Workflow

Optamos por Google Cloud como servicio en la nube para gestionar los datos, automatizar procesos y para el  procesamiento de aprendizaje automático :

Cloud Storage Buckets como datalake
Vertex Workbench para realizar el ETL de los datos
BigQuery, como datawarehouse para almacenar y procesar los datos.
Vertex AI para  implementar los modelos de aprendizaje.
Looker Studio como herramienta de visualización de datos y KPIs.

<br>


![workflow](./src/workflow.png)

<br>

## Análisis exploratorio de datos

<br>

En esta sección se realiza un primer análisis de los datos provistos por YELP y Google Maps. El objetivo de esta instancia es identificar los tipos de datos, conocer su calidad y los potenciales procesos de transformación a los que deberá ser sometida la data. Cabe mencionar, que en esta instancia no se intenta realizar un análisis exploratorio en profundidad, sino más bien tener un primer panorama de los dataset con su descripción general.  

<br>

El tratamiento de los datos previo al análisis exploratorio se presenta en los archivos: [Yelp.ipynb](Semana_1/Yelp.ipynb) y [Google_maps.ipynb](Semana_1/Google_maps.ipynb).

El análisis exploratorio de datos se presenta en el archivo: [EDA_preliminar.ipynb](Semana_1/EDA_preliminar.ipynb)

<br>


## KPIs

![KPI](<img width="370" alt="image" src="https://github.com/sebasdines/PF_DS_Henry/assets/131495435/4ade18fd-abf8-46a1-95da-996611d8e6ac">)

1. Aumento del 5% en el número de reseñas positivas de Yelp y Google para los negocios de Fast food en comparación al año anterior.
Fórmula: (Cantidad de reseñas año actual - Cantidad de reseñas año anterior) /(reseñas anterior)

2. Disminución del número de reseñas negativas del 5% de Yelp y Google para los negocios de Fast food es menor en comparación al año anterior .

Fórmula: (Cantidad de reseñas año anterior - Cantidad de reseñas año actual) /(reseñas anterior)


3. Aumentar el Índice de Satisfacción del Usuario en un 10% durante el próximo semestre.

Fórmula: Índice de Satisfacción del Usuario = (Ponderación_Yelp * Rating_Yelp + Ponderación_Google * Rating_Google) / (Ponderación_Yelp + Ponderación_Google)

- Ponderación_Yelp: Peso en proporción al total (1- total google)
- Rating_Yelp: Puntuación promedio de Yelp para un restaurante o categoría de restaurantes.
- Ponderación_Google: Peso en proporción del total (1- total yelp)
- Rating_Google: Puntuación promedio de Google para un restaurante o categoría de restaurantes.

4. Identificar 3 áreas estratégicas para franquicias de comida rápida en Florida en intervalos semestrales.
Forma: Localización geográfica de los restaurantes de fast food con stars mayor a 4 para identificar posibles lugares de inversión. 
Fórmula: (Número de restaurantes de comida rápida con rating > 4 en ubicaciones estratégicas) / (Número total de restaurantes de comida rápida en Florida).

5. Lograr una distribución más uniforme de visitas a lo largo del día durante el próximo trimestre.
Fórmula: (Visitas en una hora específica / Total de visitas en el período) x 100

<br>


## Entregables
Los entregables de esta semana se encuentran en la carpeta Semana 1: 

- Tratamiento de datos previo al EDA preliminar: [Yelp.ipynb](Semana_1/Yelp.ipynb)  y [Google_maps.ipynb](Semana_1/Google_maps.ipynb)
- [EDA_preliminar.ipynb](Semana_1/EDA_preliminar.ipynb)
- [Informe](Semana_1/Informe.pdf)
- [Presentacion](Semana_1/Presentacion.pdf)
