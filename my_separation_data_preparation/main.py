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
    nums_file = 1000  #每个背景噪声训练集生成文件数量 ，如这里有两个，总共生成2000条训练集（每种1000条）
    test_num = 100 #每个背景噪声测试集生成文件数量 ，如这里有两个，总共生成200条训练集
    useActive = False #有bug，暂时没用
    input_dir_transformer = "/home/cwc2022/soundSeparate/data/data_resample/transformer_resample" #变压器数据集文件位置
    # # input_dir_bird = "/home/cwc2022/soundSeparate/data/data_resample/bird_resample"
    # input_dir_others = "/data01/cwc/mix_3/car_fs8k"
    input_dir_others = ["/home/cwc2022/soundSeparate/data/data_resample/bird_resample", "/data01/cwc/mix_3/car_fs8k"]  #每个背景噪声的数据集作为list的一个元素
    
    CreateFiles(input_dir_transformer, input_dir_others,
                output_dir, nums_file, state,test_num) #产生txt文件记录每次混合的音频位置及随机信噪比
    print("create file down")
    dataPath = "/data01/cwc/dataset_mix3"
    GenerateMixAudio(dataPath, state, useActive) # 混合音频
    print("Generate MixAudio down")
    state = "test"
    CreateFiles(input_dir_transformer, input_dir_others,
                output_dir, nums_file, state,test_num) #产生txt文件记录每次混合的音频位置及随机信噪比
    print("create file down")
    GenerateMixAudio(dataPath, state, useActive) # 混合音频
    print("Generate MixAudio down")
    GenrateTrainScp(dataPath) #产生scp文件，我们暂时不需要
    GenrateTestScp(dataPath)
    GenrateCroValScp(dataPath)
    print("all done")
