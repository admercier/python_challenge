import os
import csv

inpath = os.path.join('Resources/budget_data.csv')
outpath = os.path.join('Analysis/budget_analysis.txt')

inpath

months = 0
revenue = 0
old_revenue = 0
revenue_change = 0

month_l = []
revenue_l = []

max_increase = ["",0]
max_decrease = ["",9999999999]

with open(inpath) as revenue_d:
    csvreader = csv.reader(revenue_d,delimiter=",")
    csvheader = next(csvreader) 
    
    first_row= next(csvreader)
    months = months + 1
    revenue = revenue + int(first_row[1])
    old_revenue = int(first_row[1])
    
    for row in csvreader: 
            months = months + 1
            revenue = revenue + int(first_row[1])  
            revenue_change = int(row[1]) - old_revenue
            old_revenue = int(row[1])
            month_l = month_l + [row[0]]
            revenue_l = revenue_l + [revenue_change]
            
            if (revenue_change > max_increase[1]):
                max_increase[1] = revenue_change
                max_increase[0] = row[0]
            if (revenue_change < max_decrease[1]):
                max_decrease[0] = row[0]
                max_decrease[1] = revenue_change

avg_rev = sum(revenue_l)/len(revenue_l)

outcome = (f"Total Months: {months}\n"
            f"Total Revenue: {revenue}\n"
            f"Average Revenue Change: ${avg_rev}\n"
            f"Greatest Increase in Revenue: {max_increase[0]} ${max_increase[1]}\n"
            f"Greatest Decrease in Revenue: {max_decrease[0]} ${max_decrease[1]}\n")

print(outcome)

outpath

with open(outpath,"w") as txt_file:
    txt_file.write(outcome)