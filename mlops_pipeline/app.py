from fastapi import FastAPI, HTTPException
import tensorflow as tf
import numpy as np
import os
import uvicorn

app = FastAPI()

MODEL_PATH = "/model/model.keras"
model = tf.keras.models.load_model(MODEL_PATH) if os.path.exists(MODEL_PATH) else None

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Model Server"}

@app.get("/model-info")
def model_info():
    return {"model_path": MODEL_PATH, "model_loaded": model is not None}

@app.post("/predict")
def predict(input: dict):
    if model is None:
        raise HTTPException(status_code=500, detail="모델이 로드되지 않았습니다.")
    
    input_data = np.array(input["input"]).reshape(1, -1)
    prediction = model.predict(input_data)[0][0]
    return {"prediction": float(prediction)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
    

