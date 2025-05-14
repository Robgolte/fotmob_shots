from flask import Flask, request, jsonify
import LanusStats as ls
import os
import pandas as pd

app = Flask(__name__)
fotmob = ls.FotMob()

@app.route('/shotmap', methods=['GET'])
def get_shotmap():
    player_id = request.args.get('playerId')
    if not player_id:
        return jsonify({'error': 'Falta el parámetro playerId'}), 400

    try:
        # Obtener los datos del jugador
        data = fotmob.get_player_shotmap("1", "0", player_id)

        # Verificar si 'data' es un DataFrame, y convertirlo a un formato serializable
        if isinstance(data, pd.DataFrame):
            data = data.to_dict(orient='records')  # Convertir el DataFrame a una lista de diccionarios

        return jsonify(data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Usar el puerto asignado por defecto (5000)
    app.run(host='0.0.0.0', port=5000, debug=True)
