import sys
sys.path.append('..')
sys.path.append('../AutomatedCICD')
import AutomatedCICD.version

def test_simple():
    return True

def test_version():
    vers = AutomatedCICD.version.version
    print(vers)