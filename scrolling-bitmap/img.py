"""
This script converts a png image into a dweet friendly hex
"""
import imageio

image_path = "scrolling-bitmap/image.png"
image = imageio.imread(image_path)
byte = ""

for row in image:
    for col in row:
        byte += "1" if col[0] == 0 else "0"
        if len(byte) == 4:
            # Reverse the bits in the byte
            byte = byte[::-1]

            # Print the bytes as hex
            i = int(byte, 2)
            print(hex(i)[2:], end="")
            byte = ""
print()
