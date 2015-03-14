##Commands file
##Just in case you needed to add your own commands, Just don't forget
##to add it to the help option.





def coms(com):

    
    
    while True:


        if "help" in com or "?" in com:
            return("\t ls \t status \t reboot \t pwd \t whoami\n\t ping\t cd\t\t passwd\t\tversion   exit\n")
            
        elif "ls" in com:
            return(".\n..\n")

        elif "status" in com:
            return("[+]ONLINE\nUPLOAD OK\nDOWNLOAD OK\n")

        elif "reboot" in com:
            return("\nRebooting...\n")
            
        elif "pwd" in com:
            return "~/home\n"
            
        elif "whoami" in com:
            return "admin\n"

        elif "ping" in com:
            return("Not allowed.\n")

        elif "cd" in com:
            return("Not allowed.\n")

        elif "passwd" in com:
            return("Not allowed.\n")

        elif "version" in com:
            return("hg8240 3.5.1\n")

        elif "exit" in com:
            return("BYE\n")            

        elif "ping" in com:
            return("Not Allowed.\n")
            
            

        else:
            return com + ": command not found\n"
        
