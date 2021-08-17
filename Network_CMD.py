import os
import sys

#Running CMD commands in python

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
            
            print("Enter Another Command, Press Enter to Skip")
            Enter4 = str(input())
            
            print("Enter Another Command, Press Enter to Skip")
            Enter5 = str(input())
            
            CMD_Command = os.system("cmd /c" + Enter1)

            CMD_Line = print(CMD_Command)

            if CMD_Command >= 1:
                print("Process -" + Enter1 + "- Unsuccesful")
                
            else:
                print("Process -" + Enter1 + "- Succesful")
                
            CMD_Command = os.system("cmd /c" + Enter2)

            CMD_Line = print(CMD_Command)

            if CMD_Command >= 1:
                print("Process -" + Enter2 + "- Unsuccesful")
                
            else:
                print("Process -" + Enter2 + "- Succesful")
                
            CMD_Command = os.system("cmd /c" + Enter3)
            if Enter3 == "":
                print("No Further Entry Was given")
            
            else:
                CMD_Line = print(CMD_Command)

                if CMD_Command >= 1:
                    print("Process -" + Enter3 + "- Unsuccesful")
                    
                else:
                    print("Process -" + Enter3 + "- Succesful")
                    
            CMD_Command = os.system("cmd /c" + Enter4)
            if Enter4 == "":
                print("No Further Entry Was given")
            
            else:
                CMD_Line = print(CMD_Command)

                if CMD_Command >= 1:
                    print("Process -" + Enter4 + "- Unsuccesful")
                    
                else:
                    print("Process -" + Enter4 + "- Succesful")
                    
            CMD_Command = os.system("cmd /c" + Enter5)
            if Enter5 == "":
                print("No Further Entry Was given")
                
            else:
                CMD_Line = print(CMD_Command)

                if CMD_Command >= 1:
                    print("Process -" + Enter5 + "- Unsuccesful")
                    #sys.exit()
                    
                else:
                    print("Process -" + Enter5 + "- Succesful")
                    #sys.exit()


