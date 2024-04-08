import random
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/upload/")
async def upload_image(image: UploadFile = File(...)):
    contents = await image.read()
    # Here you can process the image contents as per your requirements
    
    # Random acknowledgment statement
    acknowledgments = [
        f"Image '{image.filename}' Glaucoma : True",
        f"Image '{image.filename}' Glaucoma : False",
    ]
    acknowledgment = random.choice(acknowledgments)
    
    return {"filename": image.filename, "acknowledgment": acknowledgment}
