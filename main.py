from PIL import Image
import matplotlib.pyplot as plt


def get_image_info(image_path: str) -> list[tuple]:
    image = Image.open(image_path)

    pixel = image.load()  # 载入图片信息

    # 获取图片大小
    width = image.size[0]
    height = image.size[1]

    info_list = []  # 创建空列表用于存储每个像素点的法向量

    for x in range(width):
        for y in range(height):
            info = pixel[x, y]
            info_list.append(info)

    return info_list


def main():
    original_image_colors = get_image_info("original_image.png")
    normal_vector_list = get_image_info("normal_map.png")




if __name__ == '__main__':
    main()
