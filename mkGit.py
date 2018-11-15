import time
import gnupg
import getpass
import selenium
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep

##This part just gets a password from encrypted file##
gpg = gnupg.GPG(gnupghome='/Users/dennis/.gnupg')

# Take input for repoName
repoName = input("Enter name for new repo: ")
#open encrypted pw file with variable f. Use with so it closes itself
with open('../pw.txt.asc', 'r') as f:
    #Takes password for gpg private key
    gpw = getpass.getpass('Password: ')
    #declare var for the data in the file. Takes as str
    read_data = f.read()
    #set var for decrypted data. Use input from earlier
    dpass = gpg.decrypt(read_data, passphrase=gpw)
    #var for data from decryption. Saved as bytes. Encoded
    dp = dpass.data
    #print(type(dp)) #returns the type of dp as bytes
    
    
    #split the string into a list of items. Use decode to return
    split1 = dp.decode().split("\'")
    #print(split1[0]) 
    #print(split1[1])
    #print(dpass.data)

# Using firefox headless to access the web
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
# Opens up the website
driver.get('https://github.com/login')

# Select the username box
id_box = driver.find_element_by_id('login_field')
# send username
id_box.send_keys('Tacm4n')

# Select the password box
pw_box = driver.find_element_by_id('password')
# enter pw
pw_box.send_keys(split1[0])

# find the sign in button
submitButton = driver.find_element_by_name('commit')
# CLICK IT
submitButton.click()

# find the new button
newButton = driver.find_element_by_link_text('New')
newButton.click()

# get box for repo name
repoBox = driver.find_element_by_id('repository_name')
# select repo name box and fill it with repo name previously entered
repoBox.click()
repoBox.send_keys(repoName)
# Wait until website registers that repo box is populated
time.sleep(1)
# Simulate enter keypress
repoBox.send_keys(u'\ue007')
## This part didn't seem to work. Couldn't find the button
# find create repository button
#repoButton = driver.find_element_by_partial_link_text('Create')
#repoButton.click()
