import sys
import os
import zipfile
import shutil


def script_path():
    """set current path, to script path"""
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path


def zipdir(path, ziph):
    """zip directory using zipfile

    https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory
    ziph is zipfile handle. Example use case:
    with zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir('tmp/', zipf)
    """
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(
                os.path.join(root, file),
                os.path.relpath(os.path.join(root, file), os.path.join(path, "..")),
            )
    return None


def shutil_zipdir():
    """zip directory using shutil

    https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory
    use it as oneliner
    """
    shutil.make_archive("out.zip", "zip", directory)
    return None


if __name__ == "__main__":
    script_path()
    directory = "files/"

    # zipfile
    with zipfile.ZipFile("zipfile_out.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
        zipdir(directory, zipf)

    # shutil
    shutil.make_archive("shutil_out.zip", "zip", directory) 
