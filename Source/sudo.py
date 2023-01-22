import os, sys

def tuple_strings_exec():
    path = ("NSudoLC.exe -U:T -P:E ", command)
    all_strings = tuple(map(str, path))
    result = ''.join(all_strings)
    os.system(result)

if len(sys.argv) < 2:
    print("sudo: ERROR: You must insert a parameter to execute")
    print("for a help insert: 'sudo --help'")
    print(" ")
    print("Press 'Enter' to quit")
    input()
    sys.exit()

if len(sys.argv) <= 2:
    script_name, parameter = sys.argv
    
    if (parameter) == "-i":
        os.system('C:\sudo\cmd.lnk')
    
    if (parameter) == "--login":
        os.system('C:\sudo\cmd.lnk')
    
    if (parameter) == "--matrix":
        os.system('C:\sudo\system.lnk')
    
    if (parameter) == "--parrot":
        os.system('C:\sudo\system2.lnk')
    
    if (parameter) == "-n":
        os.system('cmd.exe')
    
    if (parameter) == "--normal":
        os.system('cmd.exe')
    
    if (parameter) == "--help":
        print("Usage: sudo [options...] <command>")
        print(" -i, --login                Exec with TrustedInstaller Permissions")
        print(" -n, --normal               Exec with normal administrator Permissions")
        print(" ")
        print("This is not the full help. Type 'sudo --help-all' for a complete help")
        print(" ")
        print("Press 'Enter' to quit")
        input()


    if (parameter) == "--help-all":
        print("Usage: sudo [options...] <command>")
        print(" -i, --login                Exec with TrustedInstaller Permissions")
        print(" -n, --normal               Exec with normal administrator Permissions")
        print(" ")
        print("you discovered some easter eggs")
        print(" ")
        print("You try to type 'sudo --parrot' & 'sudo --matrix' and see")
        print(" ")
        print("Press 'Enter' to quit")
        input()
        
        

else:
    script_name, parameter, command = sys.argv
    
    if (parameter) == "-i":
        tuple_strings_exec()
    if (parameter) == "--login":
        tuple_strings_exec()
    if (parameter) == "-n":
        os.system(command)  
    if (parameter) == "--normal":
        os.system(command)

