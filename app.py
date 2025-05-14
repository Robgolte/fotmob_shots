from flask import Flask, request, jsonify
import LanusStats as ls
import os

app = Flask(__name__)
fotmob = ls.FotMob()

@app.route('/shotmap', methods=['GET'])
def get_shotmap():
    player_id = request.args.get('playerId')
    if not player_id:
        return jsonify({'error': 'Falta el parámetro playerId'}), 400

    try:
        data = fotmob.get_player_shotmap("1", "0", player_id)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Usar el puerto asignado por Render (si está disponible), o 5000 como fallback
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
