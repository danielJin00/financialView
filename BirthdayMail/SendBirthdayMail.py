import datetime
from email.message import EmailMessage
import pandas as pd
import time
import smtplib
import os
import ssl

EMAIL_SENDER = 'juiciestJinster@gmail.com'
EMAIL_KEY = 'vjslioywnivbsffk' #16 App PW
EMAIL_RECEIVER = 'danielwodke25@gmail.com'

sign = "'"

em = EmailMessage()
em['From'] = EMAIL_SENDER
em['To'] = EMAIL_RECEIVER

#Get current day and split it into list [DayMonth, Year]
currentday = datetime.datetime.today().strftime("%d.%m.%Y") #temp
currentday.rsplit('.',1)
#Extract Data
bday_df = pd.read_csv('Birthdaydata.csv')
#[DayMonth, Year]
bday_df[['Date','Year']] = bday_df['Date'].str.rsplit(".",1, expand=True)
hits = bday_df.loc[bday_df['Date'] == currentday[0]]
# save year and names seperately in two lists
todaysBirthdayPeeps = bday_df['Name'].tolist()
Peepsyears = bday_df['Year'].tolist()

if todaysBirthdayPeeps:
    for peep in range(len(todaysBirthdayPeeps)):
        name = todaysBirthdayPeeps[peep]
        subject = f'WHOA! Heute ist {name}{sign}s Geburtstag!! \^-^/' 
        body = f'Schreib {name} zum {int(currentday[1])-int(Peepsyears[peep])}und feiert!!! '

        em['Subject'] = subject
        em.set_content(body)
    #add SSL (security)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_KEY)
            smtp.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, em.as_string())


#TODO LINK TO CONTINUE
#https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151

#TODO Bugdix