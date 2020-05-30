# loginbot

import webbot

#############################################################################################

username = 'ollie55589@gmail.com'

password = '3j3e3m7c'

#############################################################################################

"""
Enter your email/username into the above fields.

Each function will try your given username and password in the website
and print "incorrect" or "possibly correct"

Site functions:
	Facebook
	Hulu
	Amazon Prime
	Chase Bank
	Spotify
	Pandora
"""

def facebook(username, password):

	"""
	Facebook Auto Login

	params:
		username(str) - username/email for given account
		password(str) - password for given account
	"""

	web = webbot.Browser()

	web.go_to('facebook.com/login')							# go to the website
	web.type(username , into = 'Email' or 'Username')		# enter the username into correct place
	web.type(password , into = 'Password')					# enter password into correct place
	web.click('Log In')										# click the login button

	if web.exists('Email' or 'Username') == True:         # if it does work..
		print('Incorrect: Facebook')		   			  # print possibly correct
	else:											      # if it doesn't work..
		print('Correct: Facebook')			              # print incorrect

def hulu(username, password):

	"""
	Hulu Auto Login

	params:
		username(str) - username/email for given account
		password(str) - password for given account
	"""
	web = webbot.Browser()

	web.go_to('hulu.com/login')							    # go to the website
	web.type(username , into = 'Email' or 'Username')		# enter the username into correct place
	web.type(password , into = 'Password')	   				# enter password into correct place
	web.click('Log In')										# click the login button

	if web.exists('Email') == True:         # if it does work..
		print('Incorrect: Hulu')		   	# print possibly correct
	else:									# if it doesn't work..
		print('Correct: Hulu')			    # print incorrect

def prime(username, password):

	"""
	Amazon Prime Auto Login

	params:
		username(str) - username/email for given account
		password(str) - password for given account
	"""
	return

def chase(username, password):

	"""
	Chase Bank Auto Login

	params:
		username(str) - username/email for given account
		password(str) - password for given account
	"""
	return

def spotify(username, password):

	"""
	Spotify Auto Login

	params:
		username(str) - username/email for given account
		password(str) - password for given account
	"""
	return

def pandora(username, password):
	
	"""
	Pandora Auto Login

	params:
		username(str) - username/email for given account
		password(str) - password for given account
	"""
	return

#############################################################################################

# Websites to test

#facebook(username, password)
hulu(username, password)
#prime(username, password)
#chase(username, password)
#spotify(username, password)
#pandora(username, password)

#############################################################################################

