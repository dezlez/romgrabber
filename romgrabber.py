import paramiko, os

host = "10.0.0.15"
port = 22
username = "root"
password = "admin"

# Connect to Android Device
print 'Start Connexion...'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port=port, username=username, password=password)
sftp = ssh.open_sftp()
print 'Connected.'


#This is where the scripts will be added. 

# List the files from phone
print 'Listing all .srm files on your android device'
distantFiles = list()
filePath = '/storage/emulated/0/Download'
filePattern = '"*.srm"'
rawcommand = 'find {path} -name {pattern}'
command = rawcommand.format(path=filePath, pattern=filePattern)

stdin, stdout, stderr = ssh.exec_command(command)
filelist = stdout.read().splitlines()

for afile in filelist:
    (head, filename) = os.path.split(afile)
    distantFiles.append(filename)
print distantFiles

# List the .zip files in certain directory
print 'Listing all .zip files from your android device'
distantFiles = list()
filePath = '/storage/emulated/0/Download'
filePattern = '"*.zip"'
rawcommand = 'find {path} -name {pattern}'
command = rawcommand.format(path=filePath, pattern=filePattern)

stdin, stdout, stderr = ssh.exec_command(command)
filelist = stdout.read().splitlines()

for afile in filelist:
    (head, filename) = os.path.split(afile)
    distantFiles.append(filename)
print distantFiles

# Transfering a file to android device
sftp.put('/home/pi/RetroPie/roms/snes/Mortal Kombat.zip', '/storage/emulated/0/Download/Mortal Kombat.zip') #You need to re-type the name of the file in the destination
print 'The file has been transfered to your device'


sftp.close()
ssh.close()
