import os
import elevenlabs
import random 

elevenlabs.set_api_key(os.environ["ELEVENLABS_TOKEN"])

voice_ids = [
    "pNInz6obpgDQGcFmaJgB",
    "ErXwobaYiN019PkySvjV",
    "VR6AewLTigWG4xSOukaG",
    "EXAVITQu4vr4xnSDxMaL",
    "N2lVS1w4EtoT3dr4eOWO",
    "IKne3meq5aSn9XLyUdCD",
    "XB0fDUnXU5powFXDhCwa",
    "2EiwWnXFnvU5JabPnv8n",
    "onwK4e9ZLuTAKqWW03F9",
    "CYw3kZ02Hs0563khs1Fj",
    "AZnzlk1XvdvUeBnXmlld",
    "ThT5KcBeYPX3keUQqHPh",
    "MF3mGyEYCl7XYWbV9V6O",
    "LcfcDJNUP1GQjkzn1xUU",
    "g5CIjZEefAph4nQFvHAz",
    "D38z5RcWu1voky8WS1ja",
    "jsCqWAovK2LkecY7zXl4",
    "jBpfuIE2acCO8z3wKNLl",
    "zcAOhNBS3c14rBihAFp1",
    "z9fAnlkpzviPz146aGWa",
    "oWAxZDx7w5VEj9dCyTzz",
    "SOYHLrjzK2X1ezoPC6cr",
    "ZQe5CZNOzWyzPSCn5a3c",
    "bVMeCyTHy58xNoL34h3p",
    "t0jbNlBVZ17f02VDIeMI",
    "Zlb1dXrM653N07WRdFW3",
    "TxGEqnHWrfWFTfGW9XjX",
    "TX3LPaxmHKxFdv7VOQHJ",
    "XrExE9yKIg1WjnnlVkGX",
    "Yko7PKHZNXotIFUBG7I9",
    "flq6f7yk4E4fJM5XTYuZ",
    "zrHiDhphv9ZnVXBqCLjz",
    "piTKgcLEGmPE4e6mEKli",
    "ODq5zmih8GrVes37Dizd",
    "21m00Tcm4TlvDq8ikWAM",
    "wViXBPUzp2ZZixB1xQuM",
    "yoZ06aMxZJJ28mfd3POQ",
    "pMsXgVXv3BLzUgSXRplE",
    "GBv7mTt0atIp3Br8iCZE"
]


def synt_voice(text, name):
    voice = elevenlabs.Voice(
        voice_id = random.choice(voice_ids),
        settings = elevenlabs.VoiceSettings(
            stability = 0, # 0 stability sound best to me. Other settins shows no effect on the voice
            similarity_boost = 0.75,
            style = 0,
            use_speaker_boost = True
        )
    )
    audio = elevenlabs.generate( 
        text = text,
        voice = voice
    )
    
    elevenlabs.save(audio, f"../src/voices/{name}.mp3")


synt_voice("hello, this is fucking awesome. Why didn't I find it sooner!", "0001")
