import json
import re
import database
from itertools import groupby

replace_dict = {
    'y':'引体向上pull-ups',
    'f':'俯卧撑push-ups',
    'd':'单力臂single',
    's':'双力臂double',
    'l':'篮球basketball',
    'p':'跑步jog',
    'j':'卷腹crunch',
    'z':'杂mix',
    'e':'俄罗斯转体Russian_twist',
    'h':'核心core',
    'c':'超人式superman',
    'sb':'散步walk',
    'sf':'上斜俯卧撑high-pose_push-ups',
    'ds':'登山者climber',
    'pp':'乒乓球pingpong',
    'dc':'单车bike',
    'ym':'羽毛球badminton',
    'sd':'深蹲squat',
    'DSBF':'did_something_but_forget'
}

def transformer(content_string):
    items = content_string.split(',')
    new = []
    for item in items:
        if not item:
            continue
        s = [''.join(list(g)) for k, g in groupby(item, key=lambda x: x.isdigit())] # from https://blog.csdn.net/qq_24671941/article/details/84071960
        type_name = replace_dict.get(s[0])
        if type_name:
            s[0] = type_name
        ss = ''.join(s)
        new.append(ss)
    return ','.join(new)
        
data_file_name = 'data.json'

if __name__=='__main__':
    data = database.getdata()
    for id,i in enumerate(data):
        data[id][1] = transformer(i[1])
    database.save(data)