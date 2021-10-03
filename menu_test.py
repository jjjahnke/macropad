import unittest

from menu import  *

class TestMenuItem(unittest.TestCase):
    
    def test_MenuItem(self):
        mi = MenuItem("test")
        self.assertAlmostEqual(mi.getName(), "test")
        self.assertAlmostEqual(mi.pressed, False)
        self.assertAlmostEqual(mi.active, False)

    def test_getName(self):
        mi = MenuItem("test")
        self.assertAlmostEqual(mi.getName(), "test")
        mi = MenuItem()
        self.assertAlmostEqual(mi.getName(),None)

    def test_rotate(self):
        mi = MenuItem("test")
        self.assertAlmostEqual(mi.rotate(1),None)

    def test_pressDown(self):
        mi = MenuItem("test")
        mi.pressDown()
        self.assertAlmostEqual(mi.pressed, True)

    def test_pressUp(self):
        mi = MenuItem("test")
        mi.pressUp()
        self.assertAlmostEqual(mi.pressed, False)
        self.assertAlmostEqual(mi.active, True)
        mi.pressDown()
        mi.pressUp()
        self.assertAlmostEqual(mi.pressed, False)
        self.assertAlmostEqual(mi.active, False)
        
    def test_reset(self):
        mi = MenuItem("test")
        mi.pressUp()
        self.assertAlmostEqual(mi.active, True)
        mi.resetActive()
        self.assertAlmostEqual(mi.active, False)

class TestKeyPressToggleMenuItem(unittest.TestCase):
    
    def test_KeyPressToggleMenuItem(self):
        kpt = KeyPressToggleMenuItem("test")
        self.assertAlmostEqual(kpt.getName(), "Key Mode: Momentary")
        self.assertAlmostEqual(kpt.Toggle, False)

    def test_rotate(self):
        kpt = KeyPressToggleMenuItem("test")
        kpt.rotate(1)
        self.assertAlmostEqual(kpt.getToggle(), False)
        kpt.pressUp()
        kpt.rotate(1)
        self.assertAlmostEqual(kpt.getToggle(), True)
        kpt.rotate(1)
        self.assertAlmostEqual(kpt.getToggle(), False)
        kpt.rotate(2)
        self.assertAlmostEqual(kpt.getToggle(), False)
        kpt.rotate(3)
        self.assertAlmostEqual(kpt.getToggle(), True)
        kpt.rotate(-4)
        self.assertAlmostEqual(kpt.getToggle(), True)
        kpt.rotate(-5)
        self.assertAlmostEqual(kpt.getToggle(), False)
        kpt.pressUp()
        self.assertAlmostEqual(kpt.getToggle(), False)
    
    def test_rotation(self):
        kpt = KeyPressToggleMenuItem("test")
        self.assertAlmostEqual(kpt.getName(), "Key Mode: Momentary")
        kpt.pressUp()
        kpt.rotate(-1)
        self.assertAlmostEqual(kpt.getName(), "Key Mode: Toggle")
        
class TestBrightnessMenuItem(unittest.TestCase):

    def test_BrightnessMenuItem(self):
        bmi = BrightnessMenuItem("test")
        self.assertAlmostEqual(bmi.getBrightness(), 1)

    def test_getName(self):
        bmi = BrightnessMenuItem("test")
        self.assertAlmostEqual(bmi.getName(), "Brightness Level: 1")

    def test_rotate(self):
        bmi = BrightnessMenuItem("test")
        bmi.pressUp()
        bmi.rotate(-1)
        self.assertAlmostEqual(bmi.getBrightness(), 0.99)
        self.assertAlmostEqual(bmi.getName(), "Brightness Level: 0.99")
        bmi.rotate(100)
        self.assertAlmostEqual(bmi.getBrightness(), 1)
        self.assertAlmostEqual(bmi.getName(), "Brightness Level: 1")
        bmi.rotate(-200)
        self.assertAlmostEqual(bmi.getBrightness(), 0)
        self.assertAlmostEqual(bmi.getName(), "Brightness Level: 0")
        