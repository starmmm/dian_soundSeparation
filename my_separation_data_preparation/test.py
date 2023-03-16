import os
import random
import numpy as np
import argparse
import logging
import soundfile as sf
import tqdm
import shutil


if __name__ == '__main__':


    for i in range(9):
        inputPath = "/data01/cwc/urban8k/UrbanSound8K/audio/fold"+str(i+1)
        outputPath = "/data01/cwc/urban8k/UrbanSound8K/car"
        path1 = "/data01/cwc/urban8k/UrbanSound8K/car_fs8k"
        for root, _, files in os.walk(path1):
            for file in files:
                if file.endswith('WAV') or file.endswith('wav'):
                    wavFile = os.path.join(root, file)
                    s1_16k, fs = sf.read(wavFile)
                    print(s1_16k.size)
                    




