# NeoPixelLedStripSim

This project is a neoPixel simulator, designed to test neoPixel code. 

![Demo](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHAzank1eWEyZ3pqd2RoM2pmM2tzMDFhMWZ1dGc3aDZjaWYxbHJ5MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ADYwqNn2AJwLejUvpq/giphy.gif)



## How To Run

1. Edit the first line of the `script.js` file to change the number of LEDs in the strip.

  ```javascript
const n = 10; // Number of LEDs
```
  
2. Start the python server.
```bash
  python server.py
```

3. Open up the index.html
4. Run your pixel script example below.


# Example Usage

```python
# example_usage.py
from fake_neo import FakeNeo

# Create a virtual LED strip with 10 LEDs
pixels = FakeNeo(num_pixels=10, auto_write=False)

# Set the color of all pixels to blue
pixels.fill((0, 0, 255))

# Change the color of the first pixel to red
pixels[0] = (255, 0, 0)

# Apply the changes
pixels.show()
```

### Potential future fix
Have only the changed parts of the strip be sent
  - this could be implemented with a stack.
  - have a flag for if fill was used then send the whole strip.
