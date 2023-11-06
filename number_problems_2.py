import math

def to_natural(n):
    try:
        if type (n):
            n = float (n)
        if n == round (n):
            if n >= 0 :
                return n
            return False
        return False
    except ValueError:
        return False    
def roman_numeral(n):
	if not to_natural(n):
		raise ValueError
	if n > 3999 or n < 0:
		pass	
	remainder = 0
	thousands = n // 1000
	remainder = n % 1000
	fivehundreds = remainder // 500
	remainder = remainder % 500
	onehundreds = remainder // 100
	remainder = remainder % 100
	fiftys = remainder // 50
	remainder = remainder % 50
	tens = remainder // 10
	remainder = remainder % 10
	if remainder == 9:
		fives = "Nine"
		remainder=0
	fives = remainder // 5
	ones = remainder % 5
	numeral = ""
	for i in range(0,thousands):
		numeral = numeral + "M"
	for i in range(0,fivehundreds):
		numeral = numeral + "D"
	for i in range(0,onehundreds):
		numeral = numeral + "C"
	for i in range(0,fiftys):
		numeral = numeral + "L"
	for i in range(0,tens):
		numeral = numeral + "X"
	if fives == "Nine":
		numeral = numeral + "IX"
	else:
		for i in range(0,fives):
			numeral = numeral + "V"
	if ones == 4:
		numeral = numeral + "IV"
	else:
		for i in range(0,ones):
			numeral = numeral + "I"
	return numeral
pass

def total_roman(n):
	numeral_list = []
	numeral_list = [*n]
	print(numeral_list.count("I"))
	total = 0
	for i in range(0,numeral_list.count("I")):
		total = total + 1
	for i in range(0,numeral_list.count("V")):
		total = total + 5
	for i in range(0,numeral_list.count("X")):
		total = total + 10
	for i in range(0,numeral_list.count("L")):
		total = total + 50
	for i in range(0,numeral_list.count("L")):
		total = total + 100
	for i in range(0,numeral_list.count("D")):
		total = total + 500
	for i in range(0,numeral_list.count("M")):
		total = total + 1000
	return(total)
	pass
total_roman("MDIVVI")
def chisel_strokes(n):
	numeral_list = []
	numeral_list = [*n]
	print(numeral_list.count("I"))
	total = 0
	for i in range(0,numeral_list.count("I")):
		total = total + 1
	for i in range(0,numeral_list.count("V")):
		total = total + 2
	for i in range(0,numeral_list.count("X")):
		total = total + 2
	for i in range(0,numeral_list.count("L")):
		total = total + 2
	for i in range(0,numeral_list.count("C")):
		total = total + 2
	for i in range(0,numeral_list.count("D")):
		total = total + 3
	for i in range(0,numeral_list.count("M")):
		total = total + 3
	return(total)