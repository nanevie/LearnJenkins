import os, re, socket
#import time
import json, subprocess, paramiko

print "reading env vars "
target_hostname = os.getenv('TARGET_HOSTNAME')
target_ip = os.getenv('TARGET_IP')
user_on_target_vm = os.getenv('USER_ON_TARGET_VM')
#target_cloud = os.getenv('TARGET_CLOUD')
private_key = os.getenv('PRIVATE_KEY')

print 'IP: ' + target_ip  + ' User: ' + target_ip
# set a variable for Paramiko's ssh client
sshClient = paramiko.SSHClient()

# Functions to open and close the ssh connection
def sshOpenConn(ipAddress, username, privateKey):
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshClient.load_system_host_keys()
    pkey = k
    sshClient.connect(ipAddress, username=username, privateKey=private_key)
    print "Connected to server " + ipAddress + "\n"
def sshCloseConn():
    sshClient.close()

# Function to execute a command
# Note the use of command.replace to mask sensitive info in the log
def sshExecCmd(command, stringToMask=spiList):
    print "Executing command ...... %s " % command.replace(stringToMask, "xxxxxxxxx")
    ssh_stdin, ssh_stdout, ssh_stderr = sshClient.exec_command(command)
    stderr = ssh_stderr.read()
    stdout = ssh_stdout.read()
    exitCode = ssh_stdout.channel.recv_exit_status()
    print ("stderr: \n{}\n ", stderr)
    print ("stdout: \n{}\n ".format(stdout))
    print "Exit status of command %s is : %d" % (command.replace(stringToMask, "xxxxxxxxx"), exitCode)
    return(stderr, stdout, exitCode)

def makeDirectory(dirName):
    commandToExecute = "mkdir -p " + dirName + "; rm -rf " + dirName + "/*.sh"
    stderr, stdout, exitCode = sshExecCmd(commandToExecute)
    if exitCode != 0:
        print "Failed to create directory : " + commandToExecute
        exit(1)

# Sensitive vars to mask
spiList = [private_key]
def printMaskedFailure(command, stringToMask=spiList):
    cmd2display = command
    for spItem in stringsToMask:
        cmd2display = cmd2display.replace(spItem, "xxxxxxxxx")
    print "Failed :  %s  " % (cmd2display)

##### Variables have been read from environment, functions are defined, work can begin #####

# Login to remote server  ...
sshOpenConn(target_ip, target_ip, private_key)

# Find user's home directory
commandToExecute = "echo $\{HOME\}"
stderr, stdout, exitCode = sshExecCmd(commandToExecute)
if exitCode != 0:
    printMaskedFailure("Failed to execute command : " + commandToExecute)
    exit(1)

#create remoteApp1Dir 
remoteApp1Dir = "$\{HOME\}/myAwesomeApp"
makeDirectory(remoteApp1Dir)

# Verify
commandToExecute = "ls -la $\{HOME\}"
stderr, stdout, exitCode = sshExecCmd(commandToExecute)
if exitCode != 0:
    printMaskedFailure("Failed to execute command : " + commandToExecute)
    exit(1)

# Verify docker
commandToExecute = "docker version"
stderr, stdout, exitCode = sshExecCmd(commandToExecute)
if exitCode != 0:
    printMaskedFailure("Failed to execute command : " + commandToExecute)
    exit(1)



