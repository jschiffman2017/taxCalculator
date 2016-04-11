def oneTaxPlan(income):
	income = int(income)
	adjustedIncome = income - 9500
	if adjustedIncome <= 2650:
		tax = 0
		return tax
	elif adjustedIncome > 2650 and adjustedIncome <= 27850:
		tax = (adjustedIncome - 2650) * .15
		return tax
	elif adjustedIncome > 27850 and adjustedIncome <= 59900:
		tax = ((adjustedIncome - 27850) * .28) + ((27850 - 2650) * .15)
		return tax
	elif adjustedIncome > 59900 and adjustedIncome <= 134200:
		tax = ((adjustedIncome - 59900) * .31) + ((59900 - 27850) * .28) + ((27850 - 2650) * .15)
		return tax
	elif adjustedIncome > 134200 and adjustedIncome <= 289950:
		tax = ((adjustedIncome - 134200) * .36) + ((134200 - 59900) * .31) + ((59900 - 27850) * .28) + ((27850 - 2650) * .15)
		return tax
	else:
		tax = ((adjustedIncome - 289950) * .396) + ((289950 - 134200) * .36) + ((134200 - 59900) * .31) + ((59900 - 27850) * .28) + ((27850 - 2650) * .15)
		return tax



def twoTaxPlan(income):
	income = int(income)
	adjustedIncome = income - 9500
	if adjustedIncome <= 8025:
		tax = adjustedIncome * .1
		return tax
	elif adjustedIncome > 8025 and adjustedIncome <= 32550:
		tax = ((adjustedIncome - 8025) * .15) + 802.5
		return tax
	elif adjustedIncome > 32550 and adjustedIncome <= 78850:
		tax = ((adjustedIncome - 32550) * .25) + ((32550 - 8025) * .15) + 802.5
		return tax
	elif adjustedIncome > 78850 and adjustedIncome <= 164550:
		tax = ((adjustedIncome - 78850) * .28) + ((78850 - 32550) * .25) + ((32550 - 8025) * .15) + 802.5
		return tax
	elif adjustedIncome > 164550 and adjustedIncome <= 357700:
		tax = ((adjustedIncome - 164550) * .33) + ((164550 - 78850) * .28) + ((78850 - 32550) * .25) + ((32550 - 8025) * .15) + 802.5
		return tax
	else:
		tax = ((adjustedIncome - 357700) * .35) + ((357700 - 164550) * .33) + ((164550 - 78850) * .28) + ((78850 - 32550) * .25) + ((32550 - 8025) * .15) + 802.5
		return tax



def threeTaxPlan(income):
	income = int(income)
	adjustedIncome = income - 9500
	if adjustedIncome <= 8700:
		tax = adjustedIncome * .1
		return tax
	elif adjustedIncome > 8700 and adjustedIncome <= 35350:
		tax = ((adjustedIncome - 8700) * .15) + 870
		return tax
	elif adjustedIncome > 35350 and adjustedIncome <= 85650:
		tax = ((adjustedIncome - 35350) * .25) + ((35350 - 8700) * .15) + 870
		return tax
	elif adjustedIncome > 85650 and adjustedIncome <= 178650:
		tax = ((adjustedIncome - 85650) * .28) + ((85650 - 35350) * .25) + ((35350 - 8700) * .15) + 870
		return tax
	elif adjustedIncome > 178650 and adjustedIncome <= 388350:
		tax = ((adjustedIncome - 178650) * .33) + ((178650 - 85650) * .28) + ((85650 - 35350) * .25) + ((35350 - 8700) * .15) + 870
		return tax
	else:
		tax = ((adjustedIncome - 388350) * .35) + ((388350 - 178650) * .33) + ((178650 - 85650) * .28) + ((85650 - 35350) * .25) + ((35350 - 8700) * .15) + 870
		return tax
		
		

#---------- MAIN PROGRAM ----------

print("Welcome to the tax calculator.")
income = input("How much gross income did you earn last year? ")
income = int(income)
one = int(oneTaxPlan(income))
two = int(twoTaxPlan(income))
three = int(threeTaxPlan(income))
print("")

print("Results for the 2000 plan:")
print("Taxes owed: ${}".format(one))
print("Percent of gross: {}%".format((one / income) * 100))
print("Net income: ${}".format(income - one))
print("")

print("Results for the 2008 plan:")
print("Taxes owed: ${}".format(two))
print("Percent of gross: {}%".format((two / income) * 100))
print("Net income: ${}".format(income - two))
print("")


print("Results for the 2014 plan:")
print("Taxes owed: ${}".format(three))
print("Percent of gross: {}%".format((three / income) * 100))
print("Net income: ${}".format(income - three))
print("")


if one < two and one < three:
	print("You save the most money in the 2000 tax plan.")
elif two < one and two < three:
	print("You save the most money in the 2008 tax plan.")
elif three < one and three < two:
	print("You save the most money in the 2014 tax plan.")