import random
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# Setup CORS
origins = [
    "http://localhost:3000",  # Update this with the actual origin of your frontend
    "https://www.e-hospital.ca",  # Add additional origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

GLAUCOMA_API_URL = "https://glaucomaapi-2024-6fc75a38c6ac.herokuapp.com"

@app.post("/predict")
async def upload_image(image: UploadFile = File(...)):
    contents = await image.read()
    # Here you can process the image contents as per your requirements
    
    # Random acknowledgment statement
    acknowledgments = [
        "True",
        "False",
    ]
    acknowledgment = random.choice(acknowledgments)
    
    return { "Glaucoma": acknowledgment}

@app.post("/predict-proxy")
async def predict_proxy(image: UploadFile = File(...)):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"{GLAUCOMA_API_URL}/predict", files={"image": image.file})
            return response.json()
        except httpx.HTTPError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail="Error from Glaucoma API")
