# Import the os module
import os

# Module for reading CSV files
import csv
#---------------------------------------------------

# Read using CSV module
with open("election_data.csv",'r') as csvFile:
    csvreader = csv.reader(csvFile, delimiter=',')
    #Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
#---------------------------------------------------

# Create variables
# candidate's names list
    candidates = []

# Lnumber of votes each candidate receives list
    candidate_votes = []

# percentage of total votes each candidate garners list
    pct_votes = []

# total number of votes counter
    total_votes = 0
#---------------------------------------------------

# Go through each row      
    for row in csvreader:
        total_votes += 1
#---------------------------------------------------

#If the candidate isn't in the list, add name to the list, along with 
#their vote

    #If their name is in the list, only add their vote, not their name again
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            candidate_votes.append(1)
        else:
            index = candidates.index(row[2])
            candidate_votes[index] += 1
#---------------------------------------------------
    
    # Add to percent_votes list 
    for votes in candidate_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        pct_votes.append(percentage)
#---------------------------------------------------    
    
    # Find the winning candidate
        winner = max(candidate_votes)
        index = candidate_votes.index(winner)
        winning_candidate = candidates[index]
#---------------------------------------------------

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(pct_votes[i])} ({str(candidate_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")
#---------------------------------------------------

# Exporting to .txt file
#output = open("election_data_output.txt", "w")
#line1 = "Election Results"
#line2 = "--------------------------"
#line3 = str(f"Total Votes: {str(total_votes)}")
#line4 = str("--------------------------")
#output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
#for i in range(len(candidates)):
    #line = str(f"{candidates[i]}: {str(pct_votes[i])} ({str(candidate_votes[i])})")
    #output.write('{}\n'.format(line))
#line5 = "--------------------------"
#line6 = str(f"Winner: {winning_candidate}")
#line7 = "--------------------------"
#output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
#---------------------------------------------------------------------------

# Specify the file to write to
output_path = os.path.join("election_data_output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

# Write the first row (column headers)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["------------------------------------------"])
    csvwriter.writerow([("Total Votes: " + str(total_votes))])
    csvwriter.writerow(["------------------------------------------"])
    for i in range(len(candidates)):
        csvwriter.writerow([(f"{candidates[i]}: {str(pct_votes[i])} ({str(candidate_votes[i])})")])
    csvwriter.writerow(["------------------------------------------"])
    csvwriter.writerow([(f"Winner: {winning_candidate}")])
    csvwriter.writerow(["------------------------------------------"])


# Write the first row (column headers)
#csvwriter.writerow(["Financial Analysis"])
# Write the second row
#csvwriter.writerow(["------------------------------------------"])
#Write the total months
#csvwriter.writerow(["Total Months: " + str(total_month)])
#write the total revenue
#csvwriter.writerow(["Total: " + "$" + str(totalrev)])
#write the average change
#csvwriter.writerow(["Average Change: " + "$" + str(profit_loss_average)])
#write the max change and change the currency format
#csvwriter.writerow(["Greatest Increase in Profits: " + (month[max_index + 1]) + " " "$" + str(max_result)])
#write the min change and change the currency format
#csvwriter.writerow(["Greatest Decrease in Profits: " + (month[min_index + 1]) + " " "$" + "$" + str(min_result)])