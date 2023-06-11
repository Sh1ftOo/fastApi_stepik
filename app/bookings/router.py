from typing import List

from fastapi import APIRouter

from app.bookings.dao import BookingDao
from app.bookings.schemas import BookingSchema

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
async def get_bookings() -> List[BookingSchema]:
    return await BookingDao.find_all()


@router.get("/{booking_id}")
def get_booking(booking_id):
    pass