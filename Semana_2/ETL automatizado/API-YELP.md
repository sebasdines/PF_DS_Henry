<h1 align="center"> Uso-API-YELP </h1>
   
![oct97bs0bc08xb8eawfo](https://github.com/JLaurencioAJimenez/FastApi-Deploy/assets/135534222/220ccf33-527e-4488-8ee2-7ffe3928352a)

<h1 align="center"> Por que la usamos? </h1>
Ya que la API de YELP ofrece una gran cantidad informacion que es valiosa para nostros los Data Scientist y los dueños de Franquicias o restaurantes,
donde podremos tomar decisiones basadas en las experiencias de los usuarios, podremos recibir retroalimentaciones para mejorar y analizar el entorno del mercado en los restaurantes o franquicias mas famosas de Estados Unidos, Florida.

<h1 align="center"> Script </h1>

El codigo que creamos tiene de objetivo tomar las reseñas de un restaurante en especifico usando una ID proporcionada por YELP, esto podra aumentarse a franquicias pidiendo contrato con YELP.

<h1 align="center"> Que nos entregara? </h1>

Este nos entregara un dataframe con las reviews del nuestro restaurante, donde se encuentran 

   - Las reviews con texto del cliente
   - Su calificacion de estrellas al restaurante
   - Cuando se escribio esta review y en que restaurante con su direccion
   - Un análisis de los usuarios que vieron la reseña  donde se clasificara si es "Util","Divertida" o "Buena"

<h1 align="center"> Datalake </h1>

Una vez tengamos las reseñas desde la API estas se pasaran automaticamente a un Datalake en bucket_google_cloud, este servicio nos proporciona un almacen de datos de forma virtual
donde podremos guardar grandes volumenes de datos en su formato original.

En la imagen se puede observar el archivo de "Reviews_Yelp" que es la informacion obtenida desde la API
![e](https://github.com/JLaurencioAJimenez/FastApi-Deploy/assets/135534222/a0554ba0-95c8-487b-a5ff-bfeca9d1c416)

<h1 align="center"> Conclusión </h1>

Integrar la API de yelp nos ayudara a conseguir informacion valiosa para el propietario y los Data analyst de forma eficiente, automatica y facil para luego poder tomar diferentes 
decisiones basadas en los datos obtenidos.

Gracias a la automatizacion se pueden ahorrar tiempo, recursos y eliminar los procesos manuales.

<h1 align="center"> Slack Tecnologico </h1>

   - Google Cloud
   - Google Functions
   - YELP API
   - Python
