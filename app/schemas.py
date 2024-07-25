from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date

class DoctorBase(BaseModel):
    email: EmailStr
    name: str

class DoctorCreate(DoctorBase):
    password: str

class Doctor(DoctorBase):
    id: int

    class Config:
        from_attributes = True

class PatientBase(BaseModel):
    name: str
    dob: date
    contact_info: str
    medical_history: Optional[str] = None

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

    class Config:
        from_attributes = True

class AppointmentBase(BaseModel):
    doctor_id: int
    patient_id: int
    date: date
    time: str
    reason: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int
    status: str

    class Config:
        from_attributes = True

class MedicalRecordBase(BaseModel):
    patient_id: int
    record: str

class MedicalRecordCreate(MedicalRecordBase):
    pass

class MedicalRecord(MedicalRecordBase):
    id: int

    class Config:
        from_attributes = True

class MessageBase(BaseModel):
    recipient_id: int
    message: str

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int

    class Config:
        from_attributes = True

class InvoiceBase(BaseModel):
    patient_id: int
    amount: float
    description: str

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    id: int

    class Config:
        from_attributes = True

class AuthRequest(BaseModel):
    email: EmailStr
    password: str

class OTPRequest(BaseModel):
    email: EmailStr

class OTPVerify(BaseModel):
    email: EmailStr
    otp: str
