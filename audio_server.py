from flask import Flask, send_file, Response

app = Flask(__name__)

@app.route("/audio")
def audio():
    print(">>> /audio requested")
    return send_file("reminder.mp3", mimetype="audio/mpeg")


@app.route("/voice")
def voice():
    return Response(
"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Play>https://aversion-reissue-exodus.ngrok-free.dev/audio</Play>
</Response>
""",
        mimetype="text/xml"
    )


if __name__ == "__main__":
    app.run(port=5001)