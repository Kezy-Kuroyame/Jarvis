from speechkit import Session, ShortAudioRecognition
import speech_recognition as sr
import wave


# Yandex SpeechKit
# oauth_token = 'y0_AgAAAAAfq-BCAATuwQAAAADdsREaEr0PDjebRducWEdLlXWIST7IlnM'
# folder_id = 'b1guqdbqvjqtpd8koeq8'
# oauth_session = Session.from_yandex_passport_oauth_token(oauth_token, folder_id)
# recognizeShortAudio = ShortAudioRecognition(oauth_session)
#
#
# async def recognition(audio):
#     return recognizeShortAudio.recognize(audio, format='lpcm', sampleRateHertz='48000')


async def recognition(audio):
    f = wave.open('auido_recognition_sample.wav', 'wb')
    f.setparams([2, 2, 48000, 0, 'NONE', 'not compressed'])
    f.writeframesraw(audio)
    f.close()
    r = sr.Recognizer()
    with sr.WavFile('auido_recognition_sample.wav') as source:
        audio_file = r.record(source)
    return r.recognize_google(audio_file, language="ru_RU", show_all=True)['alternative'][0]['transcript']


