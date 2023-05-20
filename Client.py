import socket

if __name__ == '__main__':
    cont = True
    host = input("enter host address: ")
    #while loop will identify if the port number
    #is invalid or not by checking if its an int
    checkPort = True
    while checkPort == True:
        try:
            port = int(input("enter port number: "))
            checkPort = False
        except:
            print("invalid port number")
            checkPort = True
    host = str(host)
    #while loop for the echo client that will enter a message.
    #message gets encoded then it client attempts to connect to the server
    #and sends the data. options to continue or not and
    #it will send a yes or no response to the server to close the connection
    while cont == True:
        message = input("enter message: ")
        message = message.encode('utf-8')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.send(message)
            data = s.recv(1024)
        test = data.decode('utf-8')
        print(f"Echo reply: {test}")
        #indicate to send a message to the server to sever the connection
        decision = input("continue y/n: ")
        checker = True
        while checker == True:
            if decision == "y":
                message = "y"
                message = message.encode('utf-8')
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((host, port))
                    s.send(message)
                cont = True
                checker = False
            elif decision == "n":
                message = "n"
                message = message.encode('utf-8')
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((host, port))
                    s.send(message)
                cont = False
                checker = False
            else:
                checker = True
    #turn off the server connection
    s.close()