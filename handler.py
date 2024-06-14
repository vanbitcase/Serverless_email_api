import smtplib
from flask import Flask, request, jsonify
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/apidata', methods=['POST','GET'])
def process_data():
    data = request.json
    receiver_email = data.get('receiver_email')
    subject = data.get('subject')
    body_text = data.get('body_text')
    sender_email = 'anshastogi@gmail.com'
    password ='gikjtsgtkcmxzszm' # this password is generated using 'Google app password' for special allowance
    #getpass.getpass("Enter the password: ")

    # Construct the email
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body_text, 'plain'))

    try:
        #  server using SMTP_SSL
        smtp = smtplib.SMTP_SSL('smtp.gmail.com',465)
        smtp.ehlo()

        smtp.login(sender_email, password)

        smtp.sendmail(sender_email, receiver_email, message.as_string())

        smtp.quit()
    
        return jsonify({"status": 'Email sent successfully',"receiver_email":receiver_email}), 200
    except smtplib.SMTPAuthenticationError:
        return jsonify({"status": 'Failed to send email', "error": "Authentication failed"}), 401
    except smtplib.SMTPServerDisconnected:
        return jsonify({"status": 'Failed to send email', "error": "Connection unexpectedly closed"}), 500
    except smtplib.SMTPException as e:
        return jsonify({"status": 'Failed to send email', "error": str(e)}), 500



