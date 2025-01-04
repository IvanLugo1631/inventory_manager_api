from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .src.routers import product, inventory, store


app = FastAPI(
    title="Inventory Management API",
    description="API for managing products and inventory",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    # TODO:Need to adjust this in production to only allow specific origins
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(product.router)
app.include_router(inventory.router)
app.include_router(store.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Inventory Management API"}