a) Descripción del problema que estás modelando.
Se modelo la distribución y las conexiones entre las diferentes areas de un cine para optimizar el flujo de clientes, calcular rutas optimas y analizar la accesibilidad entre zonas.

b) Qué representa cada vértice.
Entrada Principal - Acceso al cine.
Taquilla - Punto de venta de boletos.
Dulceria - Punto de venta de alimentos y bebidas.
Sala 1, 2 y 3 - Salas de proyección de peliculas.
Lobby Central - Area de distribución y espera.
Baños - Sanitarios.
Salida de Emergencia - Salida en caso de emergencia.

c) Qué representa cada arista.
Cada arista representa una conexion (pasillo o corredor) entre dos areas, con su peso indicando la distancia en metros.

d) Diagrama del grafo.
El diagrama es el documento "diagrama3.jpg".

e) Análisis: grados, conexidad, ciclos si existen.
Vertice  / Grado / Conexiones
Entrada  /   1   /   Lobby   
Taquilla /   2   /   Lobby, Sala1   
Dulcería /   2   /   Lobby, Sala3   
Sala 1   /   2   /   Lobby, Taquilla  
Sala 2   /   1   /   Lobby  
Sala 3   /   3   /   Lobby, Dulceria, Baños   
Lobby    /   5   /   Entrada, Taquilla, Dulceria, Sala1, Sala2   
Baños    /   2   /   Sala3, Salida   
Salida Emerg/ 1  /   Baños   

f) Una pregunta interesante que puedas responder con tu grafo.
¿Cuál es la ruta más corta para que un cliente que entra al cine compre palomitas y llegue a la Sala 2?
La ruta más corta es Entrada > Lobby > Dulcería > Lobby > Sala2
Ya que la distancia total es de 19 metros a comparacion de otras rutas.
