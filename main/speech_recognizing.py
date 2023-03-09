from speechkit import Session, ShortAudioRecognition
import speech_recognition as sr
import wave
import os


# Yandex SpeechKit
# oauth_token = 'y0_AgAAAAAfq-BCAATuwQAAAADdsREaEr0PDjebRducWEdLlXWIST7IlnM'
# folder_id = 'b1guqdbqvjqtpd8koeq8'
# oauth_session = Session.from_yandex_passport_oauth_token(oauth_token, folder_id)
# recognizeShortAudio = ShortAudioRecognition(oauth_session)
#
#
# async def recognition(audio):
#     return recognizeShortAudio.recognize(audio, format='lpcm', sampleRateHertz='48000')


# Google Web Speech Recognition
async def recognition(audio):
    f = wave.open('recognition_sample.wav', 'wb')
    audio_params = [2, 2, 48000, 0, 'NONE', 'not compressed']
    f.setparams(audio_params)
    f.writeframesraw(audio)
    f.close()
    r = sr.Recognizer()
    with sr.WavFile('recognition_sample.wav') as source:
        audio_file = r.record(source)
    os.remove('recognition_sample.wav')
    return r.recognize_google(audio_file, show_all=True)['alternative'][0]['transcript']



