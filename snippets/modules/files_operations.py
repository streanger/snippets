import sys
import os
import json
from pathlib import Path
# TODO: read_bin, write_bin


def script_path():
    """set current path, to script path"""
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def script_path():
    """set current path, to script path"""
    current_path = str(Path(__file__).parent)
    os.chdir(current_path)
    return current_path
    
    
def write_json(filename, data):
    """write to json file"""
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(data, fp, sort_keys=True, indent=4, ensure_ascii=False)
    return True
    
    
def read_json(filename):
    """read json file to dict"""
    data = {}
    try:
        with open(filename, encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print('[x] FileNotFoundError: {}'.format(filename))
    return data
    
    
def read_text_file(filename):
    """read text file using Path"""
    return Path(filename).read_text()
    
    
def write_file(filename, text, mode='w'):
    """write to file"""
    try:
        with open(filename, mode, encoding='utf-8') as f:
            f.write(text)
    except Exception as err:
        print('[x] Failed to write to file: {}, err: {}'.format(filename, err))
    return None
    
    
def read_file(filename):
    """read from file"""
    content = ''
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print('[x] FileNotFoundError: {}'.format(filename))
    return content
    
    
def write_bin(filename, data):
    """write to binary file"""
    with open(filename, 'wb') as f:
        f.write(data)
    return True
    
    
def read_bin(filename):
    """read from binary file"""
    with open(filename, "rb") as f:
        data = f.read()
    return data
    
    
def list_directory_files(directory):
    """https://stackoverflow.com/questions/9816816/get-absolute-paths-of-all-files-in-a-directory"""
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))
            
            
def list_directory_files(directory):
    """https://stackoverflow.com/questions/9816816/get-absolute-paths-of-all-files-in-a-directory"""
    for filepath in Path(directory).glob('**/*'):
        if filepath.is_dir():
            continue
        yield str(filepath.absolute())
        
        
if __name__ == "__main__":
    pass
    script_path()
    test = read_text_file('TEST.txt')
    print(test)
    