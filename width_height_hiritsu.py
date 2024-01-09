from PIL import Image
import os

def calculate_aspect_ratio(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            aspect_ratio = width / height
            return width, height, aspect_ratio
    except Exception as e:
        print(f"エラー: {e}")
        return None

def main(folder_path):
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    if not image_files:
        print("指定されたフォルダに画像が見つかりませんでした。")
        return

    # ファイル名でソート
    image_files.sort()

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        image_info = calculate_aspect_ratio(image_path)

        if image_info is not None:
            width, height, aspect_ratio = image_info
            print(f"{image_file}: 幅 {width}, 高さ {height}, 縦横比 {aspect_ratio:.2f}")

if __name__ == "__main__":
    folder_path = "/home/god/mp/univ/plate_ocr/yellows"
    main(folder_path)
