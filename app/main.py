from fastapi import FastAPI
from ask import router as ask_router

app = FastAPI(title="AI BigData Chat")

# Daftarkan route /ask
app.include_router(ask_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
