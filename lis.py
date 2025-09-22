import socket

host = '0.0.0.0'
port = 4444


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"[*] Listening on {host}:{port}")

    f = open("listen.txt", "w")
    f.write(f"\nListening on {host}:{port}")
    # Main loop to continuously accept new connections
    while True:
        try:
            client_socket, addr = server_socket.accept()
            
            with client_socket:
                print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
                
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    f.write(data.decode('utf-8', errors='ignore'))
            
            print(f"[*] Connection from {addr[0]} closed.")

        except KeyboardInterrupt:
            print("\n[*] Server is shutting down.")
            break
        except Exception as e:
            print(f"[!] An error occurred: {e}")
