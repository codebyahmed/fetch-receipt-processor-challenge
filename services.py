from models import Receipt
import threading
import math

receipt_points_db = {}
db_lock = threading.Lock()


def process_receipt_service(receipt_id: str, receipt: Receipt) -> None:
    points: int = 0

    # One point for every alphanumeric character in the retailer name.
    for c in receipt.retailer:
        if c.isalnum():
            points += 1

    # 50 points if the total is a round dollar amount with no cents.
    if receipt.total.endswith(".00"):
        points += 50

    # 25 points if the total is a multiple of 0.25.
    if float(receipt.total) % 0.25 == 0:
        points += 25

    # 5 points for every two items on the receipt.
    points += len(receipt.items) // 2 * 5

    # If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2
    # and round up to the nearest integer. The result is the number of points earned.
    item_points: int = 0
    for item in receipt.items:
        if len(item.shortDescription.strip()) % 3 == 0:
            item_points += math.ceil(float(item.price) * 0.2)
    points += item_points

    # 6 points if the day in the purchase date is odd.
    if receipt.purchaseDate.day % 2 != 0:
        points += 6

    # 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    if 14 <= receipt.purchaseTime.hour < 16:
        points += 10

    with db_lock:
        receipt_points_db[receipt_id] = points


def get_receipt_points_service(receipt_id: str) -> int:
    return receipt_points_db.get(receipt_id, -1)
