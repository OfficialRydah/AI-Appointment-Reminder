from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from excel_db import read_appointments, mark_as_reminded
from ai_agent import generate_reminder
from tts_engine import generate_audio
from voice import make_call


def check_appointments():

    print("\nChecking appointments...")
    print("Current time:", datetime.now())

    appointments = read_appointments()

    # Only appointments that haven't been reminded
    appointments = appointments[
        appointments["Status"] == "Pending"
    ]

    if appointments.empty:
        print("No pending appointments.")
        return

    for _, row in appointments.iterrows():

        reminder = generate_reminder(row)

        print(reminder)

        phone = str(row["Phone_Number"]).strip()

        if not phone.startswith("+"):
            if phone.startswith("0"):
                phone = "+234" + phone[1:]
            else:
                phone = "+234" + phone

        print("Calling:", row["Client_Name"])
        print("Phone:", phone)

        try:

            generate_audio(reminder)

            make_call(
                row["Client_Name"],
                phone
            )

            mark_as_reminded(
                row["Client_Name"]
            )

        except Exception as e:
            print("Error:", e)


scheduler = BlockingScheduler()

scheduler.add_job(
    check_appointments,
    "interval",
    minutes=30
)

print("AI Receptionist Started...")
print("Checking every 30 minutes...\n")

check_appointments()

scheduler.start()