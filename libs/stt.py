import os
import subprocess
import wave
import json
from vosk import Model, KaldiRecognizer, SetLogLevel
import shutil
SetLogLevel(-1)
def stt_work(file, id='tmp'):
    subprocess.call(['utils/ffmpeg', '-y', '-i', f'tmp/{file}.oga', f'tmp/{file}.wav'])
    wf = wave.open(f'tmp/{file}.wav', "rb")

    model = Model(model_name="vosk-model-small-ru-0.22")


    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    rec.SetPartialWords(True)

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            ...
    return json.loads(rec.Result())['text']


def clear_tmp(file, id='tmp'):
    if os.path.isdir(f'voices/{id}'):
        shutil.copy2(f'tmp/{file}.wav', f'voices/{id}/{file}.wav')
    else:
        os.mkdir(f'voices/{id}')
        shutil.copy2(f'tmp/{file}.wav', f'voices/{id}/{file}.wav')
    os.remove(f'tmp/{file}.wav')
    os.remove(f'tmp/{file}.oga')

