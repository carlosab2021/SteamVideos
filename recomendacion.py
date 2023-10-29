from flask import Flask, request, render_template, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__, template_folder=".")
app.config['JSON_AS_ASCII'] = False

# Cargar la base de datos desde el archivo CSV
data = pd.read_csv('resultado_union_actualizado.csv')
data2 = pd.read_csv('base_de_datos_con_sentimiento.csv')

# Cargar datos de juegos (reemplaza 'games.csv' con tu archivo de datos)
games_data = pd.read_csv('resultado_union_actualizado.csv') 

# Preprocesamiento de datos para el sistema de recomendación item-item
games_data['app_name'].fillna('', inplace=True)
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(games_data['app_name'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Función para obtener juegos recomendados basados en un juego dado
def get_recommendations(game_id, cosine_sim=cosine_sim):
    game_index = games_data[games_data['item_id'] == game_id].index[0]
    sim_scores = list(enumerate(cosine_sim[game_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Excluye el juego en sí (índice 0) y toma los 5 más similares
    game_indices = [i[0] for i in sim_scores]
    return games_data['title'].iloc[game_indices].tolist()

# ... Código de las rutas existentes ...

# Ruta para obtener recomendación de juegos similares
@app.route('/recomendacion_juego/<int:game_id>', methods=['GET'])
def recomendacion_juego(game_id):
    recommended_games = get_recommendations(game_id)
    return jsonify({"recommended_games": recommended_games})

if __name__ == '__main__':
    app.run(debug=True)
r