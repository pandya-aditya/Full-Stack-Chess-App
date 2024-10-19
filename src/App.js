import './App.css';
import React, { useState, useEffect } from 'react';

function App() {
  const [board, setBoard] = useState([
    ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'], 
    ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
    ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
  ]);

  const [moves, setMoves] = useState([{}]);
  const [click, setClick] = useState(0);
  const gridSize = 8;
  const [firstClickCoords, setFirstClickCoords] = useState(null);

  // Function to handle clicks on squares
  const handleSquareClick = (row, col) => {
    const tileValue = board[row][col];
    const coords = [row, col];

    if (click === 0) {
      // First click logic: select a piece
      if (tileValue && tileValue.startsWith('w')) { // Only select white pieces
        const coordinates = { x: col, y: row };
        const payload = {
          board,
          coordinates,
        };

        // Fetch the available moves for the selected piece
        fetch('http://localhost:4000/api/coordinates', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(payload),
        })
          .then(response => response.json())
          .then(data => {
            setMoves(data); // Update moves with the fetched available moves
            setFirstClickCoords(coords); // Save the coordinates of the first click
            setClick(1); // Update click state to 1 (ready for second click)
          })
          .catch(error => console.error('Error:', error));
      } else {
        console.log('Invalid first click: select a valid piece');
        setClick(0);
      }
    } else if (click === 1) {
      // Second click logic: move the piece if the move is valid
      if (moves.available_moves.some(move => move[0] === coords[0] && move[1] === coords[1])) {
        console.log('Valid move:', coords);

        // Update the board by moving the piece
        const newBoard = board.map(row => [...row]); // Create a copy of the board
        const [firstRow, firstCol] = firstClickCoords; // Destructure first click coordinates
        
        // Move the piece to the new position and set the old position to '--'
        newBoard[coords[0]][coords[1]] = board[firstRow][firstCol]; // Move piece to new coords
        newBoard[firstRow][firstCol] = '--'; // Set old coords to empty
          // Fetch the available moves for the selected piece
        fetch('http://localhost:4000/api/board', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(newBoard),
          })
            .then(response => response.json())
            .then(newBoard => {
              setBoard(newBoard); // Update moves with the fetched available moves
            })
            .catch(error => console.error('Error:', error));
            setBoard(newBoard); // Update the board state
        } 
        else {
          console.log('Invalid first click: select a valid piece');
          setClick(0);
        } 
      } 
      else {
        console.log('Invalid move');
      }

      setClick(0); // Reset clicks after checking the move
      console.log(board);
  };

  useEffect(() => {
    if (click === 1 && moves.available_moves.length > 0) {
      console.log('Moves are available:', moves.available_moves);
    }
  }, [moves]);

  // Function to render the chess grid
  const renderGrid = () => {
    const grid = [];

    for (let row = 0; row < gridSize; row++) {
      const gridRow = [];
      for (let col = 0; col < gridSize; col++) {
        const isLightSquare = (row + col) % 2 === 0;

        gridRow.push(
          <div
            key={`${row}-${col}`}
            className={`grid-square ${isLightSquare ? 'light-square' : 'dark-square'}`}
            onClick={() => handleSquareClick(row, col)}
          >
            {/* Display image based on the piece in the current square */}
            {board[row][col] !== '--' && (
              <img
                src={`/images/${board[row][col]}.png`} // Adjust the path as needed
                alt={board[row][col]}
                className="piece-image"
              />
            )}
          </div>
        );
      }
      grid.push(
        <div key={row} className="grid-row">
          {gridRow}
        </div>
      );
    }
    return grid;
  };

  return (
    <div>
      <div className="grid-container">
        {renderGrid()}
      </div>
    </div>
  );
}

export default App;
