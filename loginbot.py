#############################################################################################

# Login Bot
# https://mashable.com/article/mschf-password-of-the-day-treasure-hunt/

import webbot

#############################################################################################

"""
Enter your given email or username and password into their fields.

The bot will test these logins automatically on each site.

In the command line, it will output 'Site: Incorrect' or 'Site: Possibly Correct'.

If it says possibly correct, you can visit the site yourself and check for a
successful login.
"""

USERNAME = 'random@email.com'

PASSWORD = 'password!'

#############################################################################################

def facebook(username, password):

	"""
	Facebook Auto Login

	params:
		username(str) - username/email for given account
		password(str) - password for given account
	"""

	web = webbot.Browser()

	web.go_to('facebook.com/login')                         # go to the website
	web.type(username , into = 'Email' or 'Username')       # enter the username into correct place
	web.type(password , into = 'Password')                  # enter password into correct place
	web.click('Log In')                                     # click the login button

	if web.exists('Email' or 'Username') == True:         # if it does work..
		print('Incorrect: Facebook')                      # print possibly correct
	else:                                                 # if it doesn't work..
		print('Correct: Facebook')                        # print incorrect

def hulu(username, password):

	"""
	Hulu Auto Login

	params:
		username(str) - username/email for given account
		password(str) - password for given account
	"""
	web = webbot.Browser()

	web.go_to('hulu.com/login')                             # go to the website
	web.type(username , into = 'Email' or 'Username')       # enter the username into correct place
	web.type(password , into = 'Password')                  # enter password into correct place
	web.click('Log In')                                     # click the login button

	if web.exists('Email') == True:         # if it does work..
		print('Incorrect: Hulu')            # print possibly correct
	else:                                   # if it doesn't work..
		print('Correct: Hulu')              # print incorrect

def prime(username, password):

	"""
	Amazon Prime Auto Login

	params:
		username(str) - username/email for given account
		password(str) - password for given account
	"""
	#todo
	return

def chase(username, password):

	"""
	Chase Bank Auto Login

	params:
		username(str) - username/email for given account
		password(str) - password for given account
	"""
	#todo
	return

def spotify(username, password):

	"""
	Spotify Auto Login

	params:
		username(str) - username/email for given account
		password(str) - password for given account
	"""
	#todo
	return

def pandora(username, password):
	
	"""
	Pandora Auto Login

	params:
		username(str) - username/email for given account
		password(str) - password for given account
	"""
	#todo
	return

#############################################################################################

# Websites to test

facebook(USERNAME, PASSWORD)
hulu(USERNAME, PASSWORD)
#prime(USERNAME, PASSWORD)
#chase(USERNAME, PASSWORD)
#spotify(USERNAME, PASSWORD)
#pandora(USERNAME, PASSWORD)

#############################################################################################

