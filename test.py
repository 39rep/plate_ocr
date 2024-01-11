import cv2
import os
import numpy as np

def resize_image():
    pass

def main(input_folder, output_folder):
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    if not image_files:
        print("指定されたフォルダに画像が見つかりませんでした。")
        return
    
    # ファイル名でソート
    image_files.sort()

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file)
        img = cv2.imread(image_path)

        # 縦横比で変換比率決定
        dst = []
        diff = 0
        height, width, _ = img.shape[:3]
        aspect_ratio = width / height
        if aspect_ratio < 1.5:
            diff = 35
        elif aspect_ratio < 1.6:
            diff = 30
        elif aspect_ratio < 1.8:
            diff = 20
        elif aspect_ratio < 1.9:
            diff = 10
        else:
            diff = 0

        # 変換の隅決め
        pts1 = np.float32([[0,0],[0,height-diff],[width,height],[width,diff]])
        pts2 = np.float32([[0,0],[0,height],[250,height],[250,0]])

        # 投影変換
        M = cv2.getPerspectiveTransform(pts1,pts2)
        dst = cv2.warpPerspective(img,M,(250,height))
        # グレースケール
        dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
        dst = dst[30:120, 50:240]
        # ネガポジ反転
        # if dst.mean() < 150:
        #     dst = 255 - dst
        # ret, dst = cv2.threshold(dst, 100, 255, cv2.THRESH_TOZERO)
        cv2.imwrite(output_path, dst)


if __name__ == "__main__":
    input_folder = "/home/lagusa/python/palte_ocr/originals"
    output_folder = "/home/lagusa/python/palte_ocr/front_views"
    main(input_folder, output_folder)