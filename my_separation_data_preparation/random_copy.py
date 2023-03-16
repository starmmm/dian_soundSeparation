import os
import random
import numpy as np
import argparse
import logging
import soundfile as sf
import tqdm
import shutil


if __name__ == '__main__':

    origin_path = "/home/cwc2022/soundSeparate/data/data_resample/bird_resample"
    copy_path = "/data01/cwc/mix_3/car_fs8k"
    wav_list = []
    for root, _, files in os.walk(origin_path):
        for file in files:
            if file.endswith('WAV') or file.endswith('wav'):
                wavFile = os.path.join(root, file)
                wav_list.append(wavFile)
    random.shuffle(wav_list)
    for i in range(200):
        shutil.copy(wav_list[i],copy_path)

                    




