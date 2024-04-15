from PIL import Image
import numpy as np
import math
from scipy import signal
import matplotlib.pyplot as plt


def get_image_info(image_path: str, mode: str = "RGB") -> list[tuple]:
    image = Image.open(image_path).convert(mode)

    pixel = image.load()  # 载入图片信息

    # 获取图片大小
    width = image.size[0]
    height = image.size[1]

    info_list = []  # 创建空列表用于存储每个像素点的法向量

    for y in range(height):
        for x in range(width):
            info = pixel[x, y]
            info_list.append(info)

    return info_list


def main():
    original_image_colors = get_image_info("original_image.png")
    normal_vector_list = get_image_info("normal_map.png", "L")

    original_image = np.asarray(Image.open("original_image.png"))
    map_image = np.asarray(Image.open("normal_map.png"))

    print(original_image[0])



    plt.imshow(original_image)
    plt.show()


if __name__ == '__main__':
    main()
