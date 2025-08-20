class BiensoModel:
    def __init__(self):
        self.img_full = None   # Ảnh gốc tải lên
        self.img_crop = None   # Ảnh biển số (nếu có)

    def set_image(self, img):
        self.img_full = img

    def detect_plate(self):
        # Giả sử dùng thuật toán hoặc EasyOCR
        # Trả về (True/False, ảnh_crop nếu có)
        # True = phát hiện được biển số
        # False = không phải biển số
        # img_crop là ImageTk.PhotoImage
        # Demo tạm:
        if self.img_full:  # ví dụ luôn nhận diện thành công
            self.img_crop = self.img_full.crop((50,50,430,150))  # cắt thử
            return True, self.img_crop
        return False, None
