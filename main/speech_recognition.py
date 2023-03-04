from speechkit import Session, ShortAudioRecognition


oauth_token = 'y0_AgAAAAAfq-BCAATuwQAAAADdsREaEr0PDjebRducWEdLlXWIST7IlnM'
folder_id = 'b1guqdbqvjqtpd8koeq8'
oauth_session = Session.from_yandex_passport_oauth_token(oauth_token, folder_id)
recognizeShortAudio = ShortAudioRecognition(oauth_session)


async def recognition(audio):
    return recognizeShortAudio.recognize(audio, format='lpcm', sampleRateHertz='48000')
