import time

import requests, json

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.get('https://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=json', verify=False)
sites = response.json()
def send():


    import smtplib
    from email.mime.text import MIMEText


    from_addr = '810063@stu.nknush.kh.edu.tw'
    to_addr = '810063@stu.nknush.kh.edu.tw'


    smtpssl=smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtpssl.login(from_addr, "E126096510")

    msg = '現在 復興站 PM2.5='+site['PM25']
    mime=MIMEText(msg, "plain", "utf-8")
    mime["Subject"]='復興站空氣品質'

    mime["From"]="PM2.5監視器"
    mime["To"]= to_addr

    smtpssl.sendmail(from_addr, to_addr, mime.as_string())
    smtpssl.quit()

while True:
    for site in sites:
        if site['Site'] == '復興':
            send()
            break
    time.sleep(0.1)
