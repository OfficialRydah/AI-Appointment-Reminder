import pandas as pd

FILE_NAME = "appointments.xlsx"


def read_appointments():
    return pd.read_excel(FILE_NAME)


def add_appointment(client_name, date, phone_number, appointment_time, service):

    df = pd.read_excel(FILE_NAME)

    new_row = {
        "Client_Name": client_name,
        "Date": date,
        "Phone_Number": phone_number,
        "Appointment_Time": appointment_time,
        "Service": service,
        "Status": "Pending"
    }

    df.loc[len(df)] = new_row

    df.to_excel(FILE_NAME, index=False)

    print("Appointment Added Successfully!")


def update_status(client_name, status):

    df = pd.read_excel(FILE_NAME)

    df.loc[
        df["Client_Name"] == client_name,
        "Status"
    ] = status

    df.to_excel(FILE_NAME, index=False)

    print("Status Updated!")


def mark_as_reminded(client_name):

    df = pd.read_excel(FILE_NAME)

    df.loc[
        df["Client_Name"] == client_name,
        "Status"
    ] = "Reminded"

    df.to_excel(FILE_NAME, index=False)

    print(f"{client_name} marked as Reminded.")