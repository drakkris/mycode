#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   Learning about Python SSH"""

import paramiko
import json

def load_credz_data():
    with open('credz.txt', 'r') as file:
        return file.read()


def main():
    """Our runtime code that calls other functions"""
        
    #credz = load_credz_data()
    credz = json.loads(load_credz_data())
    # describe the connection data
    # credz = [
    #         {"un": "bender", "ip": "10.10.2.3"}, 
    #         {"un": "zoidberg", "ip": "10.10.2.5"}, 
    #         {"un": "fry", "ip": "10.10.2.4"}
    #        ]

    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    # loop across the collection credz
    for cred in credz:
    
        ## create a session object
        sshsession = paramiko.SSHClient()

        ## add host key policy
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ## display our connections
        print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))

        ## make a connection
        sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

        ## touch the file goodnews.everyone in each user's home directory
        sshsession.exec_command("touch /home/" + cred.get("un") + "/goodnews.everyone")

        ## list the contents of each home directory
        sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + cred.get("un"))

        ## display output
        print(sessout.read().decode('utf-8'))

        ## close/cleanup SSH connection
        sshsession.close()

    print("Thanks for looping with Alta3!")

main()


