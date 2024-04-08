from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/predict")
async def upload_image(image: UploadFile = File(...)):
    contents = await image.read()
    # Here you can process the image contents as per your requirements
    
    # Acknowledgement statement
    acknowledgment = f"Image '{image.filename}' Glaucoma:True."
    
    return {"filename": image.filename, "acknowledgment": acknowledgment}
