#this needs to be able to press keys and click the mouse

import pyautogui

mapsToGenerate = 50

#wait 3 seconds
pyautogui.sleep(3)

print("Go")

for i in range(mapsToGenerate):

    worldX = 0 + i * 128
    
    #teleport to the next location
    pyautogui.press('/')
    pyautogui.typewrite('tp @p ' + str(worldX) + ' ~ 0')
    pyautogui.press('enter')

    pyautogui.sleep(1)

    #give the player a map
    pyautogui.press('/')
    pyautogui.typewrite('give @p map')
    pyautogui.press('enter')

    pyautogui.sleep(1)

    #open the map by switching to first slot, right clicking, then switching to second slot
    pyautogui.press('1')
    pyautogui.rightClick()
    pyautogui.press('2')

    pyautogui.sleep(1)

    #clear the players inventory
    pyautogui.press('/')
    pyautogui.typewrite('clear @p')
    pyautogui.press('enter')

    pass