# Raspberry Pi Zero 2 W

## Part 1: Install Raspberry Pi OS on Windows
**1. Download, install, and run "Raspberry Pi Imager"**
https://www.raspberrypi.com/software/
![alt text](https://github.com/Jafarshamsi/Raspberry/IMAGE/1.RPI_OS.png)

**2. Choose OS: Raspberry Pi OS (32 bit)**

**3. Choose Storage: select SD card**

**4. Advanced Option: Set hostname, Enable SSH, Set Username and Password, Configure Wireless LAN, Set local settings, then save!**

**5. Write!**

**6. Put SD card inside the SD card socket on Raspberry Pi Zero 2 W**

**7. Connect it to computer through USB socket (If not installed, Download and install Bonjour Print Services from apple.com)**

**8. Open MobaXterm or Putty and use SSH with hostname = raspberrypi.local and port=22**

**9. Enter username and password**

## Part 2: Enabling and Connecting over VNC**

**1. Enable VNC**
   ```sh
   sudo raspi-config
   ```
   * Select "Interfacing Options"
   * Select "VNC"and enable it
   * Finish

 **2. Download, install and launch VNC Viewer**
 
 **3. create a new connection: Enter "raspberrypi.local" in VNC Server section**
 
 **4. Enter Username and Password**
 
