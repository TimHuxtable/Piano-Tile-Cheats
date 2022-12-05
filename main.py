import pyautogui
import time
import keyboard

# import win32api, win32con

print(pyautogui.size())
im = pyautogui.screenshot()

print("Starting in 3...2...1...")
time.sleep(3)

pixel_coordinates = [(1000, 400), (1180, 400), (1370, 400), (1600, 400)]

color_to_click = (0, 0, 0)


def click(x, y):
    pyautogui.moveTo((x, y))
    pyautogui.mouseDown()
    time.sleep(0.01)
    pyautogui.mouseUp()


while not keyboard.is_pressed('q'):
    # We need to put * in front of pixel_coordinates so that it unpacks the tuple to be used as args.
    if pyautogui.pixel(*pixel_coordinates[0])[0] == 0:
        click(*pixel_coordinates[0])
    if pyautogui.pixel(*pixel_coordinates[1])[0] == 0:
        click(*pixel_coordinates[1])
    if pyautogui.pixel(*pixel_coordinates[2])[0] == 0:
        click(*pixel_coordinates[2])
    if pyautogui.pixel(*pixel_coordinates[3])[0] == 0:
        click(*pixel_coordinates[3])

#
# def main():
#     while not keyboard.is_pressed('q'):
#         for pixels in pixel_coordinates:
#             px = im.getpixel(pixels)
#             time.sleep(0.1)
#             print(px)
#             if px == color_to_click:
#                 pyautogui.moveTo(*pixels)
#                 pyautogui.click()
#             if pyautogui.pixel
#             else:
#                 continue
#         main()
#
#
# main()
