# Chess

## Introduction 

Implementing Chess, the board game

## Design

### Classes

From a client perspective, at the minimum we want two human players able to play a game of chess, moving pieces in a 
'legal' fashion, from a beginning to end position.

This will involve the following

- Chess
    - Move (Kxe4)
        - Piece
        - x1, y1
        - x2, y2
        - Piece captured (optional)
    
    - abstract Pieces
        - Pawn, Knight, Bishop, Rook, Queen, King
    - Game Manager
        - One singleton board
            - 2D Array representation of pieces
        - legal move getter from Piece on board (Piece, at xy)
            - player's turn (white/black flag)
            - per-Piece legal moves (from xy)
                - Pieces:
                    - Cannot capture same-colored pieces
                    - Pawn: 
                        - forward (0 if occupied, two else if first move, else one )
                        - diagonal (if occupied, or empassant)
                            - empassant previous move, adjacent pawn moved two forward
                    - Knight:
                        - two forwards, one side
                    - Bishop: 
                        - diagonal (0-7, until occupied)
                    - Rook (castle): 
                        - horizontal/vertical
                        - First move can be castle
                    - Queen:
                        - (0-7 horizontal/vertical)
                    - King (castle):
                        - horizontal/vertical
                        - First move can be castle (two moves left/right, Rook swap)
                        - cannot be in check

## Workflow

0. Instantiate Game
    - Instantiate Board
        - Instantiate Pieces
1. 