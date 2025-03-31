from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware
#from fastapi.staticfiles import StaticFiles

app = FastAPI()

#app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

project = "/app/data.json"

@app.get("/data")
def get_data():
    try:
        with open(project, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except Exception as e:
        return{"Ha ocurrido un error": str(e)}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

