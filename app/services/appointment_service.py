from app.models.appointment import Appointment

appointments = []

def book_appointment(patient, doctor, date):
    appointments.append(Appointment(patient, doctor, date))
    return f"Appointment booked for {patient} with Dr. {doctor} on {date}"
