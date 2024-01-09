import cv2
import numpy as np

class PlateOcr:
    def __init__(self, src: str) -> None:
        self.src = src
        self.image = cv2.imread(src)
        # グレースケール
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.areas = []
    
    def prepare_image(self):
        """画像の前処理"""
        pass

    def fint_rectangle(self):
        """輪郭検出"""
        # 2値化
        ret, img_binary  = cv2.threshold(self.gray, 150, 255, cv2.THRESH_BINARY)
        
        # 輪郭検出
        contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # 面積の大きいもののみ選別
        self.areas = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 1000:
                epsilon = 0.1*cv2.arcLength(cnt,True)
                approx = cv2.approxPolyDP(cnt,epsilon,True)
                if len(approx) == 4:
                    self.areas.append(approx)

        ##### 確認用
        print("len(areas):", len(self.areas))

        # 輪郭に色をつけたもの
        image_contour = cv2.drawContours(self.image, contours, -1, (0, 255, 0), 5)
        # ↑を保存
        output_path = "wips" + self.src[10:]
        self.output_image(image_contour, output_path)
        pass

    def transform_image(self):
        if len(self.areas) > 0:
            cv2.drawContours(img, self.areas, -1, (0,255,0), 3)
            # display_cv_image(img)
            # cv2.imwrite(wip_path, img)


            img = cv2.imread(self.src)
            # img = cv2.resize(img, (img.shape[1] * 2, img.shape[0] * 2))
            img = np.where(img > 220, 255, img)

            dst = []

            pts1 = np.float32(self.areas[0])
            pts2 = np.float32([[0,0],[0,300],[600,300],[600,0]])
            # pts2 = np.float32([[600,300],[600,0],[0,0],[0,300]])

            M = cv2.getPerspectiveTransform(pts1,pts2)
            dst = cv2.warpPerspective(img,M,(600,300))
            cv2.imwrite(output_path, dst)
        else:
            cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
            cv2.imwrite(output_path, img)
        pass

    def output_image(self, image, output_path: str):
        cv2.imwrite(output_path, image)
