import socket


if __name__ == '__main__':
    cont = True
    Host = input("enter host address: ")
    #to check if the port number is correct
    checkPort = True
    while checkPort == True:
        try:
            port = int(input("enter port number: "))
            checkPort = False
        except:
            print("invalid port number")
            checkPort = True
    #while loop to create the infinite loop of messages between client and server
    while cont == True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serve:
            #turning on the server
            host = str(Host)
            serve.bind((host, port))
            serve.listen()
            conn, addr = serve.accept()
            with conn:
                print(f"connected by {host} , {port}")
                checker = True
                #allows the message to indicate if the loop were to continue or not
                while checker == True:
                    data = conn.recv(1024)
                    translate = data.decode('utf-8')
                    if translate == "y":
                        checker = True
                    elif translate == "n":
                        checker = False
                        cont = False
                    else:
                        #message of the client after decoded
                        print(f"Echo Client Message: {translate}")
                        up = translate.upper()
                        data = up.encode('utf-8')
                        conn.send(data)
                        break
    #turn off the server connection
    serve.close()
