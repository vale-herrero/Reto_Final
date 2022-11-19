# Reto_Final

Si se parte del 1 se puede ir al 6 y al 8 (dos movimientos); si se sale del 2 se puede llegar al 7 y al 9 (dos movimientos más); iniciando desde el 3 se puede arribar al 4 y al 8 (se suman nuevamente dos); si se arranca desde el 4 las posibilidades son 3, 9 y 0 (ahora se acumulan tres movimientos); pero si la po- sición inicial es el 5 no se puede mover la ficha a ningún lugar dado que no hay movimientos válidos
–sin embargo aún restan varias posibilidades más para seguir probando–; desde el 6 se pueden alcan- zar el 1, 7 y 0 (nuevamente se agregan tres más); por su parte desde el 7 se puede mover la ficha hasta el 2 y el 6 (la cantidad se incrementa en dos); si se toma el 8 como inicio se pueden alcanzar el 1 y el 3 (se adicionan dos movimientos); si se posiciona la ficha en el 9 las opciones para moverse son 2 y 4 (nue- vamente se tienen dos movimientos); y por último si se sale desde el 0 los movimientos válidos son 4 y 6 (se suman los últimos dos). En total se pueden realizar veinte movimientos válidos con esta ficha.

Ahora, diseñe un algoritmo que permita calcular cuántos posibles movimientos válidos puede rea- lizar la ficha del caballo, recibiendo como entrada la cantidad de movimientos a realizar desde el inicio, partiendo de todos los números. Por ejemplo, como mostramos anteriormente si la cantidad de movimientos es uno, la cantidad de movimientos válidos son veinte. Pero si la cantidad de mo- vimientos son dos y se sale desde el 1 se puede ir hasta el 6 y el 8 (un movimiento), a continuación, a partir del 6 hasta el 1, 7 y 0 (dos movimientos de la ficha), luego se sigue desde el 8 hasta el 1 y 3 (para alcanzar los dos movimientos de la ficha). En resumen, se tienen cinco posibles movimientos válidos partiendo desde el 1 (1-6-1, 1-6-7, 1-6-0, 1-8-1 y 1-8-3) a estos se deben sumar todos los movi- mientos que resulten de partir de los demás número. En total la cantidad de posibles movimientos válidos para dos movimientos son 46. Una vez desarrollado el algoritmo complete la siguiente tabla.
 
Cantidad de movimientos
Posibilidades válidas
1
20
2
46
3
104
5
 
8
 
10
 
15
 
18
 
21
 
23
 
32
 
Pasemos a trabajar en otro ejemplo para fortalecer aún más nuestro pensamiento algorítmico, en este caso el problema de las n-reinas, el mismo consiste en ubicar n reinas en un tablero de ajedrez de tamaño n x n, sin que las mismas se amenacen. Recuerde que la reina desplaza de manera hori- zontal, vertical y diagonal como se puede observar en la figura 2, además podemos ver una solución al problema de las 4 reinas. Nótese que una parte importante para resolver un problema es de que manera representar la solución, para este caso particular usamos un vector de n posiciones (colum- nas) y el valor almacenado representa la fila donde se ubica dicha reina.

 
 	 

 
Figura 2. Problema de las n-reinas

Cuando haya entendido el problema y tenga una solución en mente, desarrolle un algoritmo que per- mita hallar al menos una solución para distintas cantidades de reinas, y luego complete la siguiente tabla.
 
n-reinas
Soluciones distintas
Todas las soluciones
Una solución
1
1
1
[0]
2
0
0
-
3
0
0
-
4
1
2
[1, 4, 0, 3]
5
2
10
 
6
1
4
 
7
6
40
 
8
12
92
 
9
46
352
 
10
92
724
 
15
285 053
2 279 184
 
 
 
 
Del algoritmo a las estructuras de datos:
¡A implementar!
Para implementar los algoritmos y definir las estructuras de datos se puede utilizar cualquier len- guaje de programación como C, Java, Delphi, C++, Javascript. Como lo indica el título de esta asignatura, se optó por trabajar con el lenguaje Python por su versatilidad, creciente popularidad y demanda en estos últimos años. A su vez, se buscó darle un enfoque ágil sin dejar de lado las metodologías estructuradas de estos temas. Los ejemplos están codificados de la manera clásica utilizando unos pocos comandos particulares del lenguaje, para que puedan ser codificados en cualquier otro len guaje que se prefiera, sin realizar cambios significativos. Los ejemplos pueden ser ejecutados utilizando cualquier versión “3.x” de Python dado que la versión “2.x” esta descontinuada a partir de  enero del 2020 (si se trabaja con alguna versión anterior se deberá hacer algunas modificaciones para adaptar el código y que funcione en dicha versión).
 
¿Qué es Python?
Python es un lenguaje de programación creado por Guido Van Rossum a principios de los años no- venta, es un lenguaje que posee una sintaxis clara y estructurada que favorece a generar un código legible. Es administrado por la Python Software Foundation, posee una licencia de código abierto, denominada Python Software Foundation License, que es compatible con la Licencia pública gene- ral de GNU a partir de la versión 2.1.1.
 
Se trata de un lenguaje interpretado o de script, con tipado dinámico, multiplataforma y orientado a objetos, además cuenta con una gran cantidad de librerías y frameworks disponibles. La sintaxis de Python es sencilla y cercana al lenguaje natural. Por estas razones se trata de uno de los mejores

lenguajes para comenzar a programar, –ya que es como programar en pseudocódigo–, y la curva de aprendizaje es bastante alta y rápida.
 
Es una tecnología muy utilizada en la actualidad, por su simplicidad y potencia permite realizar aplicaciones de una manera rápida, sencilla y óptima para el despliegue en distintas plataformas, además permite utilizar algoritmos de machine learning e inteligencia artificial en producción. Exis- ten muchos casos de grandes empresas que utilizan Python en sus aplicaciones con gran éxito, tal es el caso de Google, la NASA, Netflix, Mercado libre, Spotify, Dropbox, Instagram, Pinterest, Glo- bant, Sattelogic y un largo etcétera.
 
Un lenguaje interpretado o de script es aquel que se ejecuta utilizando un programa intermedio llamado intérprete, en lugar de compilar el código a lenguaje máquina que pueda comprender y ejecutar directamente una computadora. La ventaja de los lenguajes compilados es que su ejecu- ción es más rápida. Sin embargo, los lenguajes interpretados son más flexibles y más portables.
 
Python tiene, no obstante, muchas de las características de los lenguajes compilados, por lo que se podría decir que es seminterpretado. En Python, como en Java, Delphi y muchos otros lenguajes, el código fuente se traduce la primera vez que se ejecuta a un pseudocódigo máquina intermedio llama- do bytecode, generando archivos “.pyc” o “.pyo”, que son los que se ejecutarán en sucesivas ocasiones.
 
La característica de tipado dinámico se refiere a que no es necesario declarar el tipo de dato que va a contener una variable, sino que su tipo se determinará en tiempo de ejecución según el tipo del valor al que se asigne, y el tipo de esta variable puede cambiar si se le asigna un valor de otro tipo, lo cual le otorga una gran flexibilidad a la hora de programar.
 
En los lenguajes con esta característica no se permite tratar a una variable como si fuera de un tipo distinto al que tiene, es necesario convertir de forma explícita dicha variable al nuevo tipo previa- mente. Por ejemplo, si tenemos una variable que contiene un texto (variable de tipo cadena o string) no podremos tratarla como una variable numérica, sin previamente realizar una conversión.
 
La programación orientada a objetos es un paradigma en el que los conceptos del mundo real rele- vantes para nuestro problema se trasladan a clases y objetos en nuestro programa. La ejecución del programa consiste en una serie de interacciones e intercambio de mensajes entre los objetos. No obstante, el lenguaje soporta también los paradigmas de programación imperativa y funcional (este último le permite al lenguaje añadir características avanzadas muy interesantes).
 
El intérprete de Python está disponible en muchas plataformas de las más comunes (Linux, UNIX, Mac OS, Solaris, DOS, Windows, etc.) por lo que si no utilizamos librerías específicas de cada plata- forma nuestro programa podrá correr en todos estos sistemas sin tener que realizar ningún tipo de cambio. Esto nos permite desarrollar programas que sean portables de un sistema operativo a otro.
 
La filosofía de los creadores de Python entiende que la gran sencillez, flexibilidad y potencia del lenguaje debe ir acompañada de una correcta formación del programador que lo utiliza para poder realizar las actividades de desarrollo con criterio, dado que la inexperiencia de los nuevos progra- madores puede conducirlos a programar de manera incorrecta (aunque lleguen a un resultado).
