import random

vowel = ["a", "e" , "i" , "o", "u" ]
const = ["b","c","d","f","g","h","j","k","l","m","n","p","r","s","t"]

#Input: Structure of a word
#Output: Word generated from said structure
def name_gen():

	new_name = ""

	for x in range( int(10) ): #This algo uses 1/3 vowel and 2/3 consts

		if ( (random.random() * 3) > 1):
			new_name += const[int( len(const) * random.random())]
		else:
			new_name += vowel[int( len(vowel) * random.random())]

	return new_name

def get_name():
  if random.randint(0,1) > 0:
    if random.randint(0,4) > 3:  
      return name_cvcv().title()+name_cvcv()
    else:
      return name_cvcv().title()
  else:
    if random.randint(0,4) > 2:
      return name_cvcvc().title()
    else:
      return name_cvcvc().title()

def get_first_name():
  return name_cvcv().title()

def get_last_name():
  return name_cvcv().title()+name_cvcv()

def name_cvcv():
	#name_cvcv = ""
	return (add_const() + add_vowel() + add_const() + add_vowel() )

def name_cvcvc():
	#name_cvcv = ""
	return (add_const() + add_vowel() + add_const() + add_vowel() + add_const() )


#Generates a word sructure in the form of a string
def word_struc():

	return add_const() + add_vowel() + add_const() + add_const()
	
#adds a vowel
def add_vowel():
	return vowel[(int(len(vowel)  * random.random()))]

#adds a constonant
def add_const():
	return const[(int(len(const)  * random.random()))]