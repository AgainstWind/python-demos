import commands
import os

#linux
commands.getstatusoutput('netstat -n')
commands.getoutput('netstat -n')


#windows
os.system('netstat -n')