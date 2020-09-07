from PIL import Image, ImageDraw

# 1 and 2:
try:
    a = 1 // 0
except ZeroDivisionError:
    print("Can not devide by zero")


# ------------------------------------------------------
# 3 - yes the code is legal

# ------------------------------------------------------

# 4- all of the exceptions

# ------------------------------------------------------

# 5 - it's not specific for unique type of exception,
#     it's a general way to catch exceptions

# ------------------------------------------------------

# 6 IOError and ZeroDivisionError

# ------------------------------------------------------

# 7 and 8 and 9 and 10
def create_new_file(file_name="words"):
    open(f"{file_name}.txt", "w").write("Fadi\n")
    with open(f"{file_name}.txt", "r") as file:
        for line in file:
            print(line)
    open(f"{file_name}.txt", "a+").write(" היי השם שלי" + "\n" + "פאדי זאבורה")
    with open(f"{file_name}.txt", "r") as file:
        for line in file:
            print(line)


# ------------------------------------------------------

# challenge 11
def create_image():
    img = Image.new('RGB', (100, 30), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((10, 10), "Hello World", fill=(255, 255, 0))
    img.save('pil_text.png')


# ------------------------------------------------------
def main():
    create_image()
    create_new_file()


if __name__ == "__main__":
    main()
