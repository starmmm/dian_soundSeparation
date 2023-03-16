import os
import soundfile as sf
import resampy

path = "/data01/cwc/urban8k/UrbanSound8K/car"
resamplePath = "/data01/cwc/urban8k/UrbanSound8K/car_fs8k"

i = 0
resample_fs = 8000
# a = os.path.exists(path)
for root, dirs, files in os.walk(path):
    for file in files:
        wavFile = os.path.join(root, file)
        s1_16k, fs = sf.read(wavFile)
        if s1_16k.size/fs/2 > 3:
            data = resampy.resample(s1_16k[:,0], fs, resample_fs )
            mix_out_name = os.path.join(resamplePath, "resample_{}".format(file))
            sf.write( mix_out_name, data, resample_fs , format='WAV', subtype='PCM_16')
            i = i+1
            print(i)
