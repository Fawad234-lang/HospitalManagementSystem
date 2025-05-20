from app.models.doctor import Doctor

doctors = []

def add_doctor(name, specialty):
    doctors.append(Doctor(name, specialty))
