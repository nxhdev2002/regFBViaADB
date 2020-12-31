import subprocess
import os
import time
class ADB():
    def __init__(self):
        super(ADB, self).__init__()

    def check_screen_status(self):
        command = 'adb shell dumpsys deviceidle | grep mScreenOn'
        if (subprocess.check_output(command).decode().replace("\r\n", '').split('=')[1] == 'false'):
            self.currentScreenStatus = 0
        else:
            self.currentScreenStatus = 1

    def turn_on_screen(self):
        self.check_screen_status()
        print(self.currentScreenStatus)
        if (self.currentScreenStatus == 0):
            print("screen turning on")
            os.system('adb shell input keyevent 26')
            time.sleep(3)
            os.system('adb shell input touchscreen swipe 930 1000 930 380 && adb shell input text 021202')

    def switch_air_plane_mode(self, mode):
        self.turn_on_screen()
        self.getStatus()
        if (self.currentAirPlaneStatus == 1 and mode == 0):
            position = {'x': '976', 'y': '1258'}
            command = f'adb shell "input keyevent KEYCODE_WAKEUP;input keyevent KEYCODE_MOVE_HOME;am start -a android.settings.AIRPLANE_MODE_SETTINGS;sleep 0.5;input tap {position["x"]} {position["y"]}'
            os.system(command)
        elif (self.currentAirPlaneStatus == 0 and mode == 1):
            position = {'x': '976', 'y': '1258'}
            command = f'adb shell "input keyevent KEYCODE_WAKEUP;input keyevent KEYCODE_MOVE_HOME;am start -a android.settings.AIRPLANE_MODE_SETTINGS;sleep 0.5;input tap {position["x"]} {position["y"]}'
            os.system(command)

    def tap(self, x, y):
        x = str(x)
        y = str(y)
        os.system("adb shell input tap {} {}".format(x,y))
        time.sleep(2)

    def type(self, text):
        os.system(f"adb shell input text " + text)

    def press(self, x, y):
        os.system(f"adb shell input press {x} {y}")
    def swipe(self, x, y, x1, y1, duration):
        os.system(f"adb shell input swipe {x} {y} {x1} {y1} {duration}")

    def install_apk(self, filename):
        os.system("adb install {}".format(filename))
    
    def start_app(self, packagename):
        os.system(f"adb shell monkey -p {packagename} -c android.intent.category.LAUNCHER 1")
        time.sleep(1)
        self.tap(988, 2280)
        time.sleep(1)
        self.tap(894, 1435)
        self.tap(900, 1445)
        time.sleep(3)

    def getStatus(self):
        command = f'adb shell getprop persist.radio.airplane_mode_on'
        self.currentAirPlaneStatus = int(subprocess.check_output(command).decode().replace("\r\n", ''))
        