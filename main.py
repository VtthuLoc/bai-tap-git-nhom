def tinh_thue_thu_nhap(thu_nhap):
   if thu_nhap<=10000000:
    thue=0
  elif thu_nhap<=30000000:
    thue=thu_nhap*0.1
  elif thu_nhap<=50000000:
    thue=thu_nhap*0.2
  else:
    thue = thu_nhap*0.3
  return thue
thu_nhap = float(input("Nhap thu nhap: "))
print("Thue phai nop la:", tinh_thue_thu_nhap(thu_nhap))
