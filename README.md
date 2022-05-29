


Steps
1. Installation Raspberry Pi
    1-1. git clone https://github.com/adadruit/Adafruit_Python_CharLCD.git
    1-2. cd ./Adafruit_Python_CharLCD
    1-3. sudo python setup.py install
 

2. Enable SPP on Raspberry Pi
    In order to use SPP, Bluetooth service needs to be restarted with ‘compatibility’ flag.

    2-1. Open Bluetooth service configuration file.
        sudo nano /etc/systemd/system/dbus-org.bluez.service

    2-2. Look for a line starts with “ExecStart” and add compatibility flag ‘-C’ at the end of the line.
        ExecStart=/usr/lib/bluetooth/bluetoothd -C

    2-3. Add a line below immediately after “ExecStart” line, then save and close the file.
        ExecStartPost=/usr/bin/sdptool add SP

    2-4. Reload the configuration file.
        sudo systemctl daemon-reload

    2-5. Restart the service.
        sudo systemctl restart bluetooth.service
 

3. Pairing
    To establish a connection, Raspberry Pi and the phone need to be paired.

    3-1. Launch bluetoothctl.
        bluetoothctl

    3-2. Enter below in order to be discovered from the phone.
        discoverable on

    3-3. On the phone, scan for Raspberry Pi and pair. You should be able to see something like below.
        [CHG] Device XX:XX:XX:XX:XX:XX Paired: yes

    3-4. Press Ctrl+D to quit.


4. Establishing Connection from Phone

    4-1. Listen for incoming connection on Raspberry Pi.
        sudo rfcomm watch hci0

    4-2. Install and launch “Flutter Pi Terminal” app on the phone.

    4-3. In the app, go to “Device” menu and select Raspberry Pi. If everything goes well and the connection is established, you should be able to see like this:
        sudo rfcomm watch hci0
        Waiting for connection on channel 1
        Connection from XX:XX:XX:XX:XX:XX to /dev/rfcomm0
        Press CTRL-C for hangup
 

5. Listen to chat messages send from phone on Raspberry Pi

    5-1. Open another terminal and launch pi_lcd application.
        main.py /dev/rfcomm0