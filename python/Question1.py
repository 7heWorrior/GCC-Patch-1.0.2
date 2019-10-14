# modify this function, and create other functions below as you wish
def question01(intialLevelOfDebt, interestPercentage, repaymentPercentage):
	fixedPayment = intialLevelOfDebt * (repaymentPercentage/100)
	debt = intialLevelOfDebt
	counter = 0
	while debt>50.00:
		debt = debt + debt*(interestPercentage/100)
		debt = debt - fixedPayment
		counter += 1
	answer =  counter * fixedPayment + int(debt) + fixedPayment
	return answer

