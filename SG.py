import os
import subprocess
import smtplib

#Gonna use the local host instead for you to test
#python3 -m smtpd -c DebuggingServer -n localhost:1025  to open port:1025
#EMAIL_ADRESS = os.environ.get('EMAIL_USER')
#EMAIL_PWD = os.environ.get('EMAIL_PASS')
EMAIL_ADRESS = "aladin.riabi@gmail.com"

status = "Status:"
javastatus = subprocess.check_output(["java", "-version"],stderr=subprocess.STDOUT)
if (javastatus =="Command 'java' not found"):
    print("Java does not exist")
    status= status + "\n Java does not exist"
    installVal = input("Do you want to install Java: Y/N \n")
    if (installVal == "Y" or installVal == "y") :
        print("Installing Java...")
        status=status+"\n Java installed"
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "default-jdk"], check=True)   
    
else :
    print(javastatus)
    status += javastatus.decode("utf-8")
    
updateVal = input("Do you want to update to another version?: Y/N \n")

if (updateVal == "Y" or updateVal == "y") :
    versionVal=input("Please enter the desired version")
    status = status + "\n updating Java to this version:" + versionVal
    subprocess.run(["sudo", "apt", "update"], check=True)
    subprocess.run(["sudo", "apt", "install", versionVal], check=True)   


with smtplib.SMTP('localhost',1025) as smtp: 
    smtp.sendmail(EMAIL_ADRESS,EMAIL_ADRESS,status)
    print("User notified via email")

#To use real email you need to put manually your credential or use env.variables
# with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    #smtp.ehlo()
    #smtp.starttls()
    #smtp.ehlo()
    #smtp.login('EMAIL_ADRESS','EMAIL_PWD')
        
