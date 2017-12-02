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


#Unhash a Script(s) to begin. 

# Unhash to List rom save states files from phone

#print 'Listing all .srm files on your android device'
#awayFiles = list()
#filePath = '/storage/emulated/0/Download'
#filePattern = '"*.srm"'
#rawcommand = 'find {path} -name {pattern}'
#command = rawcommand.format(path=filePath, pattern=filePattern)

#stdin, stdout, stderr = ssh.exec_command(command)
#filelist = stdout.read().splitlines()

#for afile in filelist:
#    (head, filename) = os.path.split(afile)
#    awayFiles.append(filename)
#print awayFiles

# List the .zip files in certain directory

#print 'Listing all .zip files from your android device'
#awayFiles = list()
#filePath = '/storage/emulated/0/Download'
#filePattern = '"*.zip"'
#rawcommand = 'find {path} -name {pattern}'
#command = rawcommand.format(path=filePath, pattern=filePattern)

#stdin, stdout, stderr = ssh.exec_command(command)
#filelist = stdout.read().splitlines()

#for afile in filelist:
#    (head, filename) = os.path.split(afile)
#    awayFiles.append(filename)
#print awayFiles

#Unhash this script if you want to transfer a file to android device

#sftp.put('/home/pi/RetroPie/roms/snes/Donkey Kong Country.zip', '/storage/emulated/0/Download/Donkey Kong Country.zip') #You need to re-type the name of the file in the destination
#print 'The .zip file has been transfered to your device'

#sftp.put('/home/pi/RetroPie/roms/snes/Donkey Kong Country.srm', '/storage/emulated/0/Download/Donkey Kong Country.srm') #You need to re-type the nam$
#print 'The save file has been transfered to your device'


# Uncheck this script to transfer files from phone to raspberrypi

sftp.get('/storage/emulated/0/Download/Donkey Kong Country.srm' , '/home/pi/RetroPie/roms/snes/Donkey Kong Country.srm') # You need to re-type the name of the file in the destination
print 'The file has been downloaded'


sftp.close()
ssh.close()
