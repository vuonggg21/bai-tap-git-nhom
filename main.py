def tinh_thue_thu_nhap(thu_nhap):
  if thu_nhap <= 0:
      return 0
        
    thue = 0
    if thu_nhap <= 5000000:
        thue = thu_nhap * 0.05
    elif thu_nhap <= 10000000:
        thue = thu_nhap * 0.1 - 250000
    elif thu_nhap <= 18000000:
        thue = thu_nhap * 0.15 - 750000
    elif thu_nhap <= 32000000:
        thue = thu_nhap * 0.2 - 1650000
    elif thu_nhap <= 52000000:
        thue = thu_nhap * 0.25 - 3250000
    elif thu_nhap <= 80000000:
        thue = thu_nhap * 0.3 - 5850000
    else:
        thue = thu_nhap * 0.35 - 9850000
        
    return thue

print("Thuế phải nộp của bạn là:", tinh_thue_thu_nhap(10000000))
