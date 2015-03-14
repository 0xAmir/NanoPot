import SocketServer
from Commands import coms
from thread import start_new_thread
from time import sleep,strftime



class ReqHandle(SocketServer.BaseRequestHandler):
    def handle(self):
        
        try:
            filename = "Microlog " + strftime("%m%d%y %H%M%S") + " .txt"
            f = open(filename,"w",0)
            f.write("Received Connection from " + `self.client_address` + '\n')
            
            self.request.send("Echolife hg8240 Broadband Router")

            self.request.send("\nLogin: ")
            usr = self.request.recv(1024)
            f.write("\nTried to login with username: " + usr)
            
            self.request.send("Password: ")
            passwd = self.request.recv(1024)
            f.write("\nTried to login with password: " + passwd)
            
            f.write("\n[Logging Session..]\n")
            
            while True:
                self.request.send(" > ")
                command = self.request.recv(1024)
                f.write(command)
                reply = coms(command)
                self.request.send(reply)

                ##Little addition for the reboot option for realism
                if "reboot" in command:
                    sleep(10)

                #And for exit as well..
                if "exit" in command:
                    exit(0)
                    f.write("[END OF LOG]")
                    f.close()

                    
        except Exception as e:
            print("[-]OOPS Something went wrong !\n Error Details: " + `e`)




def startsrv(port):
    try:
        srv = SocketServer.TCPServer(('0.0.0.0', port),ReqHandle)
        srv.allow_reuse_address = True
        srv.serve_forever()

    except Exception as e:
        print("[-]Oops Something went wrong !\nError Details: " + `e`)
    
        
listenports = (80,8080,22,21,23,443)

for port in listenports:
    try:
        start_new_thread(startsrv,(port,))
        print("[+]Server listener created on port " + `port`)
    except Exception as e:
        print("[-]Oops Something went wrong !\nError Details: " + `e`)


raw_input()
