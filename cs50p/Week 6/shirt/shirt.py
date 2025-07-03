import sys
from PIL import Image, ImageOps
if len(sys.argv) != 3:
    sys.exit("no")
type = [".jpg", ".png", "jpeg"]
x = sys.argv[1].strip().lower()
y = sys.argv[2].strip().lower()
r = False
for n in type:
    if x.endswith(n):
        if y.endswith(n):
            r = True
if r == False:
    sys.exit(1)

s = "shirt.png"
try:
    with Image.open(x) as img:
        with Image.open(s) as shirt:
            size = shirt.size
            img = ImageOps.fit(img, size)
            img.paste(shirt, shirt)
            img.save(y)
except FileNotFoundError:
    sys.exit(2)
