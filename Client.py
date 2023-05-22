import socket
if __name__ == '__main__':
    cont = True
    #getting the server ip address
    host = input("enter server IP address: ")
    #getting using the port number that the server uses
    while True:
        try:
            port = int(input("enter port number: "))
            break
        except:
            print("invalid port number")
    #sending a message to the server till not wanting to anymore
    while cont == True:
        message = input("enter message: ")
        message = message.encode('utf-8')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.send(message)
            data = s.recv(1024)
        test = data.decode('utf-8')
        print(f"Echo reply: {test}")
        decision = input("continue y/n: ")
        while True:
            if decision == "y":
                message = "y"
                message = message.encode('utf-8')
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((host, port))
                    s.send(message)
                cont = True
                break
            elif decision == "n":
                message = "n"
                message = message.encode('utf-8')
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((host, port))
                    s.send(message)
                cont = False
                break
    #closingserver connection
    s.close()