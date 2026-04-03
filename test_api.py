import requests

url = "http://127.0.0.1:8000/predict"
# Nhớ để 1 tấm ảnh tên 'demo.jpg' vào cùng thư mục này nhé
file_path = "demo.jpg" 

with open(file_path, "rb") as f:
    # Gửi kèm tên file và định dạng để FastAPI không bị lỗi NoneType
    files = {"file": (file_path, f, "image/jpeg")} 
    response = requests.post(url, files=files)
    
    if response.status_code == 200:
        print("Kết quả từ API:", response.json())
    else:
        print(f"Lỗi {response.status_code}: {response.text}")