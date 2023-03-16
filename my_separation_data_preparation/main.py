import os
import random
import numpy as np
import argparse
import logging
import soundfile as sf
from activlev import activlev
import tqdm
from test1_mydata import CreateFiles
from test2_mydata import GenerateMixAudio
from test3_mydata import GenrateCroValScp, GenrateTestScp, GenrateTrainScp


if __name__ == '__main__':
    output_dir = "/data01/cwc/dataset_mix3"
    state = "train"
    nums_file = 1000
    test_num = 100
    useActive = False
    input_dir_transformer = "/home/cwc2022/soundSeparate/data/data_resample/transformer_resample"
    input_dir_bird = "/home/cwc2022/soundSeparate/data/data_resample/bird_resample"
    input_dir_others = "/data01/cwc/mix_3/car_fs8k"
    
    CreateFiles(input_dir_transformer, input_dir_others,
                output_dir, nums_file, state,test_num)
    print("create file down")
    dataPath = "/data01/cwc/dataset_mix3"
    GenerateMixAudio(dataPath, state, useActive)
    print("Generate MixAudio down")
    state = "test"
    CreateFiles(input_dir_transformer, input_dir_others,
                output_dir, nums_file, state,test_num)
    print("create file down")
    GenerateMixAudio(dataPath, state, useActive)
    print("Generate MixAudio down")
    GenrateTrainScp(dataPath)
    GenrateTestScp(dataPath)
    GenrateCroValScp(dataPath)
    print("all done")
