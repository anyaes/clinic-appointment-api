from pydantic import BaseModel, Field
from typing import Optional

class AppointmentCreate(BaseModel):
    patient_name: str = Field(..., min_length=2,max_length=100)
    doctor_name: str = Field(..., min_length=2,max_length=100)
    appointment_date: str = Field(...,examples=["2026-06-15"])
    appointment_time: str = Field(
        ...,
        pattern=r"^([01]\d|2[0-3]):[0-5]\d$",
        examples=["09:30"]
    )
    reason: str = Field(...,min_length=3,max_length=255)

class AppointmentUpdate(BaseModel):
    patient_name: Optional[str] = Field(None, min_length=2, max_length=100)
    doctor_name: Optional[str] = Field(None, min_length=2, max_length=100)
    appointment_date: Optional[str] = Field(None, examples=["2026-06-15"])
    appointment_time: Optional[str] = Field(
        None,
        pattern=r"^([01]\d|2[0-3]):[0-5]\d$",
        examples=["09:30"]
    )
    reason: Optional[str] = Field(None, min_length=3, max_length=255)

