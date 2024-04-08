import random
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/predict")
async def upload_image(image: UploadFile = File(...)):
    contents = await image.read()
    # Here you can process the image contents as per your requirements
    
    # Random acknowledgment statement
    acknowledgments = [
        f"Image '{image.filename}' True",
        f"Image '{image.filename}' False",
    ]
    acknowledgment = random.choice(acknowledgments)
    
    return { "Glaucoma": acknowledgment}
