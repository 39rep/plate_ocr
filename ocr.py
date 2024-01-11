import easyocr
import re


reader = easyocr.Reader(["en"])
contents = ""

for i in range(600):
    # result = reader.readtext(f"/home/god/mp/univ/plate_ocr/yellows/output/number{str(i).zfill(3)}.jpg")
    result = reader.readtext(f"/home/lagusa/python/palte_ocr/front_views/plate{str(i)}.jpg")

    if result:
        number_str: str = result[-1][1]
    else:
        number_str = "-----None"

    # 数字のみにする
    number = re.sub(r"\D", "", number_str)
    if number == "":
        number = "-----None"
    number = number + "\n"

    # ファイルに書き込む内容まとめる
    contents = contents + number

# ファイル書き込み
with open("/home/lagusa/python/palte_ocr/ocr.txt", mode="w") as f:
    f.write(contents)

    # print(f"plate{str(i)}:\n{number_str}")

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