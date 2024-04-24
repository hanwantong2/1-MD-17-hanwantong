from PIL import Image
from PIL import ImageDraw, ImageFont

# from PIL.Image import Image

image_path = "download_postcard.jpg"

img = Image.open(image_path)

area = [100, 100, 400, 400]
cropped_image = img.crop(area)

cropped_image.save("cropped_postcard.jpg")

# print("save cropped_postcard.jpg")

postcard_dict = {
    "Christmas": "christmas_postcard.jpg",
    "New year": "new year_postcard.jpg",
    "Biethday": "birthday_postcard.jpg",
}

holiday = input("birthday : ")

if holiday in postcard_dict:
    print(f"What i choose:{postcard_dict[holiday]}")
else:
    print("sorry,not found.")



name = input("Suga:")

img = Image.open("downloaded_postcard.jpg")

font = ImageFont.truetype("arial.ttf", 50)

draw = ImageDraw.Drawraw(img)

text = f"Congratulations,{"suga"}!"
text_width, text_height = draw, text_size(text, font=font)
text_position = ((img.width - text_width) // 2, (img.heigtht - text_height) // 2)

draw.text(text_position, text, font=font, fill="black")

img.save("congratulations_postcard.jpg")

print("text save congratulations_postcard.jpg")
