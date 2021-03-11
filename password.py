import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)

lowercaseLetter1=chr(random.randint(97,122)) #Generate a random lowercase letter (based on ASCII code)
lowercaseLetter2=chr(random.randint(97,122)) #Generate a random lowercase letter (based on ASCII code)
 
digit1=chr(random.randint(48,57)) #Generate a random digit between 0 - 9 (based on ASCII code)
digit2=chr(random.randint(48,57)) #Generate a random digit between 0 - 9 (based on ASCII code)

punctuation1=chr(random.randint(48,57)) #Generate a random punctuation sign (based on ASCII code)
punctuation2=chr(random.randint(48,57)) #Generate a random punctuation sign

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuation1 + punctuation2
password = shuffle(password)

#Ouput
print(password)