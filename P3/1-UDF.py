import sqlite3 #Libreria sqlite3 instalada ya con python
# import pandas as pd Se importa pandas para trabajar con datos, hay que ver curso python

try:

    square = lambda n : n*n; #lambda hace mencion a una funcion flecha y a su vez se declara una función
    print(square(10));

    # conn = sqlite3.connect("C:/Users/yaric/Documents/PROGRAMACION/CURSOS/SQL/P3/database/Northwind.db"); Así sería si estuviera en otra ubiación
    conn = sqlite3.connect("P3/database/Northwind.db"); #Se realiza la conexión a la base de datos
    conn.create_function("sqlite_square", 1, square)

    # En python hay algo llamado cursores, esto lo que indica es que le va a pedir información a la base de datos, pero es como decir yo me hago cargo de ella, yo la formateo, etc.

    cursor = conn.cursor() #se declara un cursor
    #Se ejecuta SQL
    cursor.execute (
        '''
        SELECT * FROM Products
        ''');

    results = cursor.fetchall(); #Con fetchall se obtiene la información
    # results_df = pd.DataFrame(results); ver curso py

    conn.commit(); #De esta forma ejecutamos un COMMIT, que en SQL es asentar los cambios realizados

    cursor.close(); #De esta manera se libera al cursor
    conn.close(); #De esta manera se libera a la conexión
    #La libreación de los elementos es importante para así evitar un consumo innecesario de recursos
    print (results);

except Exception as ex:
    print(ex);