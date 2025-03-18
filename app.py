import uuid
from fastapi import FastAPI, Request, status, Path, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from models import Receipt, ReceiptPoints, ReceiptId
from services import process_receipt_service, get_receipt_points_service

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Ahmed's Receipt Processor API"}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    if request.url.path == "/receipts/process":
        return JSONResponse(
            status_code=400, content={"message": "The receipt is invalid."}
        )
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@app.post(
    "/receipts/process",
    response_model=ReceiptId,
    responses={
        400: {
            "description": "The receipt is invalid",
            "content": {
                "application/json": {"example": {"message": "The receipt is invalid."}}
            },
        }
    },
)
async def process_receipt(receipt: Receipt) -> Response:
    receipt_id = str(uuid.uuid4())
    process_receipt_service(receipt_id, receipt)
    return {"id": receipt_id}


@app.get(
    "/receipts/{id}/points",
    response_model=ReceiptPoints,
    responses={
        404: {
            "description": "Receipt not found",
            "content": {
                "application/json": {
                    "example": {"message": "No receipt found for that ID."}
                }
            },
        }
    },
)
async def get_receipt_points(
    id: str = Path(
        ..., description="ID of the receipt to retrieve points for", pattern="^\\S+$"
    ),
) -> Response:
    points = get_receipt_points_service(id)
    if points >= 0:
        return {"points": points}
    return JSONResponse(
        status_code=404, content={"message": "No receipt found for that ID."}
    )
