from adb import ADB
import time


class fbAuto():
    def __init__(self, adb):
        super(fbAuto, self).__init__()
        self.adb = adb
        print(">> Starting App")
        self.adb.start_app("com.facebook.katand")
    def createAccount(self, firstname, lastname, gender, user, password):
        print(">> Click Create Acc Button")
        # Click create account button
        self.adb.tap(632, 2234)

        # Click Next
        self.adb.tap(691, 1574)

        # Deny permissions
        self.adb.tap(258, 2213)
        self.adb.tap(258, 2213)

        # Fill Last Name
        self.adb.tap(248, 872)
        print(">> Fill lastname")
        self.adb.type(lastname)

        # Fill First Name

        self.adb.tap(854, 787)
        print(">> Fill firstname")
        self.adb.type(firstname)

        # Click Next
        self.adb.tap(359, 1071)

        print(">> Fill birthday")
        # Fill BirthDay_D
        self.adb.tap(547, 963)
        self.adb.type("1")
        
        # Fill BirthDay_M
        self.adb.tap(380, 860)
        self.adb.type("Jan")

        
        # Fill Birthday_Y
        self.adb.tap(708, 871)
        self.adb.type("1990")

        # Click Next
        self.adb.tap(777, 1337)
        

        # Select Gender
        print(">> Select gender: " + gender)
        if (gender == 0):
            self.adb.tap(197, 964)
        else:
            self.adb.tap(954, 850) 

        # Click Next
        self.adb.tap(747, 1376)


        # Switch to Select Email Address
        self.adb.tap(629, 2326)
        

        # Fill Email
        print(">> Fill Email: " + user)
        self.adb.tap(230, 882)
        self.adb.type(user)

        # Enter
        self.adb.tap(817, 1030)

        # Fill Password
        print(">> Fill Pass: " + password)
        self.adb.tap(403, 901)
        self.adb.type(password)

        # Click Next
        self.adb.tap(346, 1083)

        # Click Signup without upload
        self.adb.tap(737, 1307)

        print(">> Done")
if (__name__ == '__main__'):
    adb = ADB()
    # adb.switch_air_plane_mode(1)
    adb.turn_on_screen()

    fb = fbAuto(adb)
    time.sleep(5)
    fb.createAccount("Nam\ Tran", "Nguyen", 1, "fb3112@noel2020.us", "Hacker001")