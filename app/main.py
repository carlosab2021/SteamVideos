from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Carga la base de datos desde el archivo CSV
data = pd.read_csv('resultado_union_actualizado.csv')

# Ruta para obtener el año con más horas jugadas para un género dado
@app.route('/PlayTimeGenre/<genero>', methods=['GET'])
def playtime_genre(genero):
    genero = genero.strip('[]').strip("'")  # Elimina los corchetes para obtener el género real
    # Verifica si la cadena proporcionada tiene al menos 4 caracteres 
    if len(genero) < 4:
        return jsonify({"message": "La búsqueda debe contener al menos 4 caracteres."}, 400)
    filtered_data = data[data['genres'] .str.contains(genero, case=False, na=False)]

    if filtered_data.empty:
        return jsonify({"message": "No se encontraron datos para el género especificado."}, 404)

    max_horas = filtered_data['playtime_forever'].max()
    año_max_horas = filtered_data[filtered_data['playtime_forever'] == max_horas]['release_date'].values[0]
    

    return jsonify({"Año de lanzamiento con más horas jugadas para " + genero: año_max_horas})

# if __name__ == '__main__':
    # app.run(debug=True)

