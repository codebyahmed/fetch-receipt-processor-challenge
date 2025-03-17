from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Ahmed's Receipt Processor API"}


@app.post("/receipts/process")
async def process_receipt():
    return {"message": "Process receipt"}


@app.get("/receipts/{id}/points")
async def get_receipt_points(id: str):
    return {"message": f"Get points for receipt {id}"}