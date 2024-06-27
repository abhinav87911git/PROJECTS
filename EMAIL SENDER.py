#  script that sends email 


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, from_email, to_email, from_password, body):
    msg =  MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
       with smtplib.SMTP('smtp.gmail.com', 587) as server :
           server.starttls()
           server.login(from_email, from_password)
           server.sendmail(from_email, to_email, msg.as_string())
           print('Email sent successfully ')
    except smtplib.SMTPAuthenticationError:
       print('Authentication failed, please check your email and password')
    except Exception as e:
       print('An exception occured : {e}')

      

if __name__ == '__main__':
    from_email = input('Enter the email from you want to send mail: ')
    to_email = input("Enter the recipient's email : ")
    from_password = input('Enter your password: ')
    subject = input('Enter the subject: ')

    use_file =input('do you want to read email body from any file (Y/N): ')
    if use_file== 'Y':
       file_path = input('enter the file path')
       try:
          with open(file_path, 'r') as file:
              body = file.read()
       except FileNotFoundError:
          print('File not found , please check the file path ')
          body =""
    else:
       body = input(' Enter the body of email : ')

    if body:
         send_email(subject, from_email, to_email, from_password, body)
    else:
        print('Email body is empty , please provide the body :')