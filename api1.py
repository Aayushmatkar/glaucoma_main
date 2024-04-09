import random
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Setup CORS
origins = [
    "http://localhost:3000",  # Update this with the actual origin of your frontend
    "https://glaucomaapi-2024-6fc75a38c6ac.herokuapp.com/predict",
    "https://www.e-hospital.ca",# Add additional origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def upload_image(image: UploadFile = File(...)):
    contents = await image.read()
    # Here you can process the image contents as per your requirements
    
    # Random acknowledgment statement
    acknowledgments = [
        f" True",
        f" False",
    ]
    acknowledgment = random.choice(acknowledgments)
    
    return { "Glaucoma": acknowledgment}
