import asyncio
import websockets
import json

class FakeNeo:
    def __init__(self, num_pixels, auto_write=False):
        self.num_pixels = num_pixels
        self.auto_write = auto_write
        self.pixels = [(0, 0, 0)] * num_pixels  # Initialize all pixels to black
        self._websocket_uri = 'ws://localhost:8765'  # WebSocket server URI

    def fill(self, color):
        """Fill all pixels with the same color."""
        self.pixels = [color] * self.num_pixels
        if self.auto_write:
            self.show()

    def __setitem__(self, index, color):
        """Set the color of an individual pixel."""
        if 0 <= index < self.num_pixels:
            self.pixels[index] = color
            if self.auto_write:
                self.show()
        else:
            raise IndexError("Pixel index out of range")

    def __getitem__(self, index):
        """Get the color of an individual pixel."""
        if 0 <= index < self.num_pixels:
            return self.pixels[index]
        else:
            raise IndexError("Pixel index out of range")

    def show(self):
        """Send the pixel data to the virtual LED strip."""
        asyncio.run(self._send_pixel_data())

    async def _send_pixel_data(self):
        """Asynchronously send pixel data to the WebSocket server."""
        async with websockets.connect(self._websocket_uri) as websocket:
            for index, color in enumerate(self.pixels):
                r, g, b = color
                data = {
                    'index': index,
                    'r': r,
                    'g': g,
                    'b': b
                }
                await websocket.send(json.dumps(data))
                #await asyncio.sleep(0.01)  # Slight delay to ensure messages are processed

    def __len__(self):
        return self.num_pixels
