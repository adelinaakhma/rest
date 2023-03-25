#!/usr/bin/env python
# coding: utf-8

# In[29]:


board = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
def drawBoard(board):
    for i in range(3):
        print (board[0+i*3], "|", board[1+i*3], "|", board[2+i*3])
        print ("—— ——— ———")
drawBoard(board)


# In[37]:


def takeInput(playerToken):
    valid = False
    while not valid:
        playerAnswer = input("Куда поставим " + playerToken+ " ?  ")
        if not isValidInput(playerAnswer):
            continue
        playerAnswer = int(playerAnswer)
        if (playerAnswer >= 1 and playerAnswer <=9):
            if(str(board[playerAnswer-1]) not in "XO"):
                board[playerAnswer-1] = playerToken
                valid = True
            else:
                print("Эта клетка занята!!!")
        else:
            print("Некорретный ввод. Введите число от 1 до 9")
def isValidInput(playerAnswer):
    try:
        playerAnswer = int (playerAnswer)
        return True
    except:
        print("Некорретный ввод. Число вводи")
        return False 
takeInput("X")
drawBoard(board)
takeInput("O")
drawBoard(board)


# In[ ]:


def checkin(board):
    winCoords = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8))
    for coord in winCoords:
        if board[coord[0]] == board[coord[1]] == board[coord[2]]:
            return board[coord[0]]
    return False    
tmpBoard = ["X","X","X",4,5,6,7,8,9]
checkWin(tmpBoard)
tmpBoard = ["X","O","X",4,5,6,7,8,9]
checkWin(tmpBoard)

