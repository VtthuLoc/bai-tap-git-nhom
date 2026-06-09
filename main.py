def tinh_thue_thu_nhap(thu_nhap):
    # Kết hợp logic của Dev A và Dev B
    thu_nhap_tinh_thue = thu_nhap - 4000000
    return max(0, thu_nhap_tinh_thue * 0.1)

thu_nhap = float(input("Nhập thu nhập: "))
print("Thuế phải nộp của bạn là:", tinh_thue_thu_nhap(thu_nhap))