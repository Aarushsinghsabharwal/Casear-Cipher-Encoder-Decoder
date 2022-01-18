from colorama import Fore
from colorama import init
init()
print(Fore.RED)
print("""ENCODE AND DECODE THE
 	 ___      __      ____   ___      __      ____  
	| __|    /  \    | __ | |  _|    /  \    ||  ||
	||      / /\ \   ||___  |___    / /\ \   || _||
	||__   / /__\ \  | ___|  _  |  / /__\ \  || \\
	|___| /_/    \ \ ||___  |___| /_/    \ \ ||  \\  cIpHeR """)

reference_string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
	print(Fore.WHITE)
	choice=int(input("Choose between 1(ENCODE) and 2(DECODE): "))
	print(Fore.YELLOW)
	if choice==1:
		original_message=input("Enter the message to be encrypted:").upper()
		encoded_message=""
		key=input("Enter the key(b/w 0 and 26):")
		print(f"\nThe text is to be shifted {key} places.")
		for letter in original_message:
			if letter in reference_string:
				shifted_position=reference_string.find(letter)+(int(key)%26)
				if shifted_position>25:
					shifted_position-=26
				encoded_char=reference_string[shifted_position]
				encoded_message+=encoded_char
			else:
				encoded_message+=letter

		print(Fore.GREEN+"The encoded message is:")
		print(Fore.WHITE+encoded_message.lower())
		break
	elif choice==2:
		encoded_message=input("Enter the message to be decrypted:").upper()
		original_message=""
		key=input("Enter the key(b/w 0 and 26):")
		print(f"\nThe text is to be shifted back {key} places.")
		for letter in encoded_message:
			if letter in reference_string:
				shifted_position=reference_string.find(letter)-(int(key)%26)
				if shifted_position<0:
					shifted_position+=26
				original_char=reference_string[shifted_position]
				original_message+=original_char
			else:
				original_message+=letter

		print(Fore.GREEN+"The decoded message is:")
		print(Fore.WHITE+original_message.lower())
		break
	else:
		print("Invalid input, TRY AGAIN")
		continue