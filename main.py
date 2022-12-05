import pyautogui
import time
import keyboard


# print(pyautogui.size())

print("Starting in 3...2...1...")
time.sleep(3)

pixel_coordinates = [(1000, 400), (1180, 400), (1370, 400), (1600, 400)]

color_to_click = (0, 0, 0)


def click(x, y):
    pyautogui.moveTo((x, y))
    pyautogui.mouseDown()
    time.sleep(0.01)
    pyautogui.mouseUp()


while not keyboard.is_pressed('z'):
    # We need to put * in front of pixel_coordinates so that it unpacks the tuple to be used as args.
    start_time = time.time()

    if pyautogui.pixel(*pixel_coordinates[0])[0] == 0:
        click(*pixel_coordinates[0])
        print("My program took ", time.time() - start_time, "to run")

    if pyautogui.pixel(*pixel_coordinates[1])[0] == 0:
        click(*pixel_coordinates[1])
        print("My program took ", time.time() - start_time, "to run")

    if pyautogui.pixel(*pixel_coordinates[2])[0] == 0:
        click(*pixel_coordinates[2])
        print("My program took ", time.time() - start_time, "to run")

    if pyautogui.pixel(*pixel_coordinates[3])[0] == 0:
        click(*pixel_coordinates[3])
        print("My program took ", time.time() - start_time, "to run")


