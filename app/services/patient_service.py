from app.models.patient import Patient

patients = []

def add_patient(name, age):
    patients.append(Patient(name, age))
