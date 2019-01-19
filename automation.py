import os
from subprocess import (Popen,PIPE)

def find_duplicates(path):
    checksums = {}
    for root, _, files in os.walk(path):
        for name in files:
            fullpath = os.path.join(root,name)
            print(f"Processing file: {fullpath}")
            with Popen(["md5sum", fullpath],stdout=PIPE) as proc:
                checksum, path = proc.stdout.read().split()
                if checksum in checksums:
                    print(f"Found duplicate files: {fullpath} {checksums[checksum]}")
                checksums[checksum] = fullpath

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        npath = sys.argv[1]
        find_duplicates(npath)
        sys.exit(0)
    print("Pass in path to find duplicates")