import sys, os
sys.path.append('..')
import AutomatedCICD

versionFile = os.path.join(os.path.dirname(__file__),'version.txt')

def version():
    with open(versionFile) as f:
        lines = f.readlines()

    version = lines[0].strip()

    return version

def newSimpleFunction(*args,**kwargs):
    print(*args,**kwargs)

    
if __name__ == "__main__":
    print(version())