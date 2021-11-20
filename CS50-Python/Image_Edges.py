
from PIL import Image, ImageFilter

Before = Image.open("DIK_8499.jpg")

After = Before.filter (ImageFilter.FIND_EDGES)

After.save("OutDIK_8499.jpg")

After.show()
