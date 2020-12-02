import os
import random
from selenium import webdriver


class ADB():
    def __init__(self):
        super(ADB, self).__init__()
    
    def switch_air_plane_mode(self):
        position = {'x': '976', 'y': '1258'}
        command = f'adb shell "input keyevent KEYCODE_WAKEUP;input keyevent KEYCODE_MOVE_HOME;am start -a android.settings.AIRPLANE_MODE_SETTINGS;sleep 0.5;input tap {position["x"]} {position["y"]}'
        os.system(command)


class fbAuto():
    def __init__(self):
        super(fbAuto, self).__init__()
        self.driver = webdriver.Chrome()

    
    def enterhomepage(self):
        self.driver.get("https://mbasic.facebook.com/r.php?locale=vi_VN&display=page&soft=hjk")

    def fill2From(self):
        self.enterhomepage()
        self.driver.find_element_by_name("lastname").send_keys("1")
        self.driver.find_element_by_name("firstname").send_keys("2")
        self.driver.find_element_by_name("reg_email__").send_keys("#")
        self.driver.find_element_by_xpath("//*[@id='sex' and @value='1']").click()
        ####

        # Select birthday_D
        self.driver.find_element_by_xpath('//*[@id="day"]/option[2]').click()

        # Select birthday_M
        self.driver.find_element_by_xpath('//*[@id="month"]/option[2]').click()

        # Select birthday Y
        self.driver.find_element_by_xpath('//*[@id="year"]/option[27]').click()

        ####

        self.driver.find_element_by_name("reg_passwd__").send_keys("Hacker001")
        self.driver.find_element_by_id("signup_button")

fbAuto = fbAuto()
fbAuto.fill2From()


os.system('pause')
# adb = ADB()
# adb.switch_air_plane_mode()

