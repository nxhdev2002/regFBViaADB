
import os
import re
import time
import random
import requests
import subprocess
from selenium import webdriver

def get_arb_value(dic):
    try:
        return next(iter(dic.values()))
    except StopIteration:
        pass


class infomationHandle():
    def __init__(self):
        super(infomationHandle, self).__init__()
    
    def getRandName(self):
        r = requests.get("https://www.fakeaddressgenerator.com/All_countries/address/country/Vietnam")
        reg = r"value='(.*?)'\/>"
        return re.findall(reg, r.text)[0].replace("&nbsp;", ' ').split(" ")

    def getEmailAdress(self):
        return requests.get("https://mailtamthoi.net/api/create?key=ezgwapqKHy8eJqKUEDQOyPJ5akxFVU").text


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
            os.system('adb shell input keyevent 26 && adb shell input touchscreen swipe 930 880 930 380 && adb shell input text 021202')

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

    def getStatus(self):
        command = f'adb shell getprop persist.radio.airplane_mode_on'
        self.currentAirPlaneStatus = int(subprocess.check_output(command).decode().replace("\r\n", ''))
        
# class fbAuto():
#     def __init__(self):
#         super(fbAuto, self).__init__()
#         self.driver = webdriver.Chrome()



#     def enterhomepage(self):
#         self.driver.get("https://www.facebook.com/")
#         self.driver.find_element_by_xpath('//*[@id="u_0_2"]').click()

#     def fill2From(self):
#         time.sleep(2)
#         self.driver.find_element_by_name("lastname").send_keys(self.name[0])
#         self.driver.find_element_by_name("firstname").send_keys(self.name[1])
#         self.driver.find_element_by_name("reg_email__").send_keys("xopiho6580@5y5u.com")
#         self.driver.find_element_by_name("reg_email_confirmation__").send_keys("xopiho6580@5y5u.com")
#         self.driver.find_element_by_xpath("//input[contains(@name, 'sex') and @value='1']").click()
#         ####

#         # Select birthday_D
#         self.driver.find_element_by_xpath('//*[@id="day"]/option[2]').click()

#         # Select birthday_M
#         self.driver.find_element_by_xpath('//*[@id="month"]/option[2]').click()

#         # Select birthday Y
#         self.driver.find_element_by_xpath('//*[@id="year"]/option[contains(@value, "1990")]').click()

#         ####

#         self.driver.find_element_by_name("reg_passwd__").send_keys("Hacker001")
#         self.driver.find_element_by_name("websubmit").click()

#     def regAcc(self):
#         self.getRandName()
#         self.enterhomepage()
#         self.getEmailAdress()
#         self.fill2From()

class fbADB():
    def __init__(self):
        super(fbADB, self).__init__()

    def tap(self, x, y):
        x = str(x)
        y = str(y)
        os.system("adb shell input tap {} {}".format(x,y))
    
    def type(self, text):
        os.system(f"adb shell input text " + text)

    def press(self, x, y):
        os.system(f"adb shell input press {x} {y}")
    def swipe(self, x, y, x1, y1, duration):
        os.system(f"adb shell input swipe {x} {y} {x1} {y1} {duration}")

    def install_apk(self):
        os.system("adb install lite3.apk")
    
    def start_app(self):
        os.system("adb shell monkey -p com.facebook.litg -c android.intent.category.LAUNCHER 1")
        time.sleep(1)
        self.tap(988, 2280)
        time.sleep(1)
        self.tap(894, 1435)
        self.tap(900, 1445)
        time.sleep(3)

    def reg(self):

        self.tap(882, 1183)
        self.tap(579, 974)
        time.sleep(3)
        self.tap(472, 1100)

        time.sleep(3)
        ## Enter Family name
        self.tap(342, 536)
        self.type("Xuan\ Tun")

        time.sleep(1)
        ## Enter Name
        self.tap(869, 548)
        self.tap(869, 548)
        self.type("Nguyen")

        ##
        time.sleep(2)
        self.tap(492, 717)
        self.tap(492, 717)
        time.sleep(1)
        self.tap(573, 1973)

        print(">> FILLING MAIL")

        #### FILL EMAIL
        time.sleep(3)
        ## Del old mail
        self.tap(589, 585)
        self.swipe(572, 583, 73, 598, 600)
        os.system("adb shell input keyevent 67")

        #
        mail = infomationHandle().getEmailAdress()
        print(mail)
        self.type(mail)

        self.tap(748, 713)
        self.tap(748, 713)
        
        print(">> FILLING BIRTHDAY")
        #### FILL BIRTH DAY
        time.sleep(3)
        ## Birthday_D
        self.tap(84, 566)
        self.tap(84, 566)
        self.tap(171, 1588)     # 1
        ## Birthday_M
        self.tap(135, 574)      
        self.tap(171, 1588)     # 1
        ## Birthday_Y
        self.tap(229, 574)
        self.tap(171, 1588)  # 1
        self.tap(982, 1805)  # 9
        self.tap(982, 1805)  # 9
        self.tap(536, 1958)  # 0

        self.tap(330, 693)

        print(">> FILLING SEX")
        self.tap(1001, 533)
        self.tap(368, 549)
        os.system('pause')

        print(">> FILLING PASS")
        ### FILL PASS
        self.tap(368, 549)
        self.tap(368, 549)
        self.type("Hacker001")
        
        self.tap(251, 930)

        #### WAIT BRO ^_^

        self.tap(847, 1938)
        
        time.sleep(3)

        self.tap(158, 657)
        self.getPIN(mail)

    def getPIN(self, mail):
        r = requests.get(f"https://mailtamthoi.net/api/fetch?email={mail}&key=ezgwapqKHy8eJqKUEDQOyPJ5akxFVU").json()
        print(r)
        if(r['length'] > 0):
            regex = r"https:\/\/www.facebook.com\/n\/(.*?)<"
            test_str = get_arb_value(r)['text']
            matches = re.findall(regex, test_str)
            print(matches[0])
            return ("https://www.facebook.com/n/" + matches[0])
        else:
            time.sleep(5)
            self.getPIN(mail)

    def delete_apk(self):
        os.system("adb shell pm uninstall -k --user 0 com.facebook.litg")
# adb = ADB()
# fbAuto = fbAuto()
# fbAuto.regAcc()
# adb.switch_air_plane_mode(0)
# os.system('pause')

adbfb = fbADB()
adbfb.install_apk()
adbfb.start_app()
adbfb.reg()


adbfb.delete_apk()