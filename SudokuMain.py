import pyautogui, time, keyboard, concurrent.futures
from Sudoku import BackTrack
from SudokuReader import setup, ReadLine
from TypeSudoku import Write, setup2

pyautogui.PAUSE = 0.2 # The Delay between inputs
SafetyHotkey = "n" #Choose your stopping key
Safety = True

def SafetyLock():  #Stops the program if the safety key is running
    while True:
        if keyboard.is_pressed(SafetyHotkey):
            return False




def Simas():
    x = time.time()
    pyautogui.moveTo(811, 392)  # Very Hard Difficulty Button
    pyautogui.scroll(1500) # Sudoku.kingdom tends to roll up everytime you refresh it
    time.sleep(1)
    pyautogui.leftClick()
    time.sleep(1)
    setup() # Sets up the board to be read, and places cursor in the first tile to start reading
    Table = ReadLine() #Reads all lines and put them into a 2d Matrix
    SolvedSudoku = BackTrack(Table) #Solves the Sudoku using a BackTracking approach
    setup2() #Prepares the cursor for the writing function
    Write(SolvedSudoku) # Writes the answers in the website
    print(time.time() - x)

future = concurrent.futures.ThreadPoolExecutor.submit(Safety) #
Halt = future.result()
#Safety program runs on a different thread, to not be affected by the main thread


if __name__ == "__main__":
    while not Halt: # while the safety thread doesn't detect input, keep running
        Simas()

