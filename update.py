import sys, os
sys.path.append('AutomatedCICD')
import version


currentVersion = version.version().split('.')


if len(sys.argv)>1:
    newVersion = sys.argv[1]
else:
    newVersion = '.'.join([x if i<len(currentVersion)-1 else str(int(x)+1) for i,x in enumerate(currentVersion)])

currentVersion = '.'.join(currentVersion)

print('Updating from {} to {}'.format(currentVersion,newVersion))


with open(os.path.join('AutomatedCICD','version.txt'),'w') as f:
    f.write(newVersion)


os.system('git add AutomatedCICD/version.txt')
os.system("git commit -m 'Update to version {}'".format(newVersion))
os.system("git tag -a v{} -m '{}'".format(newVersion,newVersion))
os.system("git push")
os.system("git push --tags")