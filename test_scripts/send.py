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

# Print the current state of the LEDs
print(pixels.pixels)  # Should output: [(255, 0, 0), (0, 0, 255), (0, 0, 255), ..., (0, 0, 255)]
