import smtplib
import email.mime.multipart as mime

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('hstewart15@mail.strakejesuit.org', '!we3AfUja!')

msg = mime.MIMEMultipart()
msg['Subject'] = input("Please enter to-do: ")
text = msg.as_string()

server.sendmail('hstewart15@mail.stakejesuit.org', 'hstewart@tamu.edu', text)
server.quit()
