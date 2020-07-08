# Automation of continuous integration and continuous deployment
This repository tries to make a setup in which automated testing is conducted together with an automated release upon a successful pull request. Currently, the versioning is performed by the update.py script, and store in a separate version.txt file. This might not be the optimal solution when performing e.g. PyInstaller freezing and might need to be optimised at a later point.

## Envisioned plan of usage
The setup is envisioned to be used as follows:
1) Either the develop branch or another development branch from a fork is update with new code/features
2) This code is uploaded to the github repository 
3) Upon upload, the code is checked through the continuous integration. A new version tag is required at this stage. It will be referenced by the release
4) A pull request to the main branch is created
5) All pull requests are being tested (but only on one python version)
6) A successful test is required before a merge with the main branch is performed
7) When merge is issued, automatic deployment to PyPI and a release on github is performed

## Possible improvements
- [ ] Remove requirement of version tag from development branch