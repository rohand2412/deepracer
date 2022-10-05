import glob
import os
import tarfile
from s3_download_logs import remove

def main():
    for path in glob.glob("../**/Logs-*/model.tar.gz"):
        with tarfile.open(path) as f:
            f.extractall(os.path.join(os.path.dirname(path), "model.tar.gz-extracted"))
            print("extracted: {}".format(os.path.join(os.path.dirname(path), "model.tar.gz")))

        remove(os.path.join(os.path.dirname(path), "model.tar.gz-extracted", "agent"))
        remove(path)
        remove(os.path.join(os.path.dirname(path), "output.tar.gz"))
        remove(os.path.join(os.path.dirname(path), "source"))
        remove(os.path.join(os.path.dirname(path), "model"))
        remove(os.path.join(os.path.dirname(path), "mp4", "camera-45degree"))

if __name__ == '__main__':
    main()