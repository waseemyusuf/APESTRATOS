# Note: if you run this file, remember to pip install exif if you dont have the module exif
import os
from exif import Image
import json

def parse_metadata(folder_name):
    time_name_list = {}

    images_path = os.path.dirname(os.path.abspath(__file__)) + "/" + folder_name
    image_list = os.listdir(images_path)

    for image in image_list:
        ext = os.path.splitext(image)[1]
        if ext == '.jpg':
            with open(images_path + "/" + image, "rb") as f:
                f = Image(f)
                time = f.datetime_original.split()[1]
                h, m, s = map(int, time.split(":"))
                duration = (h-3)*3600 + m*60 + s
                duration_rounded = 30 * round(duration/30)
                time_name_list[duration_rounded] =  "static/images/" + folder_name + "/" + image

    return time_name_list

pic_hor = parse_metadata("hor images")
pic_nad = parse_metadata("nadir images")

# The 2 files "hors_imgs.txt" and "nadir_imgs.txt" were made by simply
# copy pasting the results of the following print statements on the command line
# a better way would be to write the results to a file directy using python

# print("pic_nadir = [")
# for i in pic_nad:
#     print(f"    {i},")
# print("]")
#
# print("pic_hor = [")
# for i in pic_hor:
#     print(f"    {i},")
# print("]")

with open("hor.txt", "w") as f:
    json.dump(pic_hor, f)

with open("nadir.txt", "w") as f:
    json.dump(pic_nad, f)
