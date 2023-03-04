import speechkit

recognizeShortAudio = ShortAudioRecognition(session)


async def recognition(audio):
    recognized_text = recognizeShortAudio.recognize(audio)
