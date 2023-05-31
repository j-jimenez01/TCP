# TCP Server-Client Communication

This program implements a TCP server and client communication system in Python that allows them to connect locally, virtually, and to other computers based on the provided host addresses.

## Client

The client component of the program performs the following steps:

1. Prompts the user to enter the IP address and port number of the server, along with a message to be sent.
2. Establishes a connection to the server using the provided host address.
3. Sends the message to the server through the established connection.
4. Receives the server's reply through the same connection and displays it.
5. Displays an error message if the IP address or port number were entered incorrectly.
6. The client is capable of sending multiple messages to the server, allowing for ongoing communication.

## Server

The server component of the program carries out the following tasks:

1. Listens for incoming connections from clients.
2. Upon receiving a connection, receives the message from the client.
3. Changes the letters of the message to uppercase and sends it back to the client through the same connection.
4. The server can handle multiple clients concurrently, allowing for simultaneous communication.

Please note that for the server and client to communicate successfully, they must be running on machines that are connected within the same network or have proper network configurations for remote communication.

## Usage

To use this TCP server-client communication program, follow these steps:

1. Ensure you have Python installed on your system (version 3.x recommended).
2. Open two terminal windows or command prompts.
3. In one terminal, navigate to the directory where the server program file is located.
4. Run the server program by executing the command: `python server.py`.
5. In the other terminal, navigate to the directory where the client program file is located.
6. Run the client program by executing the command: `python client.py`.
7. Follow the prompts on the client side to enter the server's IP address, port number, and the message you wish to send.
8. The client will establish a connection to the server and send the message.
9. The server will receive the message, convert the letters to uppercase, and send it back to the client.
10. The client will display the modified message received from the server.
11. The client can continue sending messages by repeating the input process.
12. To stop the program, you can terminate the server or client by closing their respective terminal windows or using the appropriate termination commands.
