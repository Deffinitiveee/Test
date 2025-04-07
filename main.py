from flask import Flask, jsonify
from flask_cors import CORS
import a2s

app = Flask(__name__)
CORS(app)  # <- Esta línea habilita CORS

# Dirección del servidor CS
SERVER_ADDRESS = ("45.235.98.30", 27787)

@app.route("/server-info")
def server_info():
    try:
        info = a2s.info(SERVER_ADDRESS, timeout=5.0)
        players = a2s.players(SERVER_ADDRESS, timeout=5.0)

        return jsonify({
            "nombre_servidor": info.server_name,
            "mapa": info.map_name,
            "jugadores_conectados": f"{info.player_count}/{info.max_players}",
            "jugadores": [player.name for player in players]
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
