"""
Main File, User input
"""

import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8 #size of board 8 squares
SQ_SIZE = HEIGHT // DIMENSION #Square size
MAX_FPS = 12
IMAGES = {}

'''
Initialize global dictionary of images, called once in the main
'''
def loadImages():
    pieces = ['br', 'bn', 'bb', 'bq', 'bk','bp','wp','wr', 'wn', 'wb', 'wq', 'wk']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("chess/images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

'''
The main driver for code
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    sqSelected = () # no square selected initially, keep track of the last click of the user
    playerClciks = [] #keep track of player clicks
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #gets x, y position of mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected = () #When User reClicks the same square it unselects the piece rather than move it there
                    playerClciks = [] #clear player clicks
                else:
                    sqSelected = (row, col)
                    playerClciks.append(sqSelected) #append for both 1st and 2nd clicks
                if len(playerClciks) == 2: #after the second click has happened
                    move = ChessEngine.Move(playerClciks[0],playerClciks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = () #reset user clicks
                    playerClciks = []

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsible for graphics
'''
def drawGameState(screen, gs):
    drawBoard(screen) #draw the squares on the board
    drawPieces(screen, gs.board) # draw pieces on top of the squares

'''
Draws the Squares, Top left must always be white in both perspectives
'''
def drawBoard(screen):
    colors = [p.Color("lemon chiffon"), p.Color(" blue")]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[(( row + col ) % 2 )]
            p.draw.rect(screen, color, p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
Draws the pieces on the board
'''
def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
if __name__ == "__main__":
    main()


