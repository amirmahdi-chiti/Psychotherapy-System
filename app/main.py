from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas, crud
from app.database import engine, get_db
from typing import List
import contextlib

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/api/auth/register", response_model=schemas.Doctor)
async def register_doctor(doctor: schemas.DoctorCreate, db: AsyncSession = Depends(get_db)):
    db_doctor = await crud.get_doctor_by_email(db, email=doctor.email)
    if db_doctor:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await crud.create_doctor(db, doctor=doctor)

@app.post("/api/auth/login")
async def login(auth_request: schemas.AuthRequest, db: AsyncSession = Depends(get_db)):
    doctor = await crud.get_doctor_by_email(db, email=auth_request.email)
    if not doctor or doctor.password != auth_request.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"token": f"token_{doctor.id}"}

@app.get("/api/auth/profile", response_model=schemas.Doctor)
async def get_profile(token: str, db: AsyncSession = Depends(get_db)):
    doctor_id = int(token.split("_")[1])
    doctor = await crud.get_doctor(db, doctor_id=doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@app.post("/api/auth/send-otp", response_model=dict)
async def send_otp(request: schemas.OTPRequest, db: AsyncSession = Depends(get_db)):
    return await crud.send_otp(db, email=request.email)

@app.post("/api/auth/verify-otp", response_model=dict)
async def verify_otp(request: schemas.OTPVerify, db: AsyncSession = Depends(get_db)):
    return await crud.verify_otp(db, email=request.email, otp=request.otp)

@app.get("/api/patients", response_model=List[schemas.Patient])
async def read_patients(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    patients = await crud.get_patients(db, skip=skip, limit=limit)
    return patients

@app.get("/api/patients/{patient_id}", response_model=schemas.Patient)
async def read_patient(patient_id: int, db: AsyncSession = Depends(get_db)):
    patient = await crud.get_patient(db, patient_id=patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@app.post("/api/patients", response_model=schemas.Patient)
async def create_patient(patient: schemas.PatientCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_patient(db=db, patient=patient)

@app.put("/api/patients/{patient_id}", response_model=schemas.Patient)
async def update_patient(patient_id: int, patient: schemas.PatientCreate, db: AsyncSession = Depends(get_db)):
    db_patient = await crud.update_patient(db, patient_id=patient_id, patient=patient)
    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@app.delete("/api/patients/{patient_id}")
async def delete_patient(patient_id: int, db: AsyncSession = Depends(get_db)):
    db_patient = await crud.delete_patient(db, patient_id=patient_id)
    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Patient deleted"}

@app.get("/api/appointments", response_model=List[schemas.Appointment])
async def read_appointments(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    appointments = await crud.get_appointments(db, skip=skip, limit=limit)
    return appointments

@app.get("/api/appointments/doctor/{doctor_id}", response_model=List[schemas.Appointment])
async def read_appointments_for_doctor(doctor_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_appointments_for_doctor(db, doctor_id=doctor_id)

@app.get("/api/appointments/patient/{patient_id}", response_model=List[schemas.Appointment])
async def read_appointments_for_patient(patient_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_appointments_for_patient(db, patient_id=patient_id)

@app.post("/api/appointments", response_model=schemas.Appointment)
async def create_appointment(appointment: schemas.AppointmentCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_appointment(db=db, appointment=appointment)

@app.put("/api/appointments/{appointment_id}", response_model=schemas.Appointment)
async def update_appointment(appointment_id: int, appointment: schemas.AppointmentCreate, db: AsyncSession = Depends(get_db)):
    db_appointment = await crud.update_appointment(db, appointment_id=appointment_id, appointment=appointment)
    if not db_appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment

@app.delete("/api/appointments/{appointment_id}")
async def delete_appointment(appointment_id: int, db: AsyncSession = Depends(get_db)):
    db_appointment = await crud.delete_appointment(db, appointment_id=appointment_id)
    if not db_appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {"message": "Appointment deleted"}

# Add more endpoints for MedicalRecord, Message, Invoice, and appointment reservation as needed.
