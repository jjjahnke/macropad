class MenuItem:
    def __init__(self, name=None):
        self.name = name
        self.pressed = False
        self.resetActive()

    def getName(self):
        return self.name

    def rotate(self, distance):
        if self.active:
            return self.execute_rotate(distance)
    
    def pressDown(self):
        self.pressed = True

    def pressUp(self):
        self.pressed = False
        self.active = not self.active

    def resetActive(self):
        self.active = False

class KeyPressToggleMenuItem(MenuItem):
    def __init__(self, name):
        MenuItem.__init__(self, "Key Mode")

        self.Toggle = False

    def getName(self):
        tgl = ""
        if self.Toggle == False:
            tgl = "Momentary"
        else:
            tgl = "Toggle"
        return MenuItem.getName(self) + ": " + tgl

    def execute_rotate(self, distance):
        click = distance % 2
        if click == 1:
            self.Toggle = not self.Toggle
   
    def getToggle(self):
        return self.Toggle

class BrightnessMenuItem(MenuItem):
    def __init__(self, name):
        MenuItem.__init__(self,"Brightness Level")

        self.min = 0
        self.max = 1

        self.brightness = 1

    def getName(self):
        return MenuItem.getName(self) + ": " + str(self.brightness)

    def getBrightness(self):
        return self.brightness

    def execute_rotate(self, distance):
        self.brightness = self.brightness + (0.01 * distance)
        if self.brightness > self.max:
            self.brightness = self.max
        if self.brightness < self.min:
            self.brightness = self.min

class TopLevelMenuItem(MenuItem):
    def __init__(self, name):
        MenuItem.__init__(self, name)
