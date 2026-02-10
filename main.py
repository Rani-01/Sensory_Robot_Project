#Import all necessary libraries
import machine
from machine import Pin, I2C
import time
from buzzer import Buzzer
from stepper import Stepper
from hcsr04 import HCSR04
from oled import I2C as OLED_I2C
from mpu6050 import accel

# Initialization
i2c_bus = I2C(-1, sda=Pin(21), scl=Pin(22))

# Initialize OLED
display = OLED_I2C(128, 64, i2c_bus)

# Initialize Accelerometer
mpu = accel(i2c_bus)

led = Pin(12, Pin.OUT)
button = Pin(27, Pin.IN, Pin.PULL_UP)
my_buzzer = Buzzer(15)
Ultrasonic_Sensor = HCSR04(trigger_pin=5, echo_pin=18)

stepper_left = Stepper(13)
stepper_right = Stepper(19)

# Functions
def get_steps_from_distance(distance_cm):
    # The stepper motors have 200 steps per full revolution (360°).
    # Circumference C = 2*3.14*3(Radius in cm) = 18.849 cm
    # Steps per cm = 200/18.849 = 10.6106424744 ~ 10.61 steps
    steps_per_cm = 10.61
    return int(distance_cm * steps_per_cm)

def update_screen(dist, tilt_y):
    """Update the OLED with sensor data"""
    display.clear()
    display.text("Robot Status", 0, 0)
    display.text("Dist: {} cm".format(dist), 0, 2)
    display.text("Tilt Y: {}".format(tilt_y), 0, 4)
    display.show()

def wait_button_press():
    print("Waiting for button...")
    display.clear()
    display.text("Press Button", 0, 2)
    display.show()
    while button.value() == 1:
        time.sleep(0.01)
    return True

while True:
    #Start the process
    #Resetting the LED to low
    led.value(0)
    #Clear OLED Screen and display text
    display.clear()
    display.text("Press button to start", 0, 2)
    #Waiting for button to be pressed
    wait_button_press()
    #Turning on LED
    led.value(1)
    #Beeping the buzzer once
    my_buzzer.beep_once()
    #Getting distance measured by Ultrasonic sensor 
    dist = Ultrasonic_Sensor.distance_cm()
    print("distance: ", dist)
    #Display distance on OLED Screen
    display.clear()
    display.text("Distance: {} cm".format(dist), 0, 2)
    display.show()
    #calculating required steps
    required_steps = get_steps_from_distance(dist)
    print("required_steps: ", required_steps)
    #Setting the Flag
    reached = True
    for i in range(required_steps):
            stepper_left.move_one_step()
            stepper_right.move_one_step()
            #Getting the tilt value of Y -axis and check if the robot is tilted or not
            accel_data = mpu.get_values()
            tilt_y = accel_data["AcY"]
            #If Tilted the reached flag is set to false and breaking the loop
            if tilt_y>12000 or tilt_y<-12000:
                reached = False
                break
            
    # Checking if Robot reached the destination or tilted
    if reached:
        display.clear()
        display.text("REACHED", 0, 2)
        display.show()
        print("REACHED")
        my_buzzer.beep_once()
    else:
        led.value(1)
        display.clear()
        display.text("TILTED", 0, 2)
        print("TILTED")
        display.show()
        my_buzzer.beep_once()
        my_buzzer.beep_once()
        my_buzzer.beep_once()
    time.sleep(3)

