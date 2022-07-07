import glob
from pathlib import Path
import os   
path = 'D:\\OBS\\GTA5\\edited\*.mp4'
files = glob.glob(path)
files.sort(key=os.path.getmtime)
for file in files:
    os.system(f'python VideoUploader.py --file="{file}" --title="{Path(file).stem}" --description="" --category="20" --privacyStatus="private"')