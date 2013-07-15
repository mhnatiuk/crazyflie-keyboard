crazyflie-keyboard
==================
Testing how to control Bitcraze Crazyflie 10DOF from keyboard - the goal was to be able to automatically
start and land it. However, I am waiting for another one, since the one I had have chosen freedom and flew away...

Usage:
1. Set up Crazyflie and Crazyradio. Make sure that LEDs work as described on bitcraze wiki.
2. Make sure that you use 250K connection, otherwise edit appropriate code.
3. Run server.py. Wait until it outputs "ready" on console
4. Adapt keyboard controls in client.py as needed. For now: A-D: roll, W-S: pitch, Q-E: yaw, < > thrust up/down, M- set thrust to 40K
