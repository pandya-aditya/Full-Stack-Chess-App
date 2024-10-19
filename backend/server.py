from flask import Flask, jsonify, request
from engine import gameState
from computer import ChessAI
from flask_cors import CORS
import requests
import time

game = gameState()
computer = ChessAI()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route("/api")
def get_moves(coordinates, board):
    send_to = {}
    send_to["available_moves"] = game.get_moves(coordinates, board)
    return send_to

@app.route('/api/getAvailableMoves', methods=['POST'])
def post_api_data():
    data = request.json
    coord = data['coordinates']
    board = data['board']
    return get_moves(coord, board)

@app.route('/api/sendBoard', methods=['POST'])    
def move_black():
    board = request.json
    return computer.best_move(board, 3)

if __name__ == "__main__":
    app.run(debug=True)