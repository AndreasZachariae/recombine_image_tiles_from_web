import urllib.request
import os

base_url = "https://www.ub.uni-freiburg.de/fileadmin/ub/images/digitalisierung/stadtplaene/00019101/"
base_folder = "freiburg2/"

for folder in range(4,18):
    folder = "TileGroup" + str(folder) + "/"

    os.makedirs(base_folder + folder, exist_ok=True)

    for first_number in range(0, 62):
        for second_number in range(0, 53):
            temp_image = "6-" + str(first_number) + "-" + str(second_number) + ".jpg"

            try:
                urllib.request.urlretrieve(
                    base_url + folder + temp_image, base_folder + folder + temp_image)
            except:
                print(folder + temp_image)

