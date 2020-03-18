import time
from subprocess import Popen, PIPE


def commandToEngine(command):
    print("\nChess UI : ")
    print("\t" + command)
    engine.stdin.write(command + '\n')


def getEngineReply():
    # using the 'isready' command (engine has to answer 'readyok')
    # to indicate current last line of stdout
    engine.stdin.write('isready\n')
    print('\nChess Engine :')
    while True:
        text = engine.stdout.readline().strip()
        if text == 'readyok':
            break
        if text != '':
            print("\t" + text)


engine = Popen(["C:\Temp\stockfish-6-64.exe"], stdin=PIPE, stdout=PIPE)
print "object type of engine is " + str(type(engine))
getEngineReply()

commandToEngine('go depth 10')
time.sleep(5)
getEngineReply()

commandToEngine('quit')

while (True):
    readInput = raw_input("Input command to Engine :")
    if readInput == "quit":
        break

print "Program terminated "