from pyautogui import *
import pyperclip, pyautogui, time

InitialX = 238 # Adapts this to the X position of the first Tile
InitialY = 255 # Adapt this to the Y position of the first tile
Increment = 43 # Difference between each tile X position
Table = [] # Holds the read values from the sudoku board
pyautogui.PAUSE = 0.0075 #delay between simulated keyboard inputs
                         #The Higher, The More Consistent


def setup(): #Sets Up Cursor and Screen to Be Read
    pyautogui.moveTo(144, 329)  # Print
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.moveTo(223, 248)  # First Print Tile
    pyautogui.leftClick()


def GetLine(Y): # Copies the entire line and appends it to the Table
    global Table
    MyLine = []
    Increment = 45
    for i in range(9):
        moveTo(InitialX + Increment * (i), Y)
        leftClick()
        pyperclip.copy(0)
        hotkey("ctrl", "a")
        hotkey("ctrl", "c")
        content = pyperclip.paste()
        MyLine.append(int(content))

    Table.append(MyLine)


def ReadLine(): #Move Cursor Across Lines
    global Table
    for i in range(9):
        GetLine(InitialY + Increment * i)
    moveTo(InitialX, InitialY)
    return Table