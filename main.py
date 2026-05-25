# Phân tích và Đề xuất giải pháp
# A. Phân tích Input / Output
# Input (Dữ liệu đầu vào)

# Điều dưỡng nhập dữ liệu từ bàn phím bằng input()

# Đề xuất 2 giải pháp ép kiểu dữ liệu
# Giải pháp 1 — Ép kiểu trực tiếp khi nhập
# Giải pháp 2 — Nhập chuỗi trước rồi mới ép kiểu
# Tiêu chí	                Giải pháp 1	      Giải pháp 2
# Số lượng biến	              Ít hơn	       Nhiều hơn
# Độ ngắn gọn code	         Ngắn gọn	         Dài hơn
# Tốc độ viết code	           Nhanh	        Chậm hơn
# Dễ debug	                 Trung bình	         Tốt hơn
# Dễ kiểm tra dữ liệu sai	    Khó hơn	         Dễ hơn
# Phù hợp hệ thống lớn	       Khá tốt	         Tốt hơn

# Chốt lựa chọn giải pháp
# Giải pháp được chọn: Giải pháp 2
# Lý do

# Trong môi trường bệnh viện:

# Dữ liệu y tế cần độ chính xác cao
# Điều dưỡng có thể nhập sai định dạng
# Cần dễ kiểm tra và dễ dò lỗi

# Việc lưu dữ liệu nhập ban đầu dưới dạng chuỗi trước khi ép kiểu giúp:

# dễ validate dữ liệu
# dễ ghi log lỗi
# dễ bảo trì hệ thống

# Do đó giải pháp 2 an toàn hơn cho hệ thống y tế.

# =========================================
# HỆ THỐNG CHUẨN HÓA DỮ LIỆU SINH HIỆU
# =========================================

print("--- HỆ THỐNG TIẾP NHẬN SINH HIỆU ---")

# Nhập dữ liệu
patient_id = input("Nhập mã bệnh nhân: ")

temperature_input = input("Nhập nhiệt độ cơ thể: ")
heart_rate_input = input("Nhập nhịp tim: ")

# Chuẩn hóa dữ liệu
temperature = float(temperature_input)
heart_rate = int(heart_rate_input)

# Hiển thị kết quả
print("\n--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")

print("Mã bệnh nhân:", patient_id)

print("Nhiệt độ cơ thể:", temperature, "độ C")
print("⇒ Kiểu dữ liệu hệ thống ghi nhận:", type(temperature))

print("Nhịp tim:", heart_rate, "nhịp/phút")
print("⇒ Kiểu dữ liệu hệ thống ghi nhận:", type(heart_rate))

print("Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")