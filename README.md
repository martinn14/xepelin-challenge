# xepelin-challenge

Solucion propuesta por Martin Jourdan al challenge de data de Xepelin

## Consideraciones generales:
Para la solución de los ejercicios propuestos, se proveen los siguientes archivos:

- 1 script .py "xepelin_pipeline_challenge.py" con las funciones y la lógica completa a ejecutar
- 1 archivo "requirements.txt" con las librerias a instalar para la ejecución del script python
- 1 archivo "sftp_config_example.json" que contiene las credenciales del sftp a utilizar (se provee uno de prueba)
- 1 archivo "orders_2023-10-01.csv" con datos de muestra, los mismos que fueron propuestos en el enunciado del ejercicio "pipeline"
- 1 archivo "xepelin_sql_challenge.sql" con la creación de tablas y esquema, carga de datos de prueba y la consulta solicitada en el ejercicio "sql"



## Ejercicio "Pipeline":

El script que ejecuta la logica es "xepelin_pipeline_challenge.py". El mismo requiere recibir como parametro la fecha para la que se quiere procesar la data. Dicho parametro será utilizado para construir el nombre del archivo que buscará en el sftp. Por ejemplo

python xepelin_pipeline_challenge.py --date 2023-10-01

Buscara el archivo "orders_2023-10-01.csv" en el sftp y procesará los datos del mismo

En caso de no especificarse dicha fecha, el script fallará dado que es un dato requerido.

Algunas aclaraciones:
-  El ejercicio procesa la data del dia indicado por el nombre del archivo, sobreescribiendo la data que pueda existir de esa misma fecha y sin modificar la data de otras fechas.
-  En la lógica adjunta, no se considera ningún tipo de planificación ni orquestación de ejecución.
-  Respecto al punto anterior, se sugiere para la implementación de una ejecución diaria, el uso de una herramienta orquestadora como Airflow.
-  La solución propuesta no fue probada en un entorno de Big Query por no contar con el mismo.
-  Para la conexión a Big Query, se eligió la autenticación via cuenta de servicio a través de un archivo de credenciales .json que debe estar en el entorno en que se ejecute el script. Es posible especificar el path del mismo en la linea 40 del código (esto podria tambien llevarse al archivo de configuración JSON a fines de no tener que modificar el .py, yo elegí no hacerlo para hacer foco solo en lo solicitado) 


## Ejercicio "SQL":

El archivo "xepelin_sql_challenge.sql" contiene todo lo requerido para ejecutar la lógica:

1) en primer lugar se crea el esquema y las tablas requeridas
2) Luego se insertan algunos datos de prueba
3) Por último, se proporciona la consulta solicitada

Dicho script se resolvió utilizando sintaxis de Redshift, dado que es el motor de consulta del que dispuse para poder realizar las pruebas.
Se utilizan funciones ventana para los cálculos solicitados.



