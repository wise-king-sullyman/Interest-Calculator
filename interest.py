startingPrinciple = 24180
principleRemaining = startingPrinciple
Rate = .045
Time1 = .3333333333333333333333333333333333333
Time2 = .166666666666666666666666666666666666667
Time3 = 3.5
Payment1 = 4650
Payment2 = 3400

global totalInterest
totalInterest = 0

def interestCalculation(principleRemaining, Rate, Time):
	currentInterestCalc = principleRemaining * Rate * Time
	print "Interest due: " + str(currentInterestCalc) 
	return currentInterestCalc



currentInterest = interestCalculation(principleRemaining, Rate, Time1)
totalInterest = totalInterest + currentInterest
Payment = Payment1 - currentInterest
principleRemaining = principleRemaining - Payment
print "balance 1: " + str(principleRemaining)

currentInterest = interestCalculation(principleRemaining, Rate, Time2)
totalInterest = totalInterest + currentInterest
Payment = Payment2 - currentInterest
principleRemaining = principleRemaining - Payment
print "balance 2: " + str(principleRemaining)

currentInterest = interestCalculation(principleRemaining, Rate, Time3)
totalInterest = totalInterest + currentInterest
totalDue = principleRemaining + currentInterest
totalPayments = totalInterest + startingPrinciple

print
print "Total Interest: " + str(totalInterest)
print "Total Balance Due: " + str(totalDue)
print "Total Payments: " + str(totalPayments)