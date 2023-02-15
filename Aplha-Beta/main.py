import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax
import time

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

MOVETIMES = []
EXPANSIONSPERMOVE = []

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            st = time.time()
            value, new_board, expansions= minimax(game.get_board(), 4, WHITE, game, float('-inf'), float('inf'))
            game.ai_move(new_board)
            et = time.time()
            print("Decision time: ", et-st)
            print("Expansions: ", expansions)
            MOVETIMES.append(et-st)
            EXPANSIONSPERMOVE.append(expansions)

        if game.winner() != None:
            if(game.winner() == RED):
                print("Red Wins!")
            elif(game.winner() == WHITE):
                print("White Wins!")
            else:
                print("Stalemate - draw")
            print("Average move time with pruning: ", sum(MOVETIMES)/len(MOVETIMES))
            print("Average expansions per move: ", sum(EXPANSIONSPERMOVE)/len(EXPANSIONSPERMOVE))
            print("Total expansions: ", sum(EXPANSIONSPERMOVE))
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

main()
