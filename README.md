# Raspberry Pi Zero 2 W

## Part 1: Install Raspberry Pi OS on Windows (Headless)
**1. Download, install, and run "Raspberry Pi Imager"**
https://www.raspberrypi.com/software/

**2. Choose OS: Raspberry Pi OS (32 bit)**

**3. Choose Storage: select SD card**

**4. Advanced Option: Set hostname, Enable SSH, Set Username and Password, Configure Wireless LAN, Set local settings, then save!**

**5. Write!**

**6. Put SD card inside the SD card socket on Raspberry Pi Zero 2 W**

**7. Connect it to computer through USB socket (If not installed, Download and install Bonjour Print Services from apple.com)**

**8. Open MobaXterm or Putty and use SSH with hostname = raspberrypi.local and port=22**

**9. Enter username and password**

**10. Check the OS**
   ```sh
   uname -a
   lsb_release -a
   ```
## Part 2: Enabling and Connecting over VNC

**1. Enable VNC**
   ```sh
   sudo raspi-config
   ```
   * Select "Interfacing Options", then "VNC"and enable it

**2. Download, install and launch VNC Viewer**
 https://www.realvnc.com/en/connect/download/viewer/windows/
 
 **3. create a new connection: Enter "raspberrypi.local" in VNC Server section**
 
 **4. Enter Username and Password**
 * QUICK-NOTE: if you see  "cannot currently show the desktop" on VNC viewer, then change the resolution

## Part 3: Changing the WIFI network, if it has changed (Headless)
* Create file "wpa_supplicant.conf", write the following lines there, and put the file in the boot folder in SD card. https://github.com/Jafarshamsi/Raspberry/tree/main/First_Boot
   ```sh
   country=US
   ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
   update_config=1

   network={
   scan_ssid=1
   ssid="your_wifi_ssid"
   psk="your_wifi_password"
   }
   ```

## Part 4: Connecting Raspberry Cam
**1. Connect to PI over VNC Viwer**

**2. USING Raspicam library: Enable raspberry pi camera from raspi-cofing**
   * open raspbery config
   ```sh
   sudo raspi-config
   ```
   * Interface Options/ Enable Camera
   * QUICK-NOTE: it was possible to enable it from Raspberry Pi Configuration inside the OS, however, it seems that it is removed from there

   * Take Picture: go to desktop
   ```sh
   raspistill -o 1.jpg
   ```
   * Capture video: go to desktop
   ```sh
   raspivid -t 5000 -p 0,0,640,480 -vf
   ```
   * QUICK-NOTE: More information here: https://www.raspberrypi.com/documentation/accessories/camera.html#raspicam-commands

**2. USING libcamera library (Not working now): Disable Raspicam library from raspi-cofing**
   * QUICK-NOTE: More information here: https://www.raspberrypi.com/documentation/accessories/camera.html#libcamera-and-libcamera-apps

## Part 4: QR Code generator https://segno.readthedocs.io/en/stable/index.html
   ```sh
   pip install segno
   segno "Hello World!"
   ```
## Part 5: QR Code reader https://pypi.org/project/pyzbar/
   * install packages
   ```sh
   sudo apt-get update
   sudo apt-get install python3-opencv libzbar0 python3-pip
   python3 -m pip install pyzbar
   ```
   * check python and Thonny Python IDE (Programming/Thonny Python IDE)
   ```sh
   python
   print("Hello World!")
   exit()
   ```
   * Run qrCodeReader.py https://github.com/Jafarshamsi/Raspberry/tree/main/QR_reader

## Part 6: C++ CrossCompile (VisualGDB is an alternative)
   * Install the toolchain (The GCC compiler for C and C++ languages) from https://gnutoolchains.com/raspberry/ 
   * Create a helloworld.cpp
   ```sh
   #include <stdio.h>
   int main()
   {
       printf("Hello, world\n");
       return 0;
   }
   ```
   * Compile the code through powershell 
   ```sh
   <toolchain>\bin\arm-linux-gnueabihf-g++.exe -ggdb helloworld.cpp -o helloworld
   ```
   * Copy the generated file (helloworld) into a folder in rasparay pi and run it
   ```sh
   chmod a+x helloworld
   ./helloworld
   ```
## Part 7: [UART](https://github.com/raspberrypi/documentation/blob/develop/documentation/asciidoc/computers/configuration/uart.adoc)
   * PINs: 
   * Functionality: There are 2 UARTs: PL011 (UART0) + mini UART(UART1)
   * Kernel: There are 2 UARTs: Primary UART(serial0) + Secondary UART(serial1)
   
   * modify cofing.txt and disable bluetooth
   ```sh
   sudo nano /boot/config.txt
   dtoverlay = disable-bt
   core_freq=250
   enable_uart=1
   force_turbo=1
   ```
   * modify disable bluetooth services and reboot
   ```sh
   sudo systemctl disable hciuart.service
   sudo systemctl disable bluealsa.service
   sudo systemctl disable bluetooth.service
   sudo reboot
   ```
   * disable consule UART
   ```sh
   sudo nano /boot/cmdline.txt
   dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles
   ``` 
   * check the seiral ports
   ```sh
   ls -l /dev/serial*
   ``` 


   * install minicom to test (connect tx(pin8) to rx(pin10) and write something)
   ```sh
   sudo apt-get install minicom
   minicom -b 9600 -o -D /dev/ttyS0
   pkill minicom
   ``` 
## Part 8: startup
   *  modify rc.local and a line to run your code
   ```sh
   sudo nano /home/pi/.bashrc
   python /home/pi/Desktop/QR_UART.py &
   ``` 
## Reference
[1] https://www.raspberrypi.com/documentation/computers/os.html 
[2] https://www.raspberrypi.com/documentation/accessories/camera.html
[3] https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html
[4] https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/hello-world#
[5] https://peppe8o.com/read-qr-codes-from-raspberry-pi-with-pyzbar-and-python/
