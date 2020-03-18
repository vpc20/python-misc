import getpass
import telnetlib

from Tools.scripts.treesync import raw_input

HOST = raw_input("HOST : ")
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

try:
    tn = telnetlib.Telnet(HOST)
    tn.write('\n')
    tn.read_very_eager()
    tn.write(user)
    tn.write('\t')  # tab into the next field
    tn.write(password)
    tn.write('\r')  # 'enter' key
except:
    print("Error")
