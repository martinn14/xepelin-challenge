# xepelin-challenge

Solucion propuesta por Martin Jourdan al challenge de data de Xepelin

## Consideraciones generales:
Para la solución de los ejercicios propuestos, se proveen los siguientes archivos:

- 1 script .py "xepelin_pipeline_challenge.py" con las funciones y la lógica completa a ejecutar
- 1 archivo "requirements.txt" con las librerias a instalar para la ejecución del script python
- 1 archivo "sftp_config_example.json" que contiene las credenciales del sftp a utilizar (se provee uno de prueba)
- 1 archivo "orders_2023-10-01.csv" con datos de muestra, los mismos que fueron propuestos en el enunciado del ejercicio "pipeline"
- 1 archivo preguntas.txt con las respuestas a las preguntas teóricas planteadas en el ejercicio "pipeline"
- 1 archivo "xepelin_sql_challenge.sql" con la creación de tablas y esquema, carga de datos de prueba y la consulta solicitada en el ejercicio "sql"



## Ejercicio "Pipeline":

El script que ejecuta la logica es "xepelin_pipeline_challenge.py". El mismo requiere recibir como parametro la fecha para la que se quiere procesar la data. Dicho parametro será utilizado para construir el nombre del archivo que buscará en el sftp. Por ejemplo

python xepelin_pipeline_challenge.py --date 2023-10-01

Buscara el archivo "orders_2023-10-01.csv" en el sftp y procesará los datos del mismo

En caso de no especificarse dicha fecha, el script fallará dado que es un dato requerido.


## Ejercicio "SQL":

El archivo "xepelin_sql_challenge.sql" contiene todo lo requerido para ejecutar la lógica:

1) en primer lugar se crea el esquema y las tablas requeridas
2) Luego se insertan algunos datos de prueba
3) Por último, se proporciona la consulta solicitada

Dicho script se resolvió utilizando sintaxis de Redshift, dado que es el motor de consulta del que dispuse para poder realizar las pruebas.
Se utilizan funciones ventana para los cálculos solicitados.



