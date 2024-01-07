import pyautogui, time

next = "right"
before = "left"
pyautogui.PAUSE = 0.1


def setup2(): # Setup to close reading windows and prepare typing window
    pyautogui.hotkey("ctrl", "w")
    pyautogui.moveTo(273, 200)
    pyautogui.leftClick()


def RType(Table): #type a line to the right
    time.sleep(0.1)

    for i in range(9):
        pyautogui.press(str(Table[i]))
        pyautogui.press(next)
    pyautogui.press(before)
    pyautogui.press("down")


def LType(Table): # type a line to the left
    time.sleep(0.1)
    for i in range(8, -1, -1):
        pyautogui.press(str(Table[i]))
        pyautogui.press(before)
    pyautogui.press(next)
    pyautogui.press("down")


def Write(Table):
    num = 0

    for i in range(4):
        RType(Table[num])
        num += 1
        LType(Table[num])
        num += 1

    RType(Table[-1])