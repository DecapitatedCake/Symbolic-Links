#!/usr/bin/env python3
#Name: Mohammed Mohammedtayib
#Date: 15/11/2022
#RIT email: mnm6346@g.rit.edu

import os
import subprocess
import time
from termcolor import cprint
from tqdm import tqdm
from subprocess import Popen, PIPE


green = "\u001b[32m"
white = "\u001b[37m"


#To first start off with our script we need to clear the terminal to keep it clean
print("Hello Friend!, Welcome to the shortcut, the screen will be cleared in 2 seconds")
time.sleep(3)
os.system('clear')


def menu():
	print("Press [1] to create a symbolic link")
	print("Press [2] to delete a symbolic link")
	print("Press [3] to run a shortcut report")

menu()
option = input("Enter Your Option: ")

user = os.environ['USER']

#Creating a while loop for the menu until the user presses 0 and exists
while option != "0":
	if option == "1":
		#Execute whatever option 1 is
		print("Option [1] has been called!")
		user = os.environ['USER']
		file = input("Kindly enter the name of the file to create a shortcut: ") #Takes the input of the user of which file the user wants a symbolic link for
		search = Popen(['find', '/', '-type', 'f', '-name', file], stdout=PIPE, stderr=PIPE) #Looks for the file and using the / it seaerches everywhere and we used the pipe to dump errors
		output = search.communicate()[0] #
		output = output.decode('utf-8') #The format for decoding 
		#print(output)
		#print(f'{green} Found:  \n {output} {white}')

		if output != '':
			print(f'[+]File Found: {output}')
			os.symlink(output.rstrip(), f'/home/{user}/{file}')
			print(f'\n Successful') 
			print("[!] Extra readlink command output:")
			os.system(f'readlink /home/{user}/{file}')

		else:
			cprint(f'\n[-]File "{file}" not found', 'red', attrs=['blink'])

 	
		


	elif option == "2":
		#Execute whatever option 2 is
		print("Option [2] has been called!")

		file = input("\nKindly enter the link to remove:	")
		print(f'\nPress Y/y to confirm deleting {green}{file}{white}?')
		choice = input()
		if choice == 'y' or choice == 'Y':
			for i in tqdm(range(10)):
				time.sleep(.2)
			os.system(f'unlink /home/{user}/{file}')

		else:
			main()



	elif option == "3":
		#Execute whatever option 3 is
		print("Option [3] has been called!")

		dire = subprocess.check_output('pwd')
		dire = dire.decode('utf-8')
		print(f'\n Your current directory is: ', dire)

		symlink = subprocess.check_output(f'ls -la /home/{user} | grep ^l |' + ''' awk '{print $9 "\t" $10 "\t"$11}' ''', shell = True).decode('utf-8')
		symlink_counter = subprocess.check_output(f'ls -la /home/{user} | grep ^l | wc -l', shell = True).decode('utf-8')
		print(symlink)
		print(symlink_counter)


	elif option == 'q' or option == 'Q':
		cprint ('\nQuiting program: Returning to shell.', 'red', attrs=['blink'])
		time.sleep(5)
		os.system('clear')
		exit()

	elif option == 'quit':
		cprint('\nQuiting program: Returning to shell.', 'red', attrs=['blink'])
		time.sleep(5)
		os.system('clear')
		exit()


	else:
		print("Invalid Option")


	print(".")
	print(".")
	print(".")
	menu()
	option = input("Enter Your Option: ")

print("Thank you for using this program! Goooooooooooooodbyeeeeeeeeeee.")
