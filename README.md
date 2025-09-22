# Python-KeyLogger
Created for educational purposes.

Description
This project is a simple networked keylogger. It contains two Python scripts, a client-side keylogger (KeyLogger.py) and a server-side listener (lis.py). The keylogger captures the keystrokes from a client's machine and sends the logs over a network connection to the listener. The listener receives the data and saves it to a text file.

Disclaimer: This tool is created for educational purposes only to demonstrate network programming, threading, and system-level event handling. The use of this code to monitor or access computer systems without explicit, written permission is illegal and unethical.

Features:
  Client-side keylogger: The KeyLogger.py script uses the pynput library to capture keystrokes while running in a separate thread to ensure the application doesn't freeze.
  Periodic Data Transmission: The client script captures the keystrokes and then sends them to the server on a configurable time interval.
  Server-Side Listener: The lis.py script listens for incoming connections on a specified IUP address and port.

Getting Started:
  Prerequisites:
    Python 3.x
    pynput library

  Installation:
    Install the required library
      pip install pynput

  Usage:
      Configure the Keylogger.py script
        Change the SERVER_IP variable to the IP address of the machine running the listener script
        Ensure the SERVER_PORT matches the port in the listener script (Default is 4444)
      Start the lis.py script
        The server will start listening on 0.0.0.0:SERVER_PORT and will save received data to listen.txt.
      Run the KeyLogger.py client script
      View in Logs

Project Structure
  KeyLogger.py: Client-side script for capturing keystrokes and sending them over the network
  lis.py: The server-side script for listening for connections and then logging the keystrokes
  listen.txt: The file where the keystrokes will be saved. 
        
