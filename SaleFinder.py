import json
import praw
import smtplib
from termcolor import colored
from email.mime.text import MIMEText

def SSD_Find_Sale():
	
	with open("credentials_JSON_File") as w:
		params = json.load(w)
	
	reddit = praw.Reddit(client_id=params['client_id'],
							client_secret=params['client_secret'],
							user_agent=params['user_agent'])
	
	while True:
		for sub in reddit.subreddit('bapcsalescanada').stream.submissions():
			print(colored("New Post: ", 'red') + colored(sub.title, 'green'))
			if "[SSD]" in sub.title:
				s = smtplib.SMTP("smtp.gmail.com", 587)
				#s.set_debuglevel(1)
				s.ehlo()
				s.starttls()
				s.ehlo()
				
				s.login('email', 'password')
				msg = MIMEText(sub.url)
				sender = 'you'                                         
				recipients = 'someone'
				msg['subject'] = sub.title
				msg['From'] = sender

				
				s.sendmail(sender, recipients, msg.as_string())
				print(colored("Email sent to " + recipients, 'green'))
				print(colored("Job Done!", 'red'))
				s.quit()
	
SSD_Find_Sale()