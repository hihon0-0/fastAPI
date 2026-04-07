# 📘 BÀI THỰC HÀNH SỐ 1 - APPLICATION PROGRAMMING INTERFACE

## 👤 1. Thông tin sinh viên
- **Họ và tên:** Huỳnh Huy Hoàng  
- **Mã số sinh viên:** 24120181  
- **Lớp:** 24CTT5  
- **Trường:** Đại học Khoa học Tự nhiên - ĐHQG-HCM  
- **Môn học:** Tư duy tính toán  

---

## 🤖 2. Mô hình Hugging Face
- **Tên mô hình:** `nsfw_image_detection`  
- **Liên kết:** https://huggingface.co/Falconsai/nsfw_image_detection  
- **Chức năng:** Phân loại hình ảnh để nhận diện nội dung **nhạy cảm (NSFW)** hoặc **bình thường**  

---

## ⚙️ 3. Hướng dẫn cài đặt thư viện

```bash
pip install -r requirements.txt
```
---

## 🚀 4. Chạy chương trình (FastAPI)

Khởi động server bằng lệnh:
```bash
uvicorn main:app --reload
```

## 🌐 Sau khi chạy:

Truy cập tài liệu API tại: http://127.0.0.1:8000/docs

👉 Tại đây bạn có thể:

* **Test API** trực tiếp
* **Upload ảnh** để kiểm tra thực tế.
* **Xem chi tiết** cấu trúc Request/Response.

---

## 🔌 5. Sử dụng API
▶️ **Cách 1: Dùng file test**
```bash
python test_api.py
```
▶️ **Cách 2: Gọi API thủ công**

📥  **Request**
* **Method:** `POST`
* **Endpoint:** `/predict`
* **Content-Type:** `multipart/form-data`
* **Body:** file ảnh
  
📤 **Response (JSON)**
```bash
{
  "filename": "demo.jpg",
  "predictions": [
    {"label": "normal", "score": 0.999848484992981},
    {"label": "nsfw","score": 0.00015148617967497557}
  ]
}
```
📌**Ý nghĩa**
* `label`: loại ảnh
* `score`: độ tin cậy

---

## 🎥 6. Video Demo

🔗 https://drive.google.com/drive/folders/1c9-Aqv6ESWDnINl1koIUxwUeat_zq5-g?usp=sharing
