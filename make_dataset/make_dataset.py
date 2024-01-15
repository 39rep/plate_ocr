import os
import shutil
import re

def main(dir):
    # 振り分け前の画像取得, ソート
    org = os.path.join(dir, "original_img")
    image_files = [f for f in os.listdir(org) if f.lower().endswith(('.png', '.jpg'))]
    image_files.sort()

    gt = ["", "", ""]

    with open(os.path.join(dir, "gt.txt")) as f:
        lines = f.readlines()
        for image_file in image_files:
            num = int(re.sub(r"\D", "", image_file))
            if num % 12 == 0 and num > 0:
                gt[2] += lines[num]
                shutil.copy2(os.path.join(dir, "original_img", image_file), os.path.join(dir, "data/test/img"))
            elif num % 11 == 0 and num > 0:
                gt[1] += lines[num]
                shutil.copy2(os.path.join(dir, "original_img", image_file), os.path.join(dir, "data/valid/img"))
            else:
                gt[0] += lines[num]
                shutil.copy2(os.path.join(dir, "original_img", image_file), os.path.join(dir, "data/train/img"))


    # ゴリ押し書き込み
    with open(os.path.join(dir, "data/test/gt.txt"), mode='w') as f:
        f.write(gt[2])

    with open(os.path.join(dir, "data/valid/gt.txt"), mode='w') as f:
        f.write(gt[1])

    with open(os.path.join(dir, "data/train/gt.txt"), mode='w') as f:
        f.write(gt[0])
    

if __name__ == "__main__":
    dir = "/home/god/mp/univ/plate_ocr/make_dataset/"
    main(dir)