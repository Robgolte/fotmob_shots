from flask import Flask, request, jsonify
import LanusStats as ls
import os

app = Flask(__name__)
fotmob = ls.FotMob()

@app.route('/shotmap', methods=['GET'])
def get_shotmap():
    # Obtener el parámetro playerId de la URL
    player_id = request.args.get('playerId')

    # Si no se pasa el playerId, devolver un error 400
    if not player_id:
        return jsonify({'error': 'Falta el parámetro playerId'}), 400

    try:
        # Aquí llamamos a la función get_player_shotmap de LanusStats con los parámetros correctos
        # El primer y segundo parámetro parece ser constante, mientras que el tercer parámetro es el player_id recibido
        data = fotmob.get_player_shotmap("1", "0", player_id)
        
        # Verificar si se obtuvo una respuesta válida
        if data:
            return jsonify(data)
        else:
            return jsonify({'error': 'No se encontraron datos para el jugador con ID: ' + player_id}), 404
    except Exception as e:
        # En caso de error, devolver un mensaje con el error
        return jsonify({'error': 'Error al obtener los datos: ' + str(e)}), 500

if __name__ == '__main__':
    # Usar el puerto asignado por Render (si está disponible), o 5000 como fallback
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
