# Phân Tích Điểm Kiểm Tra Học Sinh

Dự án phân tích điểm kiểm tra của học sinh sử dụng Python, cung cấp các thống kê cơ bản và phân loại kết quả học tập.

## 📋 Mô Tả

Chương trình phân tích điểm kiểm tra của học sinh qua nhiều môn học khác nhau, bao gồm:
- Toán
- Văn
- Tiếng Anh
- Lý
- Hóa

## ✨ Tính Năng

- **Thống kê cơ bản**: Tính điểm trung bình, cao nhất, thấp nhất, trung vị
- **Độ lệch chuẩn**: Đo lường sự phân tán của điểm số
- **Phân loại học sinh**: Xếp loại theo thang điểm (Xuất sắc, Giỏi, Khá, Trung bình, Yếu)
- **So sánh môn học**: Xác định môn có điểm trung bình cao nhất và thấp nhất
- **Tổng hợp**: Tính điểm trung bình chung của tất cả các môn

## 🚀 Cách Sử Dụng

### Yêu Cầu
- Python 3.x

### Chạy Chương Trình

```bash
python analysis.py
```

Hoặc trên Windows với UTF-8 encoding:

```powershell
$env:PYTHONIOENCODING = 'utf-8'; python analysis.py
```

## 📊 Kết Quả Mẫu

Chương trình sẽ hiển thị:
- Phân tích chi tiết cho từng môn học
- Tổng kết môn có điểm cao nhất/thấp nhất
- Phân loại học sinh theo điểm số
- Điểm trung bình chung

## 📝 Cấu Trúc Code

- `test_scores`: Dictionary chứa điểm số mẫu cho các môn học
- `analyze_subject()`: Hàm phân tích thống kê cho một môn học
- `classify_score()`: Hàm phân loại điểm số
- `main()`: Hàm chính thực hiện phân tích và hiển thị kết quả

## 🔧 Tùy Chỉnh

Bạn có thể dễ dàng thay đổi:
- Dữ liệu điểm số trong dictionary `test_scores`
- Thang điểm phân loại trong hàm `classify_score()`
- Các môn học cần phân tích

## 📄 License

Dự án này được phân phối dưới giấy phép MIT License.

## 👤 Tác Giả

ThanhDo10T1

---

*Dự án demo được tạo để minh họa phân tích dữ liệu cơ bản với Python*
