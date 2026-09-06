# Chat Application

## Project Overview

This project is a simple real-time chat application built using Python's `socket` and `threading` modules.

The application uses a server-client architecture where two clients can connect to the server and exchange messages in real time. Messages are displayed with timestamps and usernames.

## Features

- Real-time communication between two clients
- Server listens for incoming client connections
- Client connects to the server using localhost
- Supports two-way message exchange
- Messages include timestamps and usernames
- Separate thread handles incoming messages
- Displays notifications when a user joins or disconnects
- Graceful disconnection handling
- Runs locally without external packages or APIs

## Technologies Used

- Python
- Socket Programming
- Threading
- datetime
