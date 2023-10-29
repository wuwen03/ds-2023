import numpy as np
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import TensorDataset,DataLoader
from torch import optim

import os

def classes_txt(root, out_path, num_class=None):
    # 创建一个存储文件夹名称的列表
    dirs = os.listdir(root)  # 列出根目录下所有类别所在文件夹名 # root目录下——test文件夹——有3755个文件夹
    if not num_class:		# 不指定类别数量就读取所有.不指定的时候num_class为空
        num_class = len(dirs)

    if not os.path.exists(out_path): # 输出文件路径不存在就新建
        f = open(out_path, 'w')      # 以“W”的方式在指定路径【out_path】创建一个输出文件。例如C:\\pytorch\\try.py
        f.close()
# 如果文件中本来就有一部分内容，只需要补充剩余部分
# 如果文件中数据的类别数比需要的多就跳过
    with open(out_path, 'r+') as f:  # 打开输出txt文件
        try:
            end = int(f.readlines()[-1].split('\\')[-2]) + 1
            # 读取txt文件所有行————取最后一行————以【/】为标志切割并取倒数第二个字符串——取整加一（因为文件是从0开始的）
        except:
            end = 0
        if end < num_class - 1:
            dirs.sort()  # 对列表的对象[text文件夹下的3755个数据集文件夹名称]进行排序（没有返回值）
            dirs = dirs[end:num_class]   # 取排序之后的前num_class个数据作为新列表（）
            for dir in dirs:    # [00000,....,00099](假设num_class为100个)（一个00000文件夹包含一个汉字的多个图片数据集）
                files = os.listdir(os.path.join(root, dir))   # 生成{一个汉字对应多张图片}名称的【列表】
                # 路径拼接成：C:\\pytorch\\writing\\HWDB1\\test/00000,也就是会自动加一个【/】.
                for file in files:  # 取单张图片的名称——对于图片文件会有【.png】后缀，文件夹则无后缀。
                    f.write(os.path.join(root, dir, file) + '\n')  # 将单张图片的路径信息写入txt文件，并换行

class VGG(torch.Module):
    def __init__(self) -> None:
        super().__init__()
        self.cov3_64=torch.nn.Sequential(
            nn.Conv2d()
        )