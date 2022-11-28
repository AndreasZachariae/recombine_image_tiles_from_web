import cv2


foler_path = "berlin/"
image = None

for folder in range(0, 32):
    tmp_folder = foler_path+str(folder) + "/"
    vertical_image = None
    for number in range(4, 28):
        temp_image = str(number) + ".png"

        try:
            new_tile = cv2.imread(tmp_folder + temp_image)
            if vertical_image is None:
                vertical_image = new_tile
            else:
                vertical_image = cv2.vconcat([vertical_image, new_tile])
        except:
            print(tmp_folder + temp_image)


    if image is None:
        image = vertical_image
    else:
        image = cv2.hconcat([image, vertical_image])
        
    cv2.imwrite('image.png', image)
