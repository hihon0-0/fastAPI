BÀI THỰC HÀNH SỐ 1 - APPLICATION PROGRAMMING INTERFACE
1. Thông tin sinh viên 
    Họ và tên: Huynh Huy Hoang
    Mã số sinh viên: 24120181. Lớp: 24CTT5 
    Trường: Đại học Khoa học Tự nhiên - ĐHQG-HCM 
    Môn học: Tư duy tính toán 
2. Mô hình Hugging Face 
    Tên mô hình: nsfw_image_detection 
    Liên kết: Falconsai/nsfw_image_detection 
    Chức năng: Phân loại hình ảnh để nhận diện nội dung nhạy cảm (NSFW) hoặc nội dung bình thường (Normal).
3. Hướng dẫn cài đặt thư viện
    Dự án sử dụng môi trường ảo Python. Để cài đặt các thư viện cần thiết, chạy lệnh sau:
                    Bashpip install -r requirements.txt
4. Hướng dẫn chạy chương trình Để khởi động Web API bằng FastAPI, sử dụng lệnh:
                    Bashuvicorn main:app --reload
    Sau khi server chạy, bạn có thể truy cập tài liệu API tại: http://127.0.0.1:8000/docs
5. Hướng dẫn gọi API và Ví dụ 
    Cách gọi API bằng Python:
    Sử dụng file test_api.py có sẵn trong mã nguồn để kiểm thử:
                    Bashpython test_api.py
Ví dụ Request/Response Request:
    Gửi file ảnh qua phương thức POST tới /predict.
    Response:JSON
    {
        "filename": "demo.jpg",
        "predictions": [
            {"label": "normal", "score": 0.999848484992981},
            {"label": "nsfw", "score": 0.00015148617967497557}
        ]
    }
6. Video Demo Liên kết video: 