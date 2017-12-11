# Dependencies
import os
import csv

# Initiate the variable to rerun program on another file
more_calculations ='y'

while more_calculations == 'y':

  # Collects the user's input for the file to be used for running the relevant calculations
  filename = input("What is the name of the file you want to use for the calculations? (please remember to include the file extension) ")

  # Creates the path for the relevant file
  bank_csv = os.path.join("raw_data", filename)

  # open and read csv
  with open(bank_csv, newline="") as csvfile:
       csvreader = csv.reader(csvfile, delimiter=",")
  # Skip the first row of the csv
  next(csv_reader, None)

  # Calculating the total number of months included in the dataset
  total_months = len(open(csvreader).readline())
  # alternate way
  # for row in csvreader:
  #      total_months +=1
  print(total_months)

  # Calculating the total amount of revenue gained over the entire period
  total_revenue = sum(x[1] for x in csvreader)
  print(total_revenue)

  # Calculating the average change in revenue between months over the entire period
  Average_change = total_revenue/total_months

  # Calculating the greatest increase in revenue (date and amount) over the entire period
  increase_revenue = max(x[1] for x in csvreader)

  # Calculating the greatest decrease in revenue (date and amount) over the entire period
  decrease_revenue = min(x[1] for x in csvreader)

  # Printing the results of the financial analysis

  print("Financial Analysis")

  print("------------------")

  print("Total Months: " + str(total_months))

  print("Total Revenue: $" + str(total_revenue))

  print("Average Revenue Change: $" +  str(Average_change))

  print("Greatest Increase in Revenue: " + str(increase_revenue))

  print("Greatest Decrease in Revenue: " + str(decrease_revenue))

  print("-------------------")


  more_calculations = input("Would you like to conduct these calculations on another file? (y)es or (n)o  ")
