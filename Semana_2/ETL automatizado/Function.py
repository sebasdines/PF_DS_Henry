import pandas as pd
from pandas.io import gbq
from google.cloud import bigquery
import functions_framework
import json
import pickle

def hello_gcs(event, context):

    """
    Triggered by a change to a Cloud Storage bucket.
    Args:
        event (dict): Event payload.
    """

    try:
        # Obteniendo ruta de archivo modificado y tipo de archivo
        file_bucket = event["bucket"]
        file_path = event['name']
        file_name = file_path.split('/')[-1].split('.')[-2]
        full_path = 'gs://' + file_bucket + '/' + file_path
        
        # Ejecuta el código si los archivos se cargan en la carpeta correcta del bukcet
        if '/' in file_path:
            main_folder = file_path.split('/')[0]

            # Especifica el conjunto de datos y la tabla donde va a almacenar en bigquery
            if main_folder == "metadata":
                
                # Especifica proyecto, conjunto de datos y tabla de bigquery a trabajar
                project_id = 'festive-freedom-402511'
                dataset = "proyectofinal."
                table_name = "negocios_gm"
                
            elif main_folder == "reviewFL":
                
                project_id = 'festive-freedom-402511'
                dataset = "proyectofinal."
                table_name = "review_gm"
                
            elif main_folder == "yelp_data":
                
                project_id = 'festive-freedom-402511'
                dataset = "proyectofinal."
                table_name = "business_yelp"
            
            
                
                # crea el data segun el tipo de archivo
                data = leer_archivo(full_path)

                # llama la funcion para limpiar el data
                data_limpia = limpiar_data(data)
                
                # llama a la funcion para cargar el data
                cargar_data(project_id, dataset, table_name, data_limpia)

    except Exception as e:
        print(f"An error occurred: {e}")

def leer_archivo(f_path):
    """
    Lee el archivo según su extensión. Disparado por la funcion "captura_evento"
    Args:
        event (dict): Event payload.
        file_path (str): ruta del archivo
        file_type (str): tipo del archivo
    """
    # Extraer el tipo de archivo
    f_type = f_path.split('.')[-1]
    
    # Revisando si archivo es csv
    if f_type == 'csv':
        # Leyendo archivo en dataframe
        data = pd.read_csv(f_path)

    # Revisando si archivo es json    
    elif f_type == 'json':
        try:
            # Intentar leer el archivo json como si no tuviera saltos de linea
            data = pd.read_json(f_path)
        except ValueError as e:
            if 'Trailing data' in str(e):
                # Leer el archivo json conteniendo saltos de linea
                data = pd.read_json(f_path, lines = True)
            else:
                # Cualquier otro error
                print('Ocurrió un error cargando el archivo JSON:', e)

    # Revisar si el archivo es tipo parquet
    elif f_type == 'parquet':
        # Leyendo archivo en dataframe
        data = pd.read_parquet(f_path)

    # Revisar si el archivo es tipo pkl (Pickle)
    elif f_type == 'pkl':
        try:
            # Leyendo archivo en DataFrame desde Google Cloud Storage
            data = pd.read_pickle(f_path)
        except Exception as e:
            print(f'Ocurrió un error al leer el archivo Pickle: {e}')
    
    return data , f_path


def limpiar_data(data, f_path):
    """
    Limpia el data "sales_count_month". Disparado por la funcion "captura_evento"
    Args:
        data (DataFrame): dataframe a limpiar.
    """
    
    try:
        """BLOQUE 1: modificar el dataframe"""

        if '/' in f_path:
            file = f_path.split('/')[0]
            
            if file == "metadata":
                # Elimino id diplicados
                data.drop_duplicates(subset='gmap_id', inplace=True)
                #Creo columna city
                data['city'] = data['address'].str.split(',').str[-2]
                # Separo el postal code de la columna address    
                data['address'] = data['address'].str.split(',').str[-1]
                data['postal_code'] = data['address'].str.slice(-5)
                # Cambio el tipo de dato de la columna address
                data['postal_code'] = pd.to_numeric(data['postal_code'], errors='coerce')
                data['postal_code'] = data['postal_code'].dropna()
                data['postal_code'] = data['postal_code'].dropna().astype(int)
                # Filtro por el codigo postal de florida 32003 hasta 34997
                data = data[(data['postal_code'] >= 32003) & (data['postal_code'] <= 34997)]
                # Función para filtrar la categoria
                def buscar_coincidencias(lista):
                    if lista is None:
                        return False
                    else:
                        texto = ' '.join(lista).lower()
                        for palabra in categorias:
                            if re.search(r'\b' + re.escape(palabra.lower()) + r'\b', texto):
                                return True
                        return False
                # Verifico si alguna de las categorias esta en la columna 'category' llamando a la funcion buscar coincidencia
                data['categorias'] =  data['category'].apply(buscar_coincidencias)
                # Filtro el data me quedo con las que se encontro resultado en la nueva columna
                data = data[data['categorias']]
                # Elimino columnas innecesarias
                columns = ['description', 'address', 'price', 'postal_code', 'hours', 'MISC', 'state', 'relative_results', 'url', 'categorias'] 
                data.drop(columns, axis=1, inplace=True)
                
            
            if file == "review_FL":
                # Selecciono las columnas que voy a utilizar
                data = data[['user_id', 'name', 'time', 'rating', 'text', 'gmap_id']]
                # Elimino duplicados
                duplicados = data.duplicated(keep='first')
                indice_duplicado = duplicados[duplicados].index
                data.drop(indice_duplicado, inplace=True)
                data.reset_index(drop=True, inplace=True)
                # Cambio el tipo de fecha
                data['time'] = pd.to_datetime(data['time'], unit='ms').dt.date
                # Filtro registros a partir de 2017(últimos 5 años)
                data=data[data['time'].apply(lambda x: x.year)>=2017]
                # Reordeno las columnas
                columnas = ['user_id', 'name', 'time', 'rating', 'text', 'sentiment_analysis', 'gmap_id']
                data = data[columnas]
                data.reset_index(drop=True, inplace=True)
                
                
                
                
            if file == "yelp_data":
                
                #Eliminamos las columnas duplicadas
                data = data.loc[:, ~data.columns.duplicated(keep='first')]

                #Filtramos las ciudades de Florida por código postal
                data = data.copy()
                data['postal_code']=data['postal_code'].astype(str)
                data_florida = data[(data['postal_code'] >= '32822') & (data['postal_code'] <= '34997')]

                #Filtramos también por longitude
                data_florida = data_florida.copy()
                data_florida['longitude']=data_florida['longitude'].astype(str)
                data_florida = data_florida[(data_florida['longitude'] >= '-82.10073072') & (data_florida['longitude'] <= '-82.851044')]
                
                #Eliminamos los vacíos de categories
                data_florida= data_florida.dropna(subset=['categories'])

                #Filtramos por palabras claves en columna category
                filtro = data_florida['categories'].str.contains(r'restaurant|restaurante|fast\s*food|hamburger|pizza|sandwich', case=False, regex=True)
                data_florida = data_florida[filtro]

                #Elimino las columnas que no voy a utilizar
                data_florida=data_florida.drop(columns=['address','state', 'postal_code','is_open','attributes','categories','hours'])
               
        return data

    except Exception as e:
        print(f"An error occurred: {e}")
        
def cargar_data(project, dataset, table, data):
    """
    Carga el df limpio en bigquery. Disparado por la funcion "captura_evento"
    Args:
        project_id (str): nombre del proyecto
        dataset (str): ubicacion del dataset de destino en bigquery
        table_name (str): nombre de la tabla de destino en bigquery
        data_limpia (DataFrame): dataframe limpio para cargar a bigquery
    """
    
    try:
        # convierte todo el dataset a str para almacenar
        data = data.astype(str)
        
        # guarda el dataset en una ruta predefinida y si la tabla ya está creada la reemplaza
        data.to_gbq(destination_table = dataset + table, 
                    project_id = project,
                    table_schema = None,
                    if_exists = 'append',
                    progress_bar = False, 
                    auth_local_webserver = False, 
                    location = 'us-east1')
            
    except Exception as e:
        print(f"An error occurred: {e}")    