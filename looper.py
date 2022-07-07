import glob
from pathlib import Path
import os
import time
path = 'D:\\OBS\\GTA5\\edited\*.mp4'
files = glob.glob(path)
files.sort(key=os.path.getmtime)
for file in files:
    os.system(f'python VideoUploader.py --file="{file}" --title="{Path(file).stem}" --description="" --category="20" --privacyStatus="private"')
    os.rename(file,os.path.join('D:\\OBS\\GTA5\\tempupload',os.path.basename(file)))
    print('Waiting 10 seconds...')
    time.sleep(10)