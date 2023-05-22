import socket
if __name__ == '__main__':
    cont = True
    #getting IP address
    host = input("enter IP address: ")
    #getting a port number
    while True:
        try:
            port = int(input("enter port number: "))
            break
        except:
            print("invalid port number")
    #while loop to create the infinite loop of messages between client and server
    while cont == True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serve:
            serve.bind((host, port))
            serve.listen()
            conn, addr = serve.accept()
            with conn:
                print(f"connected by {host} , {port}")
                while True:
                    data = conn.recv(1024)
                    translate = data.decode('utf-8')
                    if translate == "y":
                        continue
                    elif translate == "n":
                        cont = False
                        break
                    else:
                        #message of the client after decoded
                        print(f"Echo Client Message: {translate}")
                        up = translate.upper()
                        data = up.encode('utf-8')
                        conn.send(data)
                        break
    #close server connection
    serve.close()
