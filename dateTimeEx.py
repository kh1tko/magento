import pyautogui
from PIL import Image

# Move the mouse to coordinates (x=100, y=100)
pyautogui.moveTo(100, 100)

# Click the left mouse button
pyautogui.click()

# Double-click the mouse button
pyautogui.doubleClick()

# Right-click the mouse
pyautogui.rightClick()

# Move the mouse relative to its currrent position
pyautogui.moveRel(50, 0)

# Scroll the mouse up
pyautogui.scroll(10)

# Press the 'a' key
pyautogui.press('a')

# Type the string 'hello'
pyautogui.typewrite('hello')

# Press the 'enter' key
pyautogui.press('enter')

# Take a screenshot of the entire screen
screenshot = pyautogui.screenshot()

# Save the screenshot to a file
screenshot.save('scr.png')

# Take a screenshot of a region of the screen
region = (100, 100, 300, 300)  # Left, top width, height

screenshot2 = pyautogui.screenshot(region=region)

screenshot2.save('scr2.png')
