from excel_db import read_appointments


def generate_reminder(row):
    return (
        f"Hello {row['Client_Name']}. "
        f"This is your AI receptionist. "
        f"This is a reminder that you have a "
        f"{row['Service']} appointment on "
        f"{row['Date']} at {row['Appointment_Time']}. "
        f"We look forward to seeing you. "
        f"Thank you!"
    )