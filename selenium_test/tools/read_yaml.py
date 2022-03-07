import os

import yaml
from config import BASE_PATH
def read_yaml(filename):
    file_path=BASE_PATH +os.sep +"data"+os.sep +filename
    arrs=[]
    with open(file_path,'r',encoding='utf-8') as f:
        for datas in yaml.safe_load(f).values():
            arrs.append(tuple(datas.values()))
    return arrs


