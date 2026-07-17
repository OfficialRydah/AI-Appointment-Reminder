from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    print("Booking received!")
    print(data)

    return jsonify({"message": "Success"}), 200


if __name__ == "__main__":
    app.run(port=5000)



from flask import Flask, request, jsonify
from excel_db import add_appointment

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    add_appointment(
        data["Client_Name"],
        data["Date"],
        data["Phone_Number"],
        data["Appointment_Time"],
        data["Service"]
    )

    return jsonify({"message": "Appointment Saved"}), 200


if __name__ == "__main__":
    app.run(port=5000)