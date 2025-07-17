from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.models.booking import BookingRequest
from app.services.email import EmailService
from app.services.database import get_db
from app.models.booking import Booking

router = APIRouter(prefix="/booking", tags=["booking"])

@router.post("/schedule")
async def schedule_interview(booking: BookingRequest):
    """Endpoint for scheduling interviews"""
    try:
        db = get_db()
        
        # Create booking record
        booking_record = Booking(
            full_name=booking.full_name,
            email=booking.email,
            date=booking.date,
            time=booking.time
        )
        db.add(booking_record)
        db.commit()
        
        # Send confirmation email
        email_service = EmailService()
        await email_service.send_confirmation_email(
            to_email=booking.email,
            full_name=booking.full_name,
            date=booking.date,
            time=booking.time
        )
        
        return JSONResponse(
            content={"message": "Interview scheduled successfully"},
            status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        db.rollback()
        return JSONResponse(
            content={"error": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )