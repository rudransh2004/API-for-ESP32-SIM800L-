import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders 
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
mail_content = "your data is ready"
fromaddr = "airviewdevice@gmail.com"
toaddr = "nsrajput.ece@iitbhu.ac.in"
   
# instance of MIMEMultipart
msg = MIMEMultipart()
  
# storing the senders email address  
msg['From'] = fromaddr
  
# storing the receivers email address 
msg['To'] = toaddr
  
# storing the subject 
msg['Subject'] = "Subject of the Mail"
  
# string to store the body of the mail
body = "Body_of_the_mail"
  
# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.get_data()
        print(f)
        fuck = open("final.txt","w")
        fuck.write(f.decode('utf-8'))
        fuck.close()
        attachment = open("final.txt", "r")
  
# instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')
  
# To change the payload into encoded form
        p.set_payload((attachment).read())
  
# encode into base64
        encoders.encode_base64(p)
   
        p.add_header('Content-Disposition', "attachment; filename= %s" % "final.txt")
  
# attach the instance 'p' to instance 'msg'
        msg.attach(p)
  
# creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
  
# start TLS for security
        s.starttls()
  
# Authentication
        s.login(fromaddr, "AirView@12345")
  
# Converts the Multipart msg into a string
        text = msg.as_string()
  
# sending the mail
        s.sendmail(fromaddr, toaddr, text)
  
# terminating the session
        s.quit()


        print('Mail Sent')
        return '''
        <!doctype html>
         '''
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    app.run()
