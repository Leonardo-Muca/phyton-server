from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.item_routes import router as item_routes

app = FastAPI(
    title="Techno Server",
    version="1.0.0"
)

# ==============================
# 🔥 CONFIGURACIÓN DE CORS
# ==============================
origins = [
    "http://localhost:3000",      # tu app React local
    "http://127.0.0.1:3000",
    "*",                          # si quieres permitir todo (útil en desarrollo)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],          # GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],          # headers permitidos
)

# ==============================

@app.get("/")
def root():
    return {"message": "API Python estructurada funcionando"}

app.include_router(item_routes)
