# TCP
Description: Created a Server and Client that will connect to each other locally, virtually, and to other computers based off the input of the host addresses.

Client:
1. Prompts the user to input the IP address, port number of the server,and a message to send to that server.
2. Sends the message to the server.
3. Display the server replay by using the same socket.
4. Displays an error message if the IP address or port number we reentered incorrectly.
5. The client should be able to send multiple messages to the server.You may need to consider using the infinite loop as we discussed in the class.

Server
1. Receives the message from the client.
2. Change the letters of the message to “capital letters” and send it back to the client by using the same socket.
3. The server should be able to send multiple messages to the client.