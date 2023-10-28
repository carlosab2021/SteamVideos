from flask import Flask, request, render_template, jsonify
import pandas as pd

app = Flask(__name__, template_folder=".")
app.config['JSON_AS_ASCII'] = False

# Carga la base de datos desde el archivo CSV
data = pd.read_csv('resultado_union_actualizado.csv')
data2 = pd.read_csv('base_de_datos_con_sentimiento.csv')
@app.route('/')
def select_app():
    return render_template('aplicaciones.html')
# Ruta para recibir datos del formulario y ejecutar la aplicación correspondiente
@app.route('/launch_app', methods=['POST'])
def launch_app():
    selected_app = request.form['selected_app']
    input_data = request.form['input_data']
    result = {}

    if selected_app == 'UserForGenre':
        result = user_for_genre(input_data)
    elif selected_app == 'UsersRecommend':
        result = users_recommend(int(input_data))
    elif selected_app == 'UsersNotRecommend':
        result = users_not_recommend(int(input_data))
    elif selected_app == 'sentiment_analysis':
        result = sentiment_analysis(int(input_data))
    elif selected_app == 'PlayTimeGenre':
        result = playtime_genre(input_data)
    else:
        result = {"message": "Aplicación no válida."}

    # Construir un diccionario con el resultado
    response_data = {"result": result}

    # Devolver el diccionario serializado como JSON
    return response_data




# Ruta para obtener el año con más horas jugadas para un género dado
@app.route('/PlayTimeGenre/<genero>', methods=['GET'])
def playtime_genre(genero):
    genero = genero.strip('[]').strip("'")  # Elimina los corchetes para obtener el género real
    # Verifica si la cadena proporcionada tiene al menos 4 caracteres 
    if len(genero) < 4:
        return {"message": "La búsqueda debe contener al menos 4 caracteres."}, 400
    filtered_data = data[data['genres'] .str.contains(genero, case=False, na=False)]

    if filtered_data.empty:
        return {"message": "No se encontraron datos para el género especificado."}, 404

    max_horas = filtered_data['playtime_forever'].max()
    año_max_horas = filtered_data[filtered_data['playtime_forever'] == max_horas]['release_date'].values[0]
    

    return {"Año de lanzamiento con más horas jugadas para " + genero: año_max_horas}


# Ruta para obtener el usuario con más horas jugadas y la acumulación por año para un género dado
@app.route('/UserForGenre/<genero>', methods=['GET'])
def user_for_genre(genero):
    genero = genero.strip('[]').strip("'")  # Elimina los corchetes para obtener el género real
    filtered_data = data[data['genres'].str.contains(genero, case=False, na=False)]

    if filtered_data.empty:
        return {"message": "No se encontraron datos para el género especificado."}, 404

    # Encuentra el usuario con más horas jugadas para el género
    max_horas_usuario = filtered_data[filtered_data['playtime_forever'] == filtered_data['playtime_forever'].max()]['user_id'].values[0]

    # Obtén el año a partir de una cadena de fecha (ejemplo: "2022-05-15")
    filtered_data['Año'] = filtered_data['fecha_convertida'].str.split('-').str[0]
    
    # Convierte la columna 'Año' a tipo numérico (entero)
    filtered_data['Año'] = filtered_data['Año'].astype(int)

    # Agrupa por 'Año' y calcula la suma de 'playtime_forever'
    acumulacion_por_año = filtered_data.groupby('Año')['playtime_forever'].sum().reset_index()

    # Convierte el resultado a un diccionario en el formato requerido
    resultado = {
        "Usuario con más horas jugadas para " + genero: max_horas_usuario,
        "Horas jugadas": acumulacion_por_año.to_dict(orient='records')
    }

    return resultado


# Ruta para obtener el top 3 de juegos MÁS recomendados por usuarios para un año dado
@app.route('/UsersRecommend/<int:ano>', methods=['GET'])
def users_recommend(ano):
    # Filtrar los datos para el año especificado
    filtered_data = data[data['fecha_convertida'].str.contains(str(ano))]

    if filtered_data.empty:
        return {"message": "No se encontraron datos para el año especificado."}, 404

    # Filtrar solo los juegos con recomendaciones positivas o neutrales (recommend = True)
    positive_reviews = filtered_data[filtered_data['recommend'] == True]

    # Contar la cantidad de recomendaciones por juego
    game_recommend_counts = positive_reviews['item_id'].value_counts().reset_index()
    game_recommend_counts.columns = ['item_id', 'Recommend_Count']

    # Ordenar los juegos por cantidad de recomendaciones en orden descendente
    top_games = game_recommend_counts.sort_values(by='Recommend_Count', ascending=False).head(3)

    # Obtener los títulos de los juegos
    game_titles = data[['item_id', 'title']].drop_duplicates()
    top_games = pd.merge(top_games, game_titles, on='item_id')

    # Formatear el resultado en el formato requerido
    resultado = [{"Puesto " + str(i + 1): juego['title']} for i, juego in top_games.iterrows()]

    return resultado


# Ruta para obtener el top 3 de juegos MENOS recomendados por usuarios para un año dado
@app.route('/UsersNotRecommend/<int:ano>', methods=['GET'])
def users_not_recommend(ano):
    # Filtrar los datos para el año especificado
    filtered_data = data[data['fecha_convertida'].str.contains(str(ano))]

    if filtered_data.empty:
        return {"message": "No se encontraron datos para el año especificado."}, 404

    # Filtrar solo los juegos con recomendaciones negativas y comentarios negativos
    negative_reviews = filtered_data[(filtered_data['recommend'] == False)]

    # Contar la cantidad de juegos menos recomendados
    game_not_recommend_counts = negative_reviews['item_id'].value_counts().reset_index()
    game_not_recommend_counts.columns = ['item_id', 'NotRecommend_Count']

    # Ordenar los juegos por cantidad de juegos menos recomendados en orden descendente
    top_not_recommend_games = game_not_recommend_counts.sort_values(by='NotRecommend_Count', ascending=False).head(3)

    # Obtener los títulos de los juegos
    game_titles = data[['item_id', 'title']].drop_duplicates()
    top_not_recommend_games = pd.merge(top_not_recommend_games, game_titles, on='item_id')

    # Formatear el resultado en el formato requerido
    resultado = [{"Puesto " + str(i + 1): juego['title']} for i, juego in top_not_recommend_games.iterrows()]

    return resultado


# Ruta para obtener el análisis de sentimiento según el año de lanzamiento
@app.route('/sentiment_analysis/<int:ano>', methods=['GET'])
def sentiment_analysis(ano):
    # Filtra los datos para el año especificado
    filtered_data2 = data2[data2['fecha_convertida'].str.contains(str(ano))]

    if filtered_data2.empty:
        return {"message": "No se encontraron datos para el año especificado."}, 404

    # Realiza el recuento de análisis de sentimiento
    sentiment_counts = filtered_data2['sentiment'].value_counts()

    # Convierte el resultado a un diccionario
    result = sentiment_counts.to_dict()

    return result

if __name__ == '__main__':
    app.run (debug=True)

