#Otra manera de hacer las cosas y mejor

import sqlite3 #Libreria sqlite3 instalada ya con python

try:

    square = lambda n : n*n; #lambda hace mencion a una funcion flecha y a su vez se declara una función
    
    with sqlite3.connect("P3/database/Northwind.db") as conn:
        conn.create_function("sqlite_square", 1, square);
        cursor = conn.cursor();
        cursor.execute('SELECT *, sqlite_square(Price) FROM Products WHERE Price > 0'); #De esta manera nosotros ya estamos trabajando con la función creada dentro de lo que sería una consulta SQL y a su vez, como se puede mostrar al ejecutarse, lo que se indica es que el resultado será elevado al cuadrado.
        results = cursor.fetchall();

    print(results);

    #De esta manera como se puede obsrvar, es menos código y a su vez ya no es necesario cerrar la conexión

except Exception as ex:
    print(ex);