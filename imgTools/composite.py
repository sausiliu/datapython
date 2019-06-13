import os, sys
import cv2


def resize_image_percentage(img, height, width):
    top, bottom, left, right = (0, 0, 0, 0)

    h, w, _ = img.shape
    long_max = max(h, w)

    if h < long_max:
        dh = long_max - h
        top = dh // 2
        bottom = dh - top
    elif w < long_max:
        dw = long_max - w
        left = dw // 2
        right = dw - left
    else:
        pass

    # RGB
    BLACK = [0, 0, 0]
    WHITE = [255, 255, 255]

    constant = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=WHITE)
    return cv2.resize(constant, (height, width))


def do_resize(path_src, path_dest):
    for item in os.listdir(path_src):
        realpath = os.path.abspath(os.path.join(path_src, item))
        # print(realpath)

        if item.endswith('.jpg'):
            img = cv2.imread(realpath)
            img = resize_image_percentage(img, 750, 750)
            print('save' + path_dest + '/' + item)
            cv2.imwrite(path_dest + '/' + item, img)


def main():
    image_path = 'D:\\temp\images'
    resize_path = 'D:\\temp\img_resize'

    do_resize(image_path, resize_path)


if __name__ == '__main__':
    main()