from fastapi import FastAPI
from users.endpoints import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="1.0.0.127", port=8000)
