"""importación de librerias"""

import pygame
import numpy as np
import random


"""paleta colores, para cada numero"""
BG_COLORS = {
    0: (250, 250, 250),
    2: (33, 150, 136),
    4: (0, 255, 255),
    8: (255, 0, 255),
    16: (0, 128, 128),
    32: (247, 124, 95),
    64: (0, 255, 0),
    128: (128, 0, 128),
    256: (237, 204, 98),
    512: (255, 0, 0),
    1024: (255, 255, 255),
    2048: (237, 194, 46)
}
"""colores
[2:blanco, 4:azul, 8:fucsia, 16:azul, 32:naranja  64:verde, 128:violeta, 256:amarillo, 512:rojo, 1024:blanco, 2048:amarillO]
"""


"""clase juego"""

class Juego:
    
    """dimensiones juego"""
    
    
    def __init__(self) -> None:
        self.N = 5
        self.cellSize = 150
        self.gap = 4
        self.windowBgColor = (0, 0, 0)
        self.blockSize = self.cellSize + self.gap * 2
        self.windowWidth = self.blockSize * 4
        self.windowHeight = self.windowWidth

        """inicializacion de modulos"""

        pygame.init()


        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))

        """tamaño de los numeros"""
        
        self.myFont = pygame.font.SysFont("2048 python", 50)
        
        pygame.display.set_caption("2048 python")

        self.boardStatus = np.zeros((self.N, self.N))
        self.addNewNumber()

    
    def addNewNumber(self):
        freePos = zip(*np.where(self.boardStatus == 0))
        freePos = list(freePos)

        for pos in random.sample(freePos, k=1):
            self.boardStatus[pos] = 2

    def drawBoard(self):
        self.window.fill(self.windowBgColor)

        for r in range(self.N):
            rectY = self.blockSize * r + self.gap
            for c in range(self.N):
                rectX = self.blockSize * c + self.gap
                cellValue = int(self.boardStatus[r][c])

                pygame.draw.rect(
                    self.window,
                    BG_COLORS[cellValue],
                    pygame.Rect(rectX, rectY, self.cellSize, self.cellSize)
                )

                if cellValue != 0:
                    textSurface = self.myFont.render(f"{cellValue}", True, (0, 0, 0))
                    textRect = textSurface.get_rect(center=(rectX + self.blockSize/2, rectY + self.blockSize/2))
                    self.window.blit(textSurface, textRect)

    def compressNumber(self, data):
        result = [0]
        data = [x for x in data if x != 0]
        for element in data:
            if element == result[len(result) - 1]:
                result[len(result) - 1] *= 2
                result.append(0)
            else:
                result.append(element)
        
        result = [x for x in result if x != 0]
        return result

    def move(self, dir):
        for idx in range(self.N):

            if dir in "UD":
                data = self.boardStatus[:, idx]
            else:
                data = self.boardStatus[idx, :]

            flip = False
            if dir in "RD":
                flip = True
                data = data[::-1]

            data = self.compressNumber(data)
            data = data + (self.N - len(data)) * [0]

            if flip:
                data = data[::-1]

            if dir in "UD":
                self.boardStatus[:, idx] = data
            else:
                self.boardStatus[idx, :] = data
                

    """derrota"""

    def GameOver(self):
        boardStatusBackup = self.boardStatus.copy()
        for juego in "UDLR":
            self.move(juego)

            if (self.boardStatus == boardStatusBackup).all() == False:
                self.boardStatus = boardStatusBackup
                return False
        return True

        


    def play(self):
        running = True
        while running:
            self.drawBoard()
            pygame.display.update()

            for event in pygame.event.get():
                oldBoardStatus = self.boardStatus.copy()

                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.move("U")
                    elif event.key == pygame.K_DOWN:
                        self.move("D")
                    elif event.key == pygame.K_LEFT:
                        self.move("L")
                    elif event.key == pygame.K_RIGHT:
                        self.move("R")
                    elif event.key == pygame.K_ESCAPE:
                        running = False

                    if self.GameOver():
                        print("perdiste !!")
                        return
                 
                    if (self.boardStatus == oldBoardStatus).all() == False:
                        self.addNewNumber()

if __name__ == "__main__":
    game = Juego()
    game.play()

    """victoria"""

    def win (self):
        boardStatusBackup = self.boardStatus.copy()
        for juego in "UDLR":
            self.move(juego)

            if (self.boardStatus == boardStatusBackup).all() == true:
                self.boardStatus = boardStatusBackup
                return true
            return false
    

    """mensaje sobre game over"""

    from tkinter import *
    from tkinter import messagebox
    messagebox.showinfo(message="Perdiste", title="Lo siento")



"""fin"""
