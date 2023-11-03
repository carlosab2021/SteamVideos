# <p align="center"> SteamVideos</p>

<p align="justify">Este es un proyecto individual relacionado con Machine Learning Operations (MLOps) para la plataforma Steam, donde se  crea un sistema de recomendación de videojuegos para usuarios. Me enfrente a varios desafíos en la manipulación y limpieza de datos mal estructurados en archivos JSON.</p>

<p align="center">Fundamentación del Proyecto MLOps para Steam</p>
<p align="justify">El proyecto MLOps desarrollado para Steam tiene como objetivo principal la creación de un sistema de recomendación de videojuegos personalizados para usuarios. Steam, una plataforma multinacional de videojuegos, se enfrenta al desafío de proporcionar a sus usuarios recomendaciones precisas y relevantes en un entorno con datos desafiantes, como archivos JSON mal estructurados, datos anidados y falta de procesos automatizados para la actualización de nuevos productos.</p>
<p align="justify">El proyecto se inicia con la adquisición de archivos JSON de gran tamaño que contienen información sobre usuarios, reseñas de videojuegos, detalles de juegos y más. Estos archivos presentan dificultades significativas en términos de estructura de datos y acceso a la información. Para abordar este problema, se utiliza Python y la biblioteca Pandas para llevar a cabo el proceso de Extracción, Transformación y Carga (ETL) de los datos.
Uno de los desafíos iniciales fue superar la dificultad de leer los archivos JSON debido a su estructura compleja y anidada. Se realizaron múltiples intentos de carga, lo que resultó en la creación de numerosos archivos CSV temporales con diferentes modificaciones y tamaños para explorar y comprender mejor los datos.
Una vez que se logró cargar los datos, se llevaron a cabo múltiples tareas de limpieza y transformación. Los datos se agruparon en columnas pertinentes, se eliminaron registros nulos o irrelevantes y se realizaron análisis de sentimientos sobre las reseñas de los usuarios.</p>
<p align="justify">La columna 'sentiment_analysis' se creó utilizando técnicas de Procesamiento de Lenguaje Natural (NLP) con TextBlob, asignando valores numéricos para describir el sentimiento general de las reseñas (0 para malo, 1 para neutral y 2 para positivo).</p>
<p align="justify">Además, se consolidaron los datos de varios archivos y se unieron mediante identificadores únicos para crear un conjunto de datos completo y coherente. Este conjunto de datos final contiene información esencial sobre usuarios, juegos, reseñas y detalles del juego, lo que lo convierte en la base para desarrollar un sólido sistema de recomendación.
En resumen, el proyecto MLOps para Steam abordó con éxito los desafíos de datos complejos y poco estructurados para crear un sistema de recomendación de videojuegos eficiente y preciso. El análisis de sentimientos añade un valor adicional al proporcionar una comprensión más profunda de las reseñas de los usuarios. Este proyecto demuestra la importancia de la limpieza de datos y la ingeniería de características en el desarrollo de soluciones de aprendizaje automático para problemas empresariales.
Esta fundamentación destaca la relevancia y el valor del proyecto MLOps para Steam al abordar desafíos reales relacionados con datos poco estructurados y proporcionar recomendaciones de calidad para los usuarios de la plataforma.
En  tal sentido tuve que poner en funcionamiento APIs utilizando el framework Flask que servirían como un medio para exponer y proporcionar acceso a datos específicos de la empresa a través de solicitudes HTTP. A continuación, se explica cada una de estas APIs en detalle:</p>

+ def **PlayTimeGenre( *`genero` : str* )**:
    Debe devolver `año` con mas horas jugadas para dicho género.
  
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}
<p align="justify">La función PlayTimeGenre te ayuda a descubrir cuál fue el año en el que se jugaron más horas en juegos de un género en particular. Por ejemplo, si estás interesado en saber cuál fue el año con más horas jugadas en juegos de acción, puedes usar esta función para obtener la respuesta.
Para usar esta función, simplemente proporciona el nombre del género de juego que te interesa como un texto o una palabra clave (por ejemplo, "action" o "aventure"). La función buscará en sus datos y te dará el año en el que se registraron la mayoría de las horas de juego para ese género específico.</p>

+ def **UserForGenre( *`genero` : str* )**:
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf,
			     "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
	
<p align="justify">La función UserForGenre tiene dos funciones principales. En primer lugar, te ayudará a encontrar el usuario que ha acumulado la mayor cantidad de horas jugadas en juegos del género que especifiques. En segundo lugar, te proporcionará una lista de la acumulación de horas jugadas por año para ese género de juego en particular.
Para usar esta función, simplemente proporciona el nombre del género de juego que te interesa como un texto o una palabra clave (por ejemplo, "action" o "aventure"). La función buscará en sus datos y te dará el nombre de usuario que ha jugado más en ese género y una lista que muestra cuántas horas se jugaron en ese género por año.</p>


+ def **UsersRecommend( *`año` : int* )**:
   Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
  
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

<p align="justify">La función UsersRecommend busca y devuelve una lista de los tres juegos más recomendados por los usuarios para un año en particular. Se basa en las recomendaciones de los usuarios y en comentarios que son positivos o neutrales para determinar cuáles son los juegos más populares y apreciados durante ese año.
Para utilizar esta función, simplemente proporciona el año que te interesa como un número entero. La función buscará en sus datos y te dará una lista de los tres juegos más recomendados por los usuarios durante ese año específico.</p>



+ def **UsersNotRecommend( *`año` : int* )**:
   Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
  
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

<p align="justify">La función UsersNotRecommend busca y devuelve una lista de los tres juegos menos recomendados por los usuarios para un año en particular. Se basa en las recomendaciones de los usuarios y en comentarios que son negativos para determinar cuáles son los juegos menos populares y menos apreciados durante ese año.
Para utilizar esta función, simplemente proporciona el año que te interesa como un número entero. La función buscará en sus datos y te dará una lista de los tres juegos menos recomendados por los usuarios durante ese año específico.</p>


+ def **sentiment_analysis( *`año` : int* )**:
    Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento. 

Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}

<p align="justify">La función sentiment_analysis busca y devuelve una lista que muestra la cantidad de registros de reseñas de usuarios categorizados con diferentes análisis de sentimiento para un año específico de lanzamiento de juegos.</p>
<p align="justify">Para utilizar esta función, simplemente proporciona el año de lanzamiento de juegos que te interesa como un número entero. La función buscará en sus datos y te dará una lista que muestra cuántas reseñas de usuarios se han categorizado con análisis de sentimiento positivo, negativo y neutral para ese año específico.</p>


﻿# <p align="center">**`Modelo de aprendizaje automático`**: </p>

Sistema de recomendación item-item:
+ def **recomendacion_juego( *`id de producto`* )**:
    Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.
Sistema de Recomendación Item-Item:

<p align="justify">El sistema de recomendación item-item se basa en la idea de que los juegos que son similares en términos de contenido son más propensos a ser apreciados por la misma persona. Para implementar este sistema, se utilizan técnicas de procesamiento de texto y análisis de contenido.
Para calcular la similitud entre juegos, se utiliza TfidfVectorizer. Esta técnica convierte las reseñas de los juegos en vectores numéricos, donde cada término en el vector representa una palabra y su peso (TF-IDF) en el contexto de la reseña. Esto permite representar las características del contenido de cada juego de manera numérica.
Por último, se utiliza linear_kernel para calcular la similitud de coseno entre los vectores TF-IDF de los juegos. El resultado es una matriz de similitud que muestra cuán similares son los juegos entre sí en función de su contenido. El coseno de los ángulos entre los vectores se utiliza como medida de similitud, donde un valor más cercano a 1 indica una mayor similitud.</p>
	
<p align="justify">Recomendación de Juegos: Cuando un usuario proporciona el item_id, el sistema busca juegos similares en la matriz de similitud. Esto se logra encontrando las filas de la matriz que corresponden al juego de entrada y seleccionando los juegos más similares. Los 5 juegos con la similitud de coseno más alta se recomiendan al usuario, del mismo modo se puede acceder al gráfico interactivo de recomendaciones por similitud, en el archivo recommendation_plot.html, este archivo es temporal y se genera cada vez que se realiza una consulta en el sistema de recomendaciones, a continuación captura de imágenes sobre el funcionamiento del sistema:</p>
<p align="center">
<img src=https://github.com/carlosab2021/SteamVideos/assets/86332466/88fbeb44-18c7-46e7-ad23-2a2a69308917></p>
<p align="center">
<img src=https://github.com/carlosab2021/SteamVideos/assets/86332466/4fa4291a-4390-4c98-be3b-43a5219e7472></p>




Sistema de recomendación user-item:
+ def **recomendacion_usuario( *`id de usuario`* )**:
    Ingresando el id de un usuario, deberíamos recibir una lista con 5 juegos recomendados para dicho usuario.

Sistema de Recomendación User-Item:
<p align="justify">El sistema de recomendación user-item se centra en el comportamiento del usuario. Se basa en la idea de que los juegos que han sido apreciados o jugados por usuarios con gustos similares a un usuario en particular serán recomendados a ese usuario.</p>
En este caso, no se utiliza TfidfVectorizer para procesar el contenido de los juegos. En su lugar, se utilizan las interacciones de los usuarios con los juegos. Cada usuario tiene una representación de sus interacciones, que pueden incluir calificaciones, reseñas, tiempo de juego, etc., en forma de vectores.</p>
Al igual que en el sistema item-item, se utiliza linear_kernel y la similitud de coseno para calcular la similitud entre los usuarios. Esto se hace comparando los vectores de interacción de los usuarios.
Recomendación de Juegos para un Usuario: Cuando un usuario proporciona su user_id, el sistema calcula la similitud del usuario con otros usuarios. Luego, se identifican los juegos preferidos por usuarios similares y se recomiendan al usuario en función de esas preferencias compartidas. Los 5 juegos que los usuarios similares han apreciado se recomiendan al usuario, del mismo modo se puede acceder al gráfico interactivo de recomendaciones por similitud, en el archivo recommendation_plot.html, este archivo es temporal y se genera cada vez que se realiza una consulta en el sistema de recomendaciones, a continuación captura de imágenes sobre el funcionamiento del sistema:</p>
<p align="center">
<img src=https://github.com/carlosab2021/SteamVideos/assets/86332466/0cb7f412-ef62-407a-a792-b1dc112d3bd5></p>
<p align="center">
<img src=https://github.com/carlosab2021/SteamVideos/assets/86332466/1f712fc9-cf76-492f-afed-d874bd9843e4></p>


<p align="justify">En ambos sistemas, la similitud de coseno es fundamental para determinar las similitudes entre juegos o usuarios. Esto permite recomendar juegos en función de similitudes de contenido o de comportamiento del usuario, respectivamente. Las recomendaciones se generan considerando las similitudes más altas y seleccionando los 5 juegos más similares en cada caso, con la finalidad de renderizar estas app y debido a una memoria limitada de la página de Render, decidí utilizar una muestra de la base de datos consistente en aproximadamente 550 usuarios, cabe alarar que el sistema funciona en forma óptima si realizo las pruebas en el localhost, con la base de datos en su totalidad</p>

﻿### <p align="center">BASE DE DATOS</p>
<p align="justify">Los archivos csv utilizado para las APIs, luego de la limpieza, transformaciones, recortes y uniones de datos son (base_de_datos_con_sentimiento.csv y base_de_datos_muestra.csv), se agrega tambien  al Repositorio de GitHub, los archivos sentiments.ipynb y base.ipynb, en estos archivos se observa el proceso de ETL con variados códigos de prueba y que posteriormente se fueron puliendo para lograr la extraccion de los archivos finales para la utilizacón y puesta en funcionamiento de las APP.
Los notebooks sentiments.ipynb y base.ipynb son esenciales para documentar el proceso de ETL. Contienen códigos de prueba, transformaciones, limpieza de datos y otros pasos que se han realizado para llegar a los archivos base_de_datos_con_sentimiento.csv y base_de_datos_muestra.csv.</p>

﻿# <p align="center">EDA</p>
<p align="justify">Diagrama de dispersión entre dos variables numéricas
Relacion muy dispareja entre las variables "playtime_forever" y "metascore"
La justificación de que hay una relación muy dispareja entre las variables "playtime_forever" y "metascore" se basa en la observación de un diagrama de dispersión entre estas dos variables. En este caso, se supone que "playtime_forever" representa la cantidad de tiempo de juego de un juego y "metascore" representa la puntuación otorgada por Metacritic a ese juego. Veamos cómo se puede llegar a esta conclusión:</p>

<p align="justify">Distribución de los Puntos: Después de crear el diagrama de dispersión con "playtime_forever" en el eje X y "metascore" en el eje Y, se observa que los puntos están dispersos de manera irregular a lo largo del gráfico. Esto significa que no hay una tendencia clara de agrupación de puntos en una dirección específica.</p>

<p align="justify">Ausencia de Correlación Lineal: La dispersión aleatoria de puntos sugiere que no existe una correlación lineal significativa entre estas dos variables. En otras palabras, no se puede trazar una línea recta que represente una relación lineal entre la cantidad de tiempo de juego y la puntuación de Metacritic.

<p align="justify">Puntuaciones Metacríticas Variables para Juegos con Diferentes Tiempos de Juego: Se observa que juegos con una amplia gama de tiempos de juego tienen puntuaciones de Metacritic variadas. Algunos juegos con bajos tiempos de juego tienen altas puntuaciones, mientras que otros con altos tiempos de juego tienen puntuaciones bajas. Esto indica que la puntuación de Metacritic no está directamente relacionada con la cantidad de tiempo de juego.</p>

<p align="justify">Puntos Atípicos: Es posible que en el diagrama de dispersión se observen puntos atípicos, es decir, juegos que se alejan significativamente de la tendencia general. Estos puntos atípicos refuerzan la idea de que no hay una relación clara entre las dos variables.</p>

<p align="justify">En resumen, la forma en que los puntos se distribuyen en el diagrama de dispersión, la falta de una tendencia clara y la variabilidad en las puntuaciones de Metacritic para juegos con diferentes tiempos de juego indican que no hay una relación sólida y predecible entre "playtime_forever" y "metascore". Esto justifica la afirmación de que la relación entre estas dos variables es muy dispareja y que no se puede establecer una conexión lineal clara entre ellas en base a los datos observados.</p>

![image](https://github.com/carlosab2021/cabaez_labs/assets/86332466/6080c2de-8181-4e48-8ac4-e7450c868140)

Identificación de Outliers
# Diagramas de caja (box plots) para variables numéricas
![image](https://github.com/carlosab2021/cabaez_labs/assets/86332466/49ced886-2712-4bd6-bd50-c9bcd7378458)
![image](https://github.com/carlosab2021/cabaez_labs/assets/86332466/a320f9e1-eafe-4086-81a7-682830227ebb)

links Render: [https://steamvideojuegos.onrender.com/ Video: https://youtu.be/DFdkYL8TqII
