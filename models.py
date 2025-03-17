from pydantic import BaseModel, Field
from typing import List
from datetime import date, time


class Item(BaseModel):
    shortDescription: str = Field(
        description="The Short Product Description for the item.",
        pattern="^[\\w\\s\\-]+$",
        example="Mountain Dew 12PK",
    )
    price: str = Field(
        description="The total price paid for this item.",
        pattern="^\\d+\\.\\d{2}$",
        example="6.49",
    )


class Receipt(BaseModel):
    retailer: str = Field(
        description="The name of the retailer or store the receipt is from.",
        pattern="^[\\w\\s\\-&]+$",
        example="M&M Corner Market",
    )
    purchaseDate: date = Field(
        description="The date of the purchase printed on the receipt.",
        example="2022-01-01",
    )
    purchaseTime: time = Field(
        description="The time of the purchase printed on the receipt. 24-hour time expected.",
        example="13:01",
    )
    items: List[Item] = Field(description="The list of items purchased.", min_length=1)
    total: str = Field(
        description="The total amount paid on the receipt.",
        pattern="^\\d+\\.\\d{2}$",
        example="6.49",
    )