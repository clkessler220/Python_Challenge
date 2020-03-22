# Import the os module
import os

# Module for reading CSV files
import csv
    
#Read using CSV module
with open("budget_data.csv",'r') as csvFile:
    csvreader = csv.reader(csvFile, delimiter=',')
    #Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
#---------------------------------------------------        
    
    #Create variables to hold the following empty lists:   
    month = []
    profit_loss_list = []

    #this is the starting number of the revenue
    totalrev = 0
#--------------------------------------------------

    #Go through each row
    for row in csvreader:
        #append data from the row 
        month.append(str(row[0]))        
        profit_loss_list.append(int(row[1]))

        #len counts the number of months
        total_month=len(month)
 #--------------------------------------------------

 # Create total revenue, use the profit_loss_list, it starts with 0 (the beginning balance in totalrev), and adds the running total      
    for x in profit_loss_list:
        totalrev = totalrev + x
    #----------------------------------------------------

#Create variable for average changes empty list
    average_change = []
    #this is the starting number of the average change
    previous_month_amount = 0
   
    for x in range(len(profit_loss_list)):
        if x == 0:
            previous_month_amount = profit_loss_list[x]           
        else:
            monthly_change = profit_loss_list[x] - previous_month_amount
            average_change.append(monthly_change)

            previous_month_amount = profit_loss_list[x]
    
    length = len(average_change)
    total = sum(average_change)
    profit_loss_average = round(total / length, 2)
#----------------------------------------------------

max_result = max(average_change)
max_index = average_change.index(max_result)

min_result = min(average_change)
min_index = average_change.index(min_result)
#----------------------------------------------------

#Write to terminal
print("Financial Analysis")
print("----------------------------------------------")
print("Total Months: ", total_month)
print("Total: ", "$" + format(totalrev,".0f"))
print("Average Change ", "$" + format(profit_loss_average,".0f"))
print("Greatest Increase in Profits:", (month[max_index + 1]), " " + "$" + format(max_result,".0f"))
print("Greatest Decrease in Profits:", (month[min_index + 1]), " " + "$" + format(min_result,".0f"))
#----------------------------------------------------

# Specify the file to write to
output_path = os.path.join("budget_data_output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Financial Analysis"])
    # Write the second row
    csvwriter.writerow(["------------------------------------------"])
    #Write the total months
    csvwriter.writerow(["Total Months: " + str(total_month)])
    #write the total revenue
    csvwriter.writerow(["Total: " + "$" + str(totalrev)])
    #write the average change
    csvwriter.writerow(["Average Change: " + "$" + str(profit_loss_average)])
    #write the max change and change the currency format
    csvwriter.writerow(["Greatest Increase in Profits: " + (month[max_index + 1]) + " " "$" + str(max_result)])
    #write the min change and change the currency format
    csvwriter.writerow(["Greatest Decrease in Profits: " + (month[min_index + 1]) + " " "$" + "$" + str(min_result)])

