##### Sensor Robot (MicroPython)

###### **📌 Overview**



This project implements an autonomous robot control system using MicroPython on a microcontroller (such as ESP32). The robot measures distance using an ultrasonic sensor, moves using stepper motors, monitors tilt using an accelerometer, and provides real-time feedback via an OLED display, LED, and buzzer.



The modular structure of the code allows for easy reuse and adaptability in future robotics or IoT projects. Each hardware component is abstracted into its own module, making the system easy to understand, extend, and maintain.

###### 

###### ✨ Features



📏 Distance measurement using an HC-SR04 ultrasonic sensor



🛞 Movement control using dual stepper motors



📐 Tilt detection using MPU6050 accelerometer



🖥️ Real-time status display on OLED



🔊 Audio feedback using a buzzer



💡 Visual feedback using an LED



🔘 User interaction via a push button



###### 🗂️ Project Structure





*project/*

*│*

*├── main.py            # Main control logic*

*├── buzzer.py          # Buzzer control module*

*├── stepper.py         # Stepper motor control module*

*├── hcsr04.py          # Ultrasonic sensor module*

*├── oled.py            # OLED display module*

*├── mpu6050.py         # Accelerometer module*

*└── README.md          # Project documentation*





Each module encapsulates hardware-specific logic, allowing the main program to remain clean and readable.



###### ⚙️ Hardware Requirements



*ESP32 (or compatible MicroPython-supported board)*



*HC-SR04 Ultrasonic Sensor*



*MPU6050 Accelerometer*



*OLED Display (I2C, 128×64)*



*2 × Stepper Motors*



*Buzzer*



*Push Button*



*LED*



*Jumper wires and power supply*



###### 🧠 How It Works



The system waits for the button press to start.



Once started:



* The ultrasonic sensor measures distance.
* Distance is converted into stepper motor steps.
* The robot moves forward while continuously checking tilt values.

 	If excessive tilt is detected: Movement stops. The robot signals TILTED using OLED and buzzer.

 	If the robot reaches the destination safely: It displays REACHED and gives a success beep.



###### ▶️ How to Run the Project



1. **Flash MicroPython**



Ensure MicroPython is installed on your ESP32 board.



2\. **Upload Project Files**



Upload main.py and all module files (buzzer.py, stepper.py, etc.) to the board using:



1. *Wokwi*
2. *Thonny IDE*
3. *uPyCraft*
4. *ampy / rshell*



3\. **Connect Hardware**



Wire the components according to the pin definitions used in main.py:



I2C: SDA → GPIO 21, SCL → GPIO 22



Button → GPIO 27



LED → GPIO 12



Buzzer → GPIO 15



Ultrasonic Trigger → GPIO 5



Ultrasonic Echo → GPIO 18



Stepper Motors → GPIO 13 \& GPIO 19



(Adjust pins in code if your wiring differs.)



**4. Run the Program**



Reset the board or run main.py



Press the button to start the robot sequence

###### 

###### 🧩 Code Design \& Modularity



**Reusable Functions:**



get\_steps\_from\_distance() converts distance into motor steps



wait\_button\_press() handles user input



update\_screen() manages OLED updates



**Separation of Concerns:** Each hardware component is isolated into its own module, making it easy to replace or upgrade individual parts without changing the main logic.



