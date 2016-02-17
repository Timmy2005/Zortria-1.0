a = raw_input(' Choose between length, weight or volume: ')
if a == 'Length' or a == 'length':
	print"Choose a measurement from this list for your starting unit(what you are going "
	print "to convert), and one for your ending unit(what you are going to convert to),"
	print "then put in a number(how many of that unit there are)."
	print"(English)Inches"
	print"(English)Feet"
	print"(English)Yards"
	print"(English)Miles"
	print"(Metric)Millimeters"
	print"(Metric)Centimeters"
	print"(Metric)Decimeters"
	print"(Metric)Meters"
	print"(Metric)Kilometers"
	starting_unit = raw_input().lower()
	ending_unit = raw_input().lower()
	number = raw_input()
	print starting_unit
	print ending_unit
	print number
	number_2 = float(number)
	print number_2
	if starting_unit == "inches":
		if ending_unit == "feet":
			print(number_2 / 12)  	
		if ending_unit == "yards":
			print(number_2 / 36)
		if  ending_unit == "miles":
			print(number_2 / 63360)
	elif starting_unit == "feet":
		if ending_unit == "inches":
			print(number_2 * 12)
		if  ending_unit == "yards":
			print(number_2 / 3)
		if ending_unit == "miles":
			print(number_2 / 5280)
	elif starting_unit == "yards":
		if ending_unit == "inches":
			print(number_2 * 36)
		if ending_unit == "feet":
			print(number_2 * 3)
		if ending_unit == "miles":
			print(number_2 / 1760)
	elif starting_unit == "miles":		
		if ending_unit == "inches":
			print(number_2 * 63360)
		if ending_unit == "feet":
			print(number_2 * 5280)
		if ending_unit == "yards":
			print(number_2 * 1760)
	elif starting_unit == "millimeters":
		if ending_unit == "centimeters":
			print(number_2 / 10)
		if ending_unit == "decimeters":
			print(number_2 / 100)
		if ending_unit == "meters":
			print(number_2 / 1000)
		if ending_unit == "kilometers":
			print(number_2 / 1000000)
	elif starting_unit == "centimeters":
		if ending_unit == "millimeters":
			print(number_2 * 10)
		if ending_unit == "decimeters":
			print(number_2 / 10)	
		if ending_unit == "meters":
			print(number_2 / 100)
		if ending_unit == "kilometers":
			print(number_2 / 100000)
	elif starting_unit == "decimeters":
		if ending_unit == "millimeters":
			print(number_2 * 100)
		if ending_unit == "centimeters":
			print(number_2 * 10)
		if ending_unit == "meters":
			print(number_2 / 10)
		if ending_unit == "kilometers":
			print(number_2 / 10000)
	elif starting_unit == "kilometers":
		if ending_unit == "millimeters":
			print(number_2 * 1000000)
		if ending_unit == "centimeters":
			print(number_2 * 100000)
		if ending_unit == "decimeters":
			print(number_2 * 10000)
		if ending_unit == "meters":
			print(number_2 * 1000)
		
		else:
			print"Ooops!"
	else: 
		print"Ooops!"
	
	
	
elif a == 'Weight' or a == 'weight':
	print"Choose a measurement from this list for your starting unit(what you are going "
	print "to convert), and one for your ending unit(what you are going to convert to),"
	print "then put in a number(how many of that unit there are)."
	print"(English)Ounces"
	print"(English)Pounds"
	print"(English)Tons"
	print"(Metric)Grams"
	print"(Metric)Kilograms"
	starting_unit_2 = raw_input().lower()
	ending_unit_2 = raw_input().lower()
	number_3 = raw_input()
	number_4 = float(number_3)
	if starting_unit_2 == "ounces":
		if ending_unit_2 == "pounds":
			print(number_4 / 16)
		if ending_unit_2 == "tons":
			print(number_4 / 32000)
	elif starting_unit_2 == "pounds":
		if ending_unit_2 == "ounces":
			print(number_4 * 16)
		if ending_unit_2 == "tons":
			print(number_4 / 2000)
	elif starting_unit_2 == "tons":
		if ending_unit_2 == "ounces":
			print(number_2 * 32000)
		if ending_unit_2 == "pounds":
			print(number_4 * 2000)
	elif starting_unit_2 == "milligrams":
		if ending_unit_2 == "grams":
			print(number_4 / 1000)
		if ending_unit_2 == "kilograms":
			print(number_4 / 1000000)
	elif starting_unit_2 == "grams":
		if ending_unit_2 == "milligrams":
			print(number_4 * 1000)
		if ending_unit_2 == "kilograms":
			print(number_4 / 1000)
	elif starting_unit_2 == "kilograms":
		if ending_unit_2 == "milligrams":
			print(number_4 * 1000000)
		if ending_unit_2 == "grams":
			print(number_4 * 1000)
		
		else:
			print"Ooops"	
	else:
		print"Ooops!"
	
	
		
elif a == 'Volume' or a == 'volume':
	print"Choose a measurement from this list for your starting unit(what you are going "
	print "to convert), and one for your ending unit(what you are going to convert to),"
	print "then put in a number(how many of that unit there are)."
	print"(English)Teaspoons"
	print"(English)Tablespoons"
	print"(English)Fluid ounces"
	print"(English)Cups"
	print"(English)Pints"
	print"(English)Quarts"
	print"(English)Gallons"
	print"(Metric)Milliliters"
	print"(Metric)Liters"
	starting_unit_3 = raw_input().lower()
	ending_unit_3 = raw_input().lower()
	number_5 = raw_input()
	number_6 = float(number_5)
	if starting_unit_3 == "teaspoons":
		if ending_unit_3 == "tablespoons":
			print(number_6 / 3)
		if ending_unit_3 == "fluid ounces":
			print(number_6 / 6)
		if ending_unit_3 == "cups":
			print(number_6 / 48)
		if ending_unit_3 == "pints":
			print(number_6 / 96)
		if ending_unit_3 == "quarts":
			print(number_6 / 192)
		if ending_unit_3 == "gallons":
			print(number_6 / 768)
	elif starting_unit_3 == "tablespoons":
		if ending_unit_3 == "teaspoons":
			print(number_6 * 3)
		if ending_unit_3 == "fluid ounces":
			print(number_6 / 2)
		if ending_unit_3 == "cups":
			print(number_6 / 16)
		if ending_unit_3 == "pints":
			print(number_6 / 32)
		if ending_unit_3 == "quarts":
			print(number_6 / 64)
		if ending_unit_3 == "gallons":
			print(number_6 / 256)
	elif starting_unit_3 == "Fluid ounces":
		if ending_unit_3 == "teaspoons":
			print(number_6 * 6)
		if ending_unit_3 == "tablespoons":
			print(number_6 * 2)
		if ending_unit_3 == "cups":
			print(number_6 / 8)
		if ending_unit_3 == "pints":
			print(number_6 / 16)	
		if ending_unit_3 == "quarts":
			print(number_6 / 32)
		if ending_unit_3 == "gallons":
			print(number_6 / 128)
	elif starting_unit_3 == "cups":
		if ending_unit_3 == "teaspoons":
			print(number_6 * 48)
		if ending_unit_3 == "tablespoons":
			print(number_6 * 16)
		if ending_unit_3 == "fluid ounces":
			print(number_6 * 8)
		if ending_unit_3 == "pints":
			print(number_6 / 2)
		if ending_unit_3 == "quarts":
			print(number_6 / 4)
		if ending_unit_3 == "gallons":
			print(number_6 / 16)
	elif starting_unit_3 == "pints":
		if ending_unit_3 == "teaspoons":
			print(number_6 * 96)
		if ending_unit_3 == "tablespoons":
			print(number_6 * 32)
		if ending_unit_3 == "fluid ounces":
			print(number_6 * 16)
		if ending_unit_3 == "cups":
			print(number_6 * 2)
		if ending_unit_3 == "quarts":
			print(number_6 / 2)
		if ending_unit_3 == "gallons":
			print(number_6 / 8)
	elif starting_unit_3 == "quarts":
		if ending_unit_3 == "teaspoons":
			print(number_6 * 192)
		if ending_unit_3 == "tablespoons":
			print(number_6 * 64)
		if ending_unit_3 == "fluid ounces":
			print(number_6 * 32)
		if ending_unit_3 == "cups":
			print(number_6 * 4)
		if ending_unit_3 == "pints":
			print(number_6 * 2)
		if ending_unit_3 == "gallons":
			print(number_6 / 4)
	elif starting_unit_3 == "gallons":
		if ending_unit_3 == "teaspoons":
			print(number_6 * 768)
		if ending_unit_3 == "tablespoons":	
			print(number_6 * 256)
		if ending_unit_3 == "fluid ounces":
			print(number_6 * 128)
		if ending_unit_3 == "cups":
			print(number_6 * 64)	
		if ending_unit_3 == "pints":
			print(number_6 * 8)
		if ending_unit_3 == "quarts":
			print(number_6 * 4)
	elif starting_unit_3 == "milliliters":
		if ending_unit_3 == "liters":
			print(number_6 / 1000)
	elif starting_unit_3 == "liters":
		if ending_unit_3 == "milliliters":
			print(number_6 * 1000)
		
		else:
			print"Ooops!"
	else:
		print"Ooops!"	
else:
	print"Oo