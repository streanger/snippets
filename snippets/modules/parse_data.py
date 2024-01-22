import re
import subprocess
from pathlib import Path


def extract_png_images(data: bytes):
    """parse bytes to find png images based on magic bytes
    we assume that images occurs one by one
    
    :param data: data to analyze
    :type data: bytes
    """
    def find_indexes(sub, s):
        indexes = [m.start() for m in re.finditer(sub, s)]
        return indexes

    png_start_bytes = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
    png_stop_bytes = b'\x49\x45\x4E\x44\xAE\x42\x60\x82'
    start_indexes = find_indexes(png_start_bytes, data)
    stop_indexes = find_indexes(png_stop_bytes, data)
    images = []
    for (begin, end) in zip(start_indexes, stop_indexes):
        img = data[begin:end+8]
        images.append(img)
    return images


def strings_subprocess(path, n=4):
    """
    get strings from specified file(path) using external strings tool
    strings must be present in system

    :param path: path to file
    :type path: str

    :param n: minimal number of characters
    :type n: int
    """
    command = ['strings', '-nobanner', '-n', str(n), path]
    response = subprocess.getoutput(command)
    out = response.splitlines()
    return out


def strings(data: bytes=None, path: str=None, n=4):
    """
    get strings from specified data or file(path)

    :param data: data to get strings from
    :type data: bytes

    :param path: path to file
    :type path: str

    :param n: minimal number of characters
    :type n: int

    https://catonmat.net/my-favorite-regex
    """
    if (data is None) and (path is None):
        raise Exception('neither data or path specified')
    elif (data is not None) and (path is not None):
        raise Exception('specify data or path, not both')
    elif (type(data) is bytes) and (path is None):
        pass
    elif (data is None) and (type(path) is str):
        data = Path(path).read_bytes()
    else:
        raise Exception('wrong type of params specified, use help(strings)')
    out = [item for item in re.findall(b'[ -~]+', data) if len(item) >= n]
    return out


if __name__ == "__main__":
    # TODO: add tests
    pass
