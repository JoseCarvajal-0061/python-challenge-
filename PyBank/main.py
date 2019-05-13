import os 
import csv

bank_csv = os.path.join("." "PyBank", "budget_data.csv") 
    
with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimeter = ",")
    csvheader = next(csvfile)


for row in csvreader: 

                total = 0
                total_months = 0
                initial_profit = 0 
                monthly_Change = 0
                greatest_increase = 0
                greatest_decrease = 0 
                average_Change= 0

#total months in the data set 
        #Total_Months = 0 
                total_months = total_months + 1
    
#total profits in the data set
        #Total = 0 
                total = total + int(bank_csv[1])

#Monthly Change 
                change = total - initial_profit 

monthly_Change = change/total_months


if monthly_Change > 0:
                greatest_increase = average_Change
                greatest_increase = row[0]

elif monthly_Change < 0:
                greatest_decrease = average_Change
                greatest_decrease = row[0]

average_Change = monthly_Change/ (total_months -1)

print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(total_months))
print("Total Profits: " + "$" + str(total))
print("Average Change: " + "$" + str(int(average_Change)))
print("Greatest Increase in Profits: "("$" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: "("$" + str(greatest_decrease) + ")")
print("----------------------------------------------------------")

with open(os.path.join("PyBank", "Output", "financial_analysis.txt"), "w") as txtfile:
    txtfile.write(output)

