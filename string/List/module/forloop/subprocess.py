#default module within python
import subprocess
print(dir(subprocess))
cmd="dir"
sp=subprocess.Popen(dir,shell=True,STDOUT=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()

print(f'The return code: {rc}')
'''
# to get bash version
import subprocess
cmd=["bash","--version"]
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
o,e=sp.communicate()

if rc==0:
    for each_line in o.splitlines():
     # if "version" in each_line and "release" in each_line:
     print("command output: ",o)
       # print(each_line.split()[3].split('(')[0])
else:
    print("command was failed: ",e)
'''