import cv2


foler_path = "freiburg3/"
image = None

for first_number in range(0, 21):
    vertical_image = None
    for sec_number in range(0, 35):
        temp_image = "6-" + str(first_number) + "-" + str(sec_number) + ".jpg"

        try:
            new_tile = cv2.imread(foler_path + temp_image)
            if vertical_image is None:
                vertical_image = new_tile
            else:
                vertical_image = cv2.vconcat([vertical_image, new_tile])
        except:
            print(foler_path + temp_image)

    if image is None:
        image = vertical_image
    else:
        image = cv2.hconcat([image, vertical_image])

    cv2.imwrite('freiburg3_map.png', image)
