# Full Stack Chess Application (React, Python, Flask)

## Overview
This is a full-stack chess application built using React for the frontend, Node.js/Express for the backend API, and Python with Flask for the chess engine logic. The app allows users to play chess in a browser, providing move validation and AI-driven move suggestions for black using the minimax algorithm.

### Tech Stack
- **Frontend**: React
- **Backend**: Node.js (Express) and Python (Flask)
- **AI Engine**: Python (Minimax Algorithm for Chess AI)
- **Styling**: CSS
- **API Communication**: Axios and Flask-CORS
- **Board Representation**: A 2D array representing an 8x8 chessboard

## Features
- Interactive chessboard where users can play as white.
- Move validation and legal move generation for white pieces.
- AI-driven black piece moves using the minimax algorithm.
- Communication between frontend and backend using REST API.
- Fetching available moves from the backend in real-time for selected pieces.

## Project Structure

```bash
.
├── frontend/
│   ├── src/
│   │   ├── App.js         # Main React application component for the chessboard
│   │   ├── App.css        # Styling for the chessboard and pieces
├── api/
│   ├── index.js           # Express.js server to handle API requests
├── backend/
│   ├── server.py          # Flask server to handle chess logic and AI moves
│   ├── engine.py          # GameState class for move generation logic
│   ├── computer.py        # ChessAI class implementing the minimax algorithm for AI moves
```

## Getting Started

### Prerequisites
- **Node.js**: Ensure you have Node.js and npm installed.
- **Python**: Python 3.x is required for running the backend.
- **Flask**: Install Flask and Flask-CORS for the Python backend.

### Installation Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/chess-app.git
    cd chess-app
    ```

2. **Frontend Setup** (React):
    - Navigate to the `frontend/` directory.
    ```bash
    cd frontend
    npm install
    npm start
    ```
    - The React app will be served on `http://localhost:3000`.

3. **Backend Setup** (Node.js and Python):
    - Navigate to the `api/` directory for the Node.js backend.
    ```bash
    cd api
    npm install
    node index.js
    ```
    - This will start the API server at `http://localhost:4000`.

4. **Python Backend Setup**:
    - Install the required Python dependencies in the `backend/` directory.
    ```bash
    cd backend
    pip install Flask Flask-CORS
    python server.py
    ```
    - The Flask server will run on `http://localhost:5000`.

### Running the Application
1. Start the React frontend.
2. Start the Express backend.
3. Start the Flask chess engine.

The application should now be available at `http://localhost:3000`.

## API Endpoints

### Node.js Backend (Express)
1. **POST /api/coordinates**: 
   - Fetches available moves for a selected piece from the Python backend.
   - **Request Body**: 
     ```json
     {
       "board": [...],
       "coordinates": { "x": 0, "y": 0 }
     }
     ```

2. **POST /api/board**: 
   - Sends the updated board to the backend and retrieves the AI move.
   - **Request Body**: 
     ```json
     [ ... ]  # 8x8 array representing the chessboard
     ```

### Python Backend (Flask)
1. **POST /api/getAvailableMoves**:
   - Returns legal moves for a selected piece based on the board state.

2. **POST /api/sendBoard**:
   - Calculates the best move for black using the minimax algorithm.

## Frontend Explanation (React)
- The `App.js` file manages the chessboard's state and user interactions.
- The chessboard is rendered using an 8x8 grid of `div` elements, with each square representing a tile.
- Clicking on a white piece fetches available moves from the Flask backend, and clicking again makes the move.
- Chess pieces are displayed as images based on the board's state.

### Key Functions
- **`handleSquareClick(row, col)`**: Manages user interactions with the chessboard and determines valid moves.
- **`renderGrid()`**: Renders the chessboard grid dynamically based on the current game state.

## Python Chess Engine
- **`engine.py`**: Implements chess logic for move validation and generation based on piece type.
- **`computer.py`**: Implements the ChessAI class using the minimax algorithm to determine black's best move.

## AI Logic
- The ChessAI class uses a minimax algorithm to evaluate the board state and generate the best move for the black pieces.
- The algorithm considers multiple depths and applies evaluation functions to prioritize moves.

## Future Improvements
- Add multiplayer capabilities.
- Improve AI performance with advanced techniques (e.g., Alpha-Beta pruning).
- Implement castling, en passant, and promotion rules.

## Conclusion
This chess application is a simple yet powerful implementation of a chess game with AI-driven moves for the black player. By combining React for the frontend and Flask for backend logic, it provides an interactive and intelligent chess-playing experience.