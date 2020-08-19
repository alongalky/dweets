"""
This script converts a png image into a dweet friendly hex
"""
import imageio

image_path = "scrolling-bitmap-bigint/image.png"
image = imageio.imread(image_path)
byte = ""

print('0x',end='')
for row in image[::-1]:
    for col in row[::-1]:
        byte += "1" if col[0] == 0 else "0"
        if len(byte) == 4:
            # Print as hex
            i = int(byte, 2)
            print(hex(i)[2:], end="")
            byte = ""
print('n')
