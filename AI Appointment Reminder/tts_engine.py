import asyncio
import edge_tts

VOICE = "en-US-AriaNeural"


async def create_audio(text):
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )

    await communicate.save("reminder.mp3")


def generate_audio(text):
    asyncio.run(create_audio(text))
    print("Audio Created Successfully!")