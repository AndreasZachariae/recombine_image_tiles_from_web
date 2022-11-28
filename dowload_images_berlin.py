import urllib.request
import os

# base_url = "https://www.ub.uni-freiburg.de/fileadmin/ub/images/digitalisierung/stadtplaene/0001898/"
# folder = "TileGroup1/"  # "TileGroup0/"
# image_name = "4-"

base_url = "https://berliner-stadtplansammlung.de/images/maps/1857%20Generalstab/5/"


for folder in range(0, 32):
    tmp_folder = "berlin/"+str(folder) + "/"
    os.makedirs(tmp_folder, exist_ok=True)
    for number in range(4, 28):
        temp_image = str(number) + ".png"

        try:
            urllib.request.urlretrieve(
                base_url + str(folder) + "/" + temp_image, tmp_folder + temp_image)
        except:
            print(tmp_folder + temp_image)
