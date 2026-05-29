from fastapi import FastAPI, HTTPException, status
from app.models import AppointmentCreate, AppointmentUpdate

app = FastAPI(
    title="Clinic Appointment API",
    description="A simple API for managing clinic appointments.",
    version="1.0.0"
)

appointments = {}
next_id = 1

@app.get("/")
def read_root():
    return{
        "message": "Welcome to the Clinic Appointment API",
        "docs": "/docs"
    }

@app.get("/appointments")
def get_appointments():
    return{
        "count": len(appointments),
        "appointments": appointments
    }

@app.get("/appointments/{appointment_id}")
def get_appointment(appointment_id: int):
    if appointment_id not in appointments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found"
        )
    return appointments[appointment_id]

@app.post("/appointments", status_code=status.HTTP_201_CREATED)
def create_appointment(appointment: AppointmentCreate):
    global next_id

    new_appointment = {
        "id": next_id,
        "patient_name": appointment.patient_name,
        "doctor_name": appointment.doctor_name,
        "appointment_date": appointment.appointment_date,
        "appointment_time": appointment.appointment_time,
        "reason": appointment.reason,
        "status": "scheduled"
    }

    appointments[next_id] = new_appointment
    next_id += 1

    return{
        "message": "Appointment created successfully",
        "appointment": new_appointment
    }

@app.put("/appointments/{appointment_id}")
def update_appointment(appointment_id: int, appointment_update: AppointmentUpdate):
    if appointment_id not in appointments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found"
        )
    
    existing_appointment = appointments[appointment_id]
    update_data = appointment_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        existing_appointment[key] = value
    
    appointments[appointment_id] = existing_appointment

    return{
        "message": "Appointment updated successfully",
        "appointment": existing_appointment
    }

@app.delete("/appointments/{appointment_id}")
def cancel_appointment(appointment_id: int):
    if appointment_id not in appointments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found"
        )
    appointments[appointment_id]["status"] = "cancelled"

    return{
        "message": "Appointment cancelled successfully",
        "appointment": appointments[appointment_id]
    }

@app.get("/health")
def health_check():
    return {"status": "API is running"}

@app.get("/appointments/status/{status}")
def get_appointments_by_status(status: str):
    filtered = [
        appointment for appointment in appointments.values()
        if appointment["status"].lower() == status.lower()
    ]
    return {
        "count": len(filtered),
        "appointments": filtered
    }

@app.get("/appointments/doctor/{doctor_name}")
def get_appointments_by_doctor(doctor_name: str):
    filtered = [
        appointment for appointment in appointments.values()
        if appointment["doctor_name"].lower() == doctor_name.lower()
    ]
    return {
        "count": len(filtered),
        "appointments": filtered
    }

    