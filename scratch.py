import pyautogui
import time
import keyboard


# print(pyautogui.size())

print("Starting in 3...2...1...")
time.sleep(3)

pixel_coordinates = [(1000, 400), (1180, 400), (1370, 400), (1600, 400)]

color_to_click = (0, 0, 0)


# def click(x, y):
#     pyautogui.moveTo((x, y))
#     pyautogui.mouseDown()
#     time.sleep(0.01)
#     pyautogui.mouseUp()
#
#
# while not keyboard.is_pressed('z'):
#     # We need to put * in front of pixel_coordinates so that it unpacks the tuple to be used as args.
#     if pyautogui.pixel(*pixel_coordinates[0])[0] == 0:
#         click(*pixel_coordinates[0])
#     if pyautogui.pixel(*pixel_coordinates[1])[0] == 0:
#         click(*pixel_coordinates[1])
#     if pyautogui.pixel(*pixel_coordinates[2])[0] == 0:
#         click(*pixel_coordinates[2])
#     if pyautogui.pixel(*pixel_coordinates[3])[0] == 0:
#         click(*pixel_coordinates[3])


def main():
    while not keyboard.is_pressed('z'):
        for pixels in pixel_coordinates:
            start_time = time.time()
            im = pyautogui.screenshot()
            px = im.getpixel(pixels)
            time.sleep(0.01)
            print(px)
            if px == color_to_click:
                pyautogui.moveTo(*pixels)
                print("My program took ", time.time() - start_time, "to run")
                pyautogui.mouseDown()
                time.sleep(0.01)
                pyautogui.mouseUp()
        main()


main()
