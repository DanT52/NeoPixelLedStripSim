import asyncio
import websockets
import json

connected = set()  # Keep track of connected WebSocket clients

async def led_handler(websocket, path):
    connected.add(websocket)  # Add the new connection to the set
    try:
        async for message in websocket:  # Receive messages from clients
            data = json.loads(message)  # Parse the JSON message
            index = data['index']
            r = data['r']
            g = data['g']
            b = data['b']
            # Broadcast the received message to all other connected clients
            for conn in connected:
                if conn != websocket:  # Don't send the message back to the sender
                    await conn.send(json.dumps({'index': index, 'r': r, 'g': g, 'b': b}))
    finally:
        connected.remove(websocket)  # Remove the connection when it's closed

# Start the WebSocket server
start_server = websockets.serve(led_handler, 'localhost', 8765)

# Run the server until manually stopped
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
