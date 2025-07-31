import smtplib

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user="mymail", password="password")
connection.sendmail(from_addr="mymail", to_addrs="Receiver Email", msg="Hello")
connection.close()


# pythonanywhere.com - its use for like suppose you have some reminder code , so its call the function everyweek or every day 
# to run your code and you receive message every day or week