import sqlite3; #Para la conexión con el gestor
import pandas as pd;    #Para el ordenamiento de los datos
import matplotlib.pyplot as plt;    #Para la generación de gráficos

# PARA OBTENER A LOS 10 PRODUCTOS QUE MÁS GENERAN INGRESOS
conn = sqlite3.connect("P4_EJERCICIOFINAL/database/Northwind.db");
query = '''
    SELECT ProductName, SUM(Price * Quantity) as Revenue
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
'''

top_products = pd.read_sql_query(query, conn);  #Este método se encarga de el cursor, de abrir la consulta, de cerrarla, etc. SOLO SE DEBE INDICAR LA CONSULTA Y LA CONEXIÓN

# print(top_products);  #Esto imprime los valores 

# -- COMIENZO DE LA GRÁFICA A LOS PRODUCTOS QUE MÁS GENERAN INGRESOS

top_products.plot(x = "ProductName", y = "Revenue", kind = "bar", figsize = (10, 5), legend = False); #x nos pide una lista/tupla con los datos del eje x; y lo mismo para y; kind dtermina el tipo de gráfico, figsize determina el tamaño

plt.title("10 Poductos más rentables");
plt.xlabel("Productos");
plt.ylabel("Revenue");
plt.xticks(rotation = 90);    #De esta manera se indica que los valores se roten 90 grados en el eje x, para que así las leyendas no abarquen demasiado espacio a la horizontal, y puedan caber todos nuestros parámetros
plt.show();
# -- FINALIZACIÓN DE LOS PRODUCTOS QUE MÁS GENERAN INGRESOS

# OBTENIENDO A LOS 10 EMPLEADOS MÁS EFECTIVOS

# || Esto es concatenación, se usará en nuestra consulta y es para sumar valores, como cuando sumamos strings por ejemplo
query2 = '''
    SELECT FirstName || " " || LastName as Employee, COUNT(*) as Total
    FROM Orders o
    JOIN Employees e
    ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total DESC
    LIMIT 10
'''

top_employees = pd.read_sql_query(query2, conn);
top_employees.plot(x = "Employee", y = "Total", kind = "bar", figsize = (10, 5), legend = False);

plt.title("10 Empleados Más Efectivos");
plt.xlabel("Empleados");
plt.ylabel("Total Vendido");
plt.xticks(rotation = 45);

plt.show();