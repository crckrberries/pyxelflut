import socket, random, os, secrets, numpy, binascii, threading, logging, time
from PIL import Image, ImageDraw, ImageFont

def sendlines(list, socket):
    for line in lines:
        s.send(line.encode())
        time.sleep(0.1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("tcp://pixelflut.uwu.industries", 1234))
s.connect(("127.0.0.1", 1234))

mode = input("mode: ")
if  mode == "t":
    txt = input("text: ")
    size = int(input("size: "))
    font = ImageFont.truetype('./Arial.ttf', size)
    img = Image.new('RGB', (0, 0), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    tlength = draw.textlength(txt, font)
    img = Image.new('RGB', (round(tlength) + 20, size * 2), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), txt, fill=(0, 0, 0), font=font, align='center')
elif mode == "w":
    img = Image.new('RGB', (1280, 720), (0, 0, 0))
else:
    filename = input("file: ")
    img = Image.open(filename)
    img = img.resize([int(elem) for elem in input("size: ").split()])

width, height = img.size

# s.send('SIZE\n'.encode())
# size = s.recv(10).decode()[5:].split()
# print(size)

xoff, yoff = [int(elem) for elem in input("offset: ").split()]

lines = []
for y in range(height):
    line = ''
    for x in range(width):
        rgb = img.getpixel((x, y))
        hexcolor = '%02x%02x%02x' % (rgb)
        line += 'PX %d %d %s\n' % (x + xoff, y + yoff, hexcolor)
    lines.append(line)


# random.shuffle(lines)

sendlines(lines, s)
s.close()