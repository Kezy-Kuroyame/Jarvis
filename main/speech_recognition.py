from speechkit import ShortAudioRecognition

recognizeShortAudio = ShortAudioRecognition(session)


async def recognition(audio):
    recognized_text = recognizeShortAudio.recognize(audio)
