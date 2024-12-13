import os
import time

while True:
    #print('\n--------------------------------------------------\n')
    
    #print("     (_\     /_)     ")
    #print("       ))   ((       ")
    #print('     .-"""""""-.     ')  
    #print(" /^\/  _.   _.  \/^\ ")
    #print(" \(   /__\ /__\   )/ ")
    #print("  \,  \o_/_\o_/  ,/  ")
    #print("    \    (_)    /    ")
    #print("     `-.'==='.-'     ")
    #print("      __) - (__      ")
    #print("     /  `~~~`  \     ")
    #print("    /  /     \  \    ")
    #print("    \ :       ; /    ")
    #print("     \|==(*)==|/     ")
    #print("      :       :      ")
    #print("       \  |  /       ")
    #print("     ___)=|=(___     ")
    #print("    {____/ \____}    ")

    print("")
    print(" ^__^             ")
    print(" (oo)\_______     ")
    print(" (__)\       )\/\ ")
    print("     ||----w |    ")
    print("     ||     ||    ")
    print("")

    os.system('net stop wuauserv')
    os.system('net stop bits')
    os.system('net stop dosvc')
    time.sleep(30)

