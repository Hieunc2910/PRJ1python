# Hiện tại giá điện đang được tính theo bậc thang gồm 6 mức (mức điều chỉnh từ 04/05/2023), với giá thấp nhất (bậc 1) là 1.728VND và giá bậc cao nhất là 3.015 VND. Tuy nhiên EVN đang đề xuất một cách tính giá điện bậc thang mới chỉ gồm 5 mức như hinh dưới, giá thấp nhất (bậc 1) khoảng 1.728 đồng một kWh và cao nhất (bậc 5) là 3.457 đồng một kWh.
#
# Bậc	Biểu giá hiện hành	Phương án 5 bậc
#   	Mức sử dụng	Giá (*)	Mức sử dụng	Giá
# 1	0-50 kWh	1.728	0-100 kWh	1.728
# 2	51-100 kWh	1.786	101-200 kWh	2.074
# 3	101-200 kWh	2.074	201-400 kWh	2.612
# 4	201-300 kWh	2.612	401-700 kWh	3.111
# 5	301-400 kWh	2.919	701 kWh trở lên	3.457
# 6  	401 kWh trở lên	3.015
# (*) Giá chưa bao gồm thuế VAT
#
# Hãy xây dựng chương trình nhập vào số kwh điện của một hộ tiêu thụ và so sánh xem theo bảng giá mới đang lấy ý kiến thì tiền điện tiêu thụ của hộ đó sẽ tăng thêm hay giảm đi bao nhiêu.
#
# INPUT: là số kwh điện tiêu thụ của hộ (là số nguyên)
# OUTPUT: là chênh lệch giữa giá theo đề xuất và giá theo mô hình bậc thang 6 mức đang được áp dụng.
#
# VAT sẽ được lấy là 10%, và kết quả in ra sẽ lấy tới 2 chữ số thập phân
#
# EXAMPLE
# INPUT
# 540
# OUTPUT
# -22176.00
#
#
# INPUT
# 70
# OUTPUT
# -1276.00
def tien_dien_ms(so_dien):
    tien_dien_moi =0
    if so_dien>700:
        tien_dien_moi=(so_dien-700)*3457
        so_dien=700
    if so_dien>400:
        tien_dien_moi+=(so_dien-400)*3111
        so_dien=400
    if so_dien>200:
        tien_dien_moi+=(so_dien-200)*2612
        so_dien=200
    if so_dien>100:
        tien_dien_moi+=(so_dien-100)*2074
        so_dien=100
    tien_dien_moi+=so_dien*1728
    return int(tien_dien_moi)
def tien_dien_cu(so_dien):
    tien_dien_cu =0
    if so_dien>401:
        tien_dien_cu+=(so_dien-400)*3015
        so_dien=400
    if so_dien>300:
        tien_dien_cu+=(so_dien-300)*2919
        so_dien=300
    if so_dien>200:
        tien_dien_cu+=(so_dien-200)*2612
        so_dien=200
    if so_dien>100:
        tien_dien_cu+=(so_dien-100)*2074
        so_dien=100
    if so_dien>50:
        tien_dien_cu+=(so_dien-50)*1786
        so_dien=50
    tien_dien_cu+=so_dien*1728
    return int(tien_dien_cu)
if __name__ == '__main__':
    so_dien = int(input())
    chenh_lech =(tien_dien_ms(so_dien)-tien_dien_cu(so_dien))*1.1
    print('{:.2f}'.format(chenh_lech))

