import os
import sys

#Running CMD commands in python
#This script is written to run and check the success of an operable command
#Returns a not succesful when a command is not operable / not functioning
#Given any figure return equal to 0 is a success and 1 above is unsuccesful

Troubleshoot_Commands = ["help", "ipconfig", "ipconfig /all", "ipconfig /release", "ipconfig /renew",
                         "ipconfig /?", "ipconfig/flushdns", "net use", "arp -a", "nbtstat -a dc",
                         "getmac", "hostname", "netsh", "net view", "tracert", "netstat -e -p tcp",
                         "nslookup", "pathping", "systeminfo"]
HelpDesk_Commands = ["gpresult /r >c:\results.txt", "gpupdate /help", "gpresult /r", "gpresult /?"]

print("Command Prompt Execute Script")

while True:
    print("Enter 1 for Single Input, 2 for Multiple :(Max 5), 3 to Exit")
    Choice = int(input())
    for Press in range (1):

        if Choice == 3:
            sys.exit()

        if Choice == 1:
            print("Enter Command you want to execute")
            Enter = str(input())
            CMD_Command = os.system("cmd /c" + Enter)

            CMD_Line = print(CMD_Command)

            if CMD_Command >= 1:
                print("Process -" + Enter + "- Unsuccesful")
                #sys.exit()

            else:
                print("Process -" + Enter + "- Succesful")
                #sys.exit()

        if Choice == 2:
            print("Enter first Command you want to execute!")
            Enter1 = str(input())

            print("Enter Another Command")
            Enter2 = str(input())

            print("Enter Another Command, Press Enter to Skip")
            Enter3 = str(input())

            if Enter3 == "":

                CMD_Command1 = os.system("cmd /c" + Enter1)

                CMD_Line = print(CMD_Command1)

                CMD_Command2 = os.system("cmd /c" + Enter2)

                CMD_Line = print(CMD_Command2)

                CMD_Command3 = os.system("cmd /c" + Enter3)

                CMD_Line = print(CMD_Command3)

                if CMD_Command1 >= 1:
                    print("Process -" + Enter1 + "- Unsuccesful")

                else:
                    print("Process -" + Enter1 + "- Succesful")

                if CMD_Command2 >= 1:
                    print("Process -" + Enter2 + "- Unsuccesful")

                else:
                    print("Process -" + Enter2 + "- Succesful")

                if Enter3 == "":
                    print("No Further Entry Was given")

                elif CMD_Command3 >= 1:
                    print("Process -" + Enter3 + "- Unsuccesful")

                else:
                    print("Process -" + Enter3 + "- Succesful")

            else:

                print("Enter Another Command, Press Enter to Skip")
                Enter4 = str(input())

                if Enter4 == "":

                    CMD_Command1 = os.system("cmd /c" + Enter1)

                    CMD_Line = print(CMD_Command1)

                    CMD_Command2 = os.system("cmd /c" + Enter2)

                    CMD_Line = print(CMD_Command2)

                    CMD_Command3 = os.system("cmd /c" + Enter3)

                    CMD_Line = print(CMD_Command3)

                    CMD_Command4 = os.system("cmd /c" + Enter4)

                    CMD_Line = print(CMD_Command4)

                    if CMD_Command1 >= 1:
                        print("Process -" + Enter1 + "- Unsuccesful")

                    else:
                        print("Process -" + Enter1 + "- Succesful")

                    if CMD_Command2 >= 1:
                        print("Process -" + Enter2 + "- Unsuccesful")

                    else:
                        print("Process -" + Enter2 + "- Succesful")

                    if CMD_Command3 >= 1:
                        print("Process -" + Enter3 + "- Unsuccesful")

                    else:
                        print("Process -" + Enter3 + "- Succesful")

                    if Enter4 == "":
                        print("No Further Entry Was given")

                    elif CMD_Command4 >= 1:
                        print("Process -" + Enter4 + "- Unsuccesful")

                    else:
                        print("Process -" + Enter4 + "- Succesful")

                else:

                    print("Enter Another Command, Press Enter to Skip")
                    Enter5 = str(input())

                    CMD_Command1 = os.system("cmd /c" + Enter1)

                    CMD_Line = print(CMD_Command1)

                    CMD_Command2 = os.system("cmd /c" + Enter2)

                    CMD_Line = print(CMD_Command2)

                    CMD_Command3 = os.system("cmd /c" + Enter3)

                    CMD_Line = print(CMD_Command3)

                    CMD_Command4 = os.system("cmd /c" + Enter4)

                    CMD_Line = print(CMD_Command4)

                    CMD_Command5 = os.system("cmd /c" + Enter5)

                    CMD_Line = print(CMD_Command5)

                    if CMD_Command1 >= 1:
                        print("Process -" + Enter1 + "- Unsuccesful")

                    else:
                        print("Process -" + Enter1 + "- Succesful")

                    if CMD_Command2 >= 1:
                        print("Process -" + Enter2 + "- Unsuccesful")

                    else:
                        print("Process -" + Enter2 + "- Succesful")

                    if CMD_Command3 >= 1:
                        print("Process -" + Enter3 + "- Unsuccesful")

                    else:
                        print("Process -" + Enter3 + "- Succesful")

                    if CMD_Command4 >= 1:
                        print("Process -" + Enter4 + "- Unsuccesful")

                    else:
                        print("Process -" + Enter4 + "- Succesful")

                    if Enter5 == "":
                        print("No Further Entry Was given")

                    elif CMD_Command5 >= 1:
                        print("Process -" + Enter5 + "- Unsuccesful")
                        #sys.exit()

                    else:
                        print("Process -" + Enter5 + "- Succesful")
                        #sys.exit()
 
