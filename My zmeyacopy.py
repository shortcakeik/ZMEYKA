import time
import os
import random
import numpy as np
import colorama
import curses

#w = curses.initscr()

snake = np.zeros((16, 16))
apple = []
ap = 0
MLSnake = 2
snake[3][2] = 2
snake[3][3] = 1
def rnd():
    f = int(random.randint(0, 15))
    return f
def printScreen():
    for x in range(16):
        print('                            ', end=' ')
        #w.addstr('                             ')
        for y in range(16):

            if x == apple[0] and y == apple[1]:
                print('A', end='   ')
                #w.refresh()
            elif snake[x][y] == max:
                print('O', end='   ')
            elif snake[x][y]:
                print('o', end='   ')
            else:
                print(' ', end='   ')
        print('\n')

    time.sleep(0.1)
    #w.clear()
    #w.refresh()
    #print('\033[2J\033[1;1f')
    os.system('CLS')

while MLSnake:
    f = 0
    if ap == 0:
        apple = [rnd(), rnd()]
        ap = 1
    printScreen()
    while ap:
        maxlen = 0
        for i in range(16):
            for j in range(16):
                if snake[i,j] > maxlen:
                    x = i
                    y = j
                    maxlen = snake[i,j]

        if apple[0] == x and apple[1] == y:
            MLSnake = MLSnake + 1
            ap = 0
            for i in range(16):
                for j in range(16):
                    if snake[i,j] != 0:
                        snake[i,j] = snake[i,j] + 1

            snake[x1,y1] = 1
            apple = 'o'
            printScreen()
            break

        for i in range(16):
            for j in range(16):
                if snake[i,j] == 1:
                    x1 = i
                    y1 = j


        if x > apple[0]:
            for i in range(16):
                for j in range(16):
                    if snake[i,j] != 0:
                        snake[i,j] = snake[i,j] - 1
            if snake[x - 1][y] == 0 and x - 1 >= 0:
                snake[x - 1][y] = MLSnake
                printScreen()
                break
            elif snake[x][y - 1] == 0 and y - 1 >= 0:
                snake[x][y - 1] = MLSnake
                printScreen()
                break
            elif snake[x][y + 1] == 0 and y + 1 <= 16:
                snake[x][y + 1] = MLSnake
                printScreen()
                break
            elif snake[x + 1][y] == 0 and x + 1 <= 16:
                snake[x + 1][y] = MLSnake
                printScreen()
                break

        if x < apple[0]:
            for i in range(16):
                for j in range(16):
                    if snake[i,j] != 0:
                        snake[i,j] = snake[i,j] - 1
            if snake[x + 1,y] == 0 and x + 1 <= 16:
                snake[x + 1, y] = MLSnake
                printScreen()
                break
            elif snake[x][y - 1] == 0 and y - 1 >= 0:
                snake[x][y - 1] = MLSnake
                printScreen()
                break
            elif snake[x][y + 1] == 0 and y + 1 <= 16:
                snake[x][y + 1] = MLSnake
                printScreen()
                break
            elif snake[x - 1][y] == 0 and x - 1 >= 0:
                snake[x - 1][y] = MLSnake
                printScreen()
                break

        if y > apple[1]:
            for i in range(16):
                for j in range(16):
                    if snake[i,j] != 0:
                        snake[i,j] = snake[i,j] - 1
            if snake[x, y - 1] == 0 and y - 1 >= 0:
                snake[x, y - 1] = MLSnake
                printScreen()
                break
            elif snake[x + 1][y] == 0 and x + 1 <= 16:
                snake[x + 1][y] = MLSnake
                printScreen()
                break
            elif snake[x - 1][y] == 0 and x - 1 >= 0:
                snake[x - 1][y] = MLSnake
                printScreen()
                break
            elif snake[x][y + 1] == 0 and y + 1 <= 16:
                snake[x][y + 1] = MLSnake
                printScreen()
                break


        if y < apple[1]:
            for i in range(16):
                for j in range(16):
                    if snake[i,j] != 0:
                        snake[i,j] = snake[i,j] - 1
            if snake[x, y + 1] == 0 and y + 1 <= 16:
                snake[x, y + 1] = MLSnake
                printScreen()
                break
            elif snake[x + 1][y] == 0 and x + 1 <= 16:
                snake[x + 1][y] = MLSnake
                printScreen()
                break
            elif snake[x - 1][y] == 0 and x - 1 >= 0:
                snake[x - 1][y] = MLSnake
                printScreen()
                break
            elif snake[x][y - 1] == 0 and y - 1 >= 0:
                snake[x][y - 1] = MLSnake
                printScreen()
                break

    #os.system('CLS')



