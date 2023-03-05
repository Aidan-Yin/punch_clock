import os
import json
import time
from shutil import copyfile

data_file_name = 'data.json'
def store(date,content):
    frame = [date,content]
    data = []
    if os.path.exists(data_file_name):
        with open(data_file_name,'r') as f:
            fileread = f.read()
            if fileread:
                data = json.loads(fileread)
    data.append(frame)
    with open(data_file_name,'w') as f:
        f.write(json.dumps(data))

def getlastdate():
    time.sleep(0.01) # 避免上一帧数据还没保存好读错
    if not os.path.exists(data_file_name):
        return None
    with open(data_file_name,'r') as f:
        fileread = f.read()
        if not fileread:
            return None
        data = json.loads(fileread)
    return data[-1][0]

def getdata():
    time.sleep(0.01) # 避免上一帧数据还没保存好读错
    if not os.path.exists(data_file_name):
        return None
    with open(data_file_name,'r') as f:
        fileread = f.read()
        if not fileread:
            return None
        data = json.loads(fileread)
    return data

def save(data,backup=True):
    if backup:
        if not os.path.exists('./backups'):
            os.mkdir('./backups')
        copyfile(data_file_name,'./backups/'+data_file_name+str(time.time()))
    with open(data_file_name,'w') as f:
        f.write(json.dumps(data))