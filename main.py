from fastapi import FastAPI, File, UploadFile, HTTPException
from transformers import pipeline
from PIL import Image
import io

app = FastAPI()

# Khởi tạo mô hình NSFW từ Hugging Face 
classifier = pipeline("image-classification", model="Falconsai/nsfw_image_detection")

@app.get("/") # Yêu cầu chức năng 1 
def read_root():
    return {
        "message": "Chào mừng đến với API nhận dạng nội dung ảnh",
        "student": "Huỳnh Huy Hoàng - 24120181",
        "model": "Falconsai/nsfw_image_detection"
    }

@app.get("/health") # Yêu cầu chức năng 2 
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Kiểm tra an toàn để tránh lỗi 'NoneType' object has no attribute 'startswith'
    if not file or not file.content_type:
         raise HTTPException(status_code=400, detail="Không nhận diện được file ảnh.")

    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File tải lên không phải là ảnh!")

    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # Gọi mô hình và trả kết quả JSON 
        results = classifier(image)
        return {"filename": file.filename, "predictions": results}
    except Exception as e:
        # Xử lý lỗi trong quá trình suy luận 
        raise HTTPException(status_code=500, detail=str(e))

# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# .\venv\Scripts\activate
# uvicorn main:app --reload

