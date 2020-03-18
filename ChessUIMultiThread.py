#!/usr/bin/python

import threading
import time
from subprocess import Popen, PIPE

exitFlag = 0


class EngineThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        engine = Popen(["C:\Temp\stockfish-6-64.exe"], stdin=PIPE, stdout=PIPE)
        get_engine_reply(engine)
        while True:
            # get_ui_input(engine)
            read_input = raw_input("Input command to Engine :")
            command_to_engine(engine, read_input)
            get_engine_reply(engine)


def command_to_engine(engine, command):
    print("\nChess UI : ")
    print("\t" + command)
    engine.stdin.write(command)


def get_engine_reply(engine):
    # using the 'isready' command (engine has to answer 'readyok')
    # to indicate current last line of stdout
    engine.stdin.write('isready\n')
    print('\nChess Engine :')
    while True:
        text = engine.stdout.readline().strip()
        if text == 'readyok':
            break
        if text != '':
            print("\t" + text)  # def print_time(threadName, delay, counter):

def get_ui_input(engine):
    while True:
        read_input = raw_input("Input command to Engine :")
        if read_input == "quit":
            command_to_engine(engine, read_input)
            break
        else:
            command_to_engine(engine, read_input)


# def get_chars():
#     char = ''
#     input_str = ''
#     while char != '\r':
#         char = msvcrt.getche()
#         if char == '\r':
#             break
#         input_str += char
#     input_str += '\n'
#     return input_str

# Create new thread and start
thread1 = EngineThread()
thread1.start()
# get_ui_input()

print "Program terminated "
