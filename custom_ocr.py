import os
import re
import easyocr
from natsort import natsorted


def main(img_dir):
    reader = easyocr.Reader(["en"], recog_network="custom_example")
    contents = ""

    image_files = [f for f in os.listdir(img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    image_files = natsorted(image_files)
    
    for image_file in image_files:
        result = reader.readtext(os.path.join(img_dir, image_file))

        # 結果の有無
        if result:
            number_str: str = result[-1][1]
        else:
            number_str = "-----None"

        # 数字のみにする
        number = re.sub(r"\D", "", number_str)
        if number == "":
            number = "-----None"

        # ファイルに書き込む内容まとめる
        contents = contents + image_file + "\t" + number + "\n"

    # ファイル書き込み
    with open("./ocr.txt", mode="w") as f:
        f.write(contents)


if __name__ == "__main__":
    img_dir = "./front_views_all_32x100"
    main(img_dir)


# 構造例
[
    (
        [
            [54, 0], [206, 0], [206, 46], [54, 46]
        ], 
        'Lo ', 
        0.08661511767775976
    ), 
    (
        [
            [92, 42], [238, 42], [238, 118], [92, 118]
        ], 
        '4 88', 
        0.9120393395423889
    )
]