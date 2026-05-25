raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 " 
while True:
    print('''1. Hiển thị chuỗi mã vạch gốc
             2. Giải mã, làm sạch và in báo cáo kiểm kê
             3. Tra cứu nhanh theo đuôi Serial
             4. Thoát chương trình''')
    choice=int(input('Nhập lựa chọn của bạn'))
    match choice:
        case 1:
            print(raw_batch)
        case 2:
          part=raw_batch.split(';')
          valid=0
          print(f"\n{'MÃ SP':<8} {'XUẤT XỨ':<10} {'NĂM SX':<8} {'SERIAL':<10} {'TRẠNG THÁI'}")
          for item in part:
              ID=item.split('-')[0].strip().upper()
              nation=item.split('-')[1].upper()
              year="20"+item.split('-')[2]  
              serial=item.split('-')[3].strip()
              if not serial.isdigit():
                 print('Serial không hợp lệ')
                 continue
              trang_thai = " Hợp lệ"
              valid+=1
              print(f"{ID:<8} {nation:<10} {year:<8} {serial:<10} {trang_thai}")
              
          print(f"Đã giải mã thành công {valid} sản phẩm hợp lệ / Tổng số {len(part)} sản phẩm.")
        case 3:
            search=input("nhập hai số cuối của serial cần tìm")
            part = raw_batch.split(';')
            find = False

            for item in part:
                serial = item.split('-')[3].strip().upper()
                if(serial[-2:]==search):
                    find=True
                    ID     = item.split('-')[0].strip().upper()
                    nation = item.split('-')[1].upper()
                    year   = "20" + item.split('-')[2]
                    print(f"\n✅ Tìm thấy sản phẩm!")
                    print(f"   Mã SP  : {ID}")
                    print(f"   Xuất xứ: {nation}")
                    print(f"   Năm SX : {year}")
                    print(f"   Serial : {serial}")
            if(find==False):
                print(f'Không tìm thấy sản phẩm có serial {serial}')
        case 4:
            print("Tạm biệt")
            break
        case _:
            print('Lựa chọn không hợp lệ')
                
                    