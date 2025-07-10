from kokoro import KPipeline
import soundfile as sf
import numpy as np
import torch
from pathlib import Path

path_audios = Path(__file__).parent / 'audios'

lang_code = 'p'
voices = ['pm_santa', 'pf_dora', 'pm_alex']

pipeline = KPipeline(lang_code=lang_code)

def text_to_speech(text, voice, audio_path):

    generator = pipeline(text, voice=voice)

    audio_chunks = []

    for gs, ps, audio in generator:
        audio_chunks.append(audio)

    audio = np.concatenate(audio_chunks)
    path_audio = path_audios / f'{audio_path}.wav'
    sf.write(path_audio, audio, 24000)

if __name__ == '__main__':
    
    text = '''
Olá, Professor Sandeco!
Soubemos que o senhor está em recuperação. Queria apenas mandar uma mensagem rápida para desejar melhoras e dizer para o senhor não se preocupar com nada das aulas. Foque em descansar e se sentir bem logo! Estamos na torcida pela sua saúde.
Abraço e se cuide!
'''
    for v in voices:
        text_to_speech(text, v, v)

