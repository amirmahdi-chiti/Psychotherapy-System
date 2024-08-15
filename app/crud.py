from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas
from app.utils import generate_otp, send_otp_via_email, verify_otp
import pyotp
from datetime import datetime, timedelta

# Doctor CRUD operations
async def get_doctor(db: AsyncSession, doctor_id: int):
    result = await db.execute(select(models.Doctor).filter(models.Doctor.id == doctor_id))
    return result.scalars().first()

async def get_doctor_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(models.Doctor).filter(models.Doctor.email == email))
    return result.scalars().first()

async def create_doctor(db: AsyncSession, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(email=doctor.email, name=doctor.name, password=doctor.password)
    db.add(db_doctor)
    await db.commit()
    await db.refresh(db_doctor)
    return db_doctor

# Patient CRUD operations
async def get_patients(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Patient).offset(skip).limit(limit))
    return result.scalars().all()

async def get_patient(db: AsyncSession, patient_id: int):
    result = await db.execute(select(models.Patient).filter(models.Patient.id == patient_id))
    return result.scalars().first()

async def create_patient(db: AsyncSession, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    await db.commit()
    await db.refresh(db_patient)
    return db_patient

async def update_patient(db: AsyncSession, patient_id: int, patient: schemas.PatientCreate):
    db_patient = await get_patient(db, patient_id)
    if not db_patient:
        return None
    for key, value in patient.dict().items():
        setattr(db_patient, key, value)
    await db.commit()
    await db.refresh(db_patient)
    return db_patient

async def delete_patient(db: AsyncSession, patient_id: int):
    db_patient = await get_patient(db, patient_id)
    if not db_patient:
        return None
    await db.delete(db_patient)
    await db.commit()
    return db_patient

# Appointment CRUD operations
async def get_appointments(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Appointment).offset(skip).limit(limit))
    return result.scalars().all()

async def get_appointment(db: AsyncSession, appointment_id: int):
    result = await db.execute(select(models.Appointment).filter(models.Appointment.id == appointment_id))
    return result.scalars().first()

async def get_appointments_for_doctor(db: AsyncSession, doctor_id: int):
    result = await db.execute(select(models.Appointment).filter(models.Appointment.doctor_id == doctor_id))
    return result.scalars().all()

async def get_appointments_for_patient(db: AsyncSession, patient_id: int):
    result = await db.execute(select(models.Appointment).filter(models.Appointment.patient_id == patient_id))
    return result.scalars().all()

async def create_appointment(db: AsyncSession, appointment: schemas.AppointmentCreate):
    # Ensure the appointment is 30 minutes long
    start_time = appointment.time
    end_time = (datetime.combine(datetime.min, start_time) + timedelta(minutes=30)).time()
    db_appointment = models.Appointment(**appointment.dict(), end_time=end_time, status="Confirmed")
    db.add(db_appointment)
    await db.commit()
    await db.refresh(db_appointment)
    return db_appointment

async def update_appointment(db: AsyncSession, appointment_id: int, appointment: schemas.AppointmentCreate):
    db_appointment = await get_appointment(db, appointment_id)
    if not db_appointment:
        return None
    for key, value in appointment.dict().items():
        setattr(db_appointment, key, value)
    await db.commit()
    await db.refresh(db_appointment)
    return db_appointment

async def delete_appointment(db: AsyncSession, appointment_id: int):
    db_appointment = await get_appointment(db, appointment_id)
    if not db_appointment:
        return None
    await db.delete(db_appointment)
    await db.commit()
    return db_appointment

# FreeTime CRUD operations
async def get_free_times_for_doctor(db: AsyncSession, doctor_id: int):
    # Get all free times for the doctor
    result = await db.execute(select(models.FreeTime).filter(models.FreeTime.doctor_id == doctor_id))
    free_times = result.scalars().all()

    # Get all appointments for the doctor
    appointments_result = await db.execute(select(models.Appointment).filter(models.Appointment.doctor_id == doctor_id))
    appointments = appointments_result.scalars().all()

    # Filter out the free times that overlap with existing appointments
    available_free_times = []
    for free_time in free_times:
        is_available = True
        for appointment in appointments:
            if (appointment.date == free_time.date and
                    ((free_time.start_time <= appointment.time < free_time.end_time) or
                     (free_time.start_time < (datetime.combine(datetime.min, appointment.time) + timedelta(minutes=30)).time() <= free_time.end_time))):
                is_available = False
                break
        if is_available:
            available_free_times.append(free_time)

    return available_free_times

async def create_free_time(db: AsyncSession, free_time: schemas.FreeTimeCreate):
    db_free_time = models.FreeTime(**free_time.dict())
    db.add(db_free_time)
    await db.commit()
    await db.refresh(db_free_time)
    return db_free_time

async def delete_free_time(db: AsyncSession, free_time_id: int):
    db_free_time = await db.get(models.FreeTime, free_time_id)
    if not db_free_time:
        return None
    await db.delete(db_free_time)
    await db.commit()
    return db_free_time

# OTP operations
async def send_otp(db: AsyncSession, email: str):
    doctor = await get_doctor_by_email(db, email=email)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    secret = pyotp.random_base32()
    otp = generate_otp(secret)
    send_otp_via_email(email, otp)

    doctor.otp_secret = secret
    await db.commit()
    return {"message": "OTP sent"}

async def verify_otp(db: AsyncSession, email: str, otp: str):
    doctor = await get_doctor_by_email(db, email=email)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    if not doctor.otp_secret:
        raise HTTPException(status_code=400, detail="OTP not generated")

    if not verify_otp(doctor.otp_secret, otp):
        raise HTTPException(status_code=400, detail="Invalid OTP")

    doctor.otp_secret = None
    await db.commit()
    return {"message": "OTP verified"}
