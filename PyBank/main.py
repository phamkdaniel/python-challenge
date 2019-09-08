import os
import sys
import csv

line = "-" *28

# main function
def main():
    # paths to input and output files
    input_file = os.path.join(sys.path[0],"Resources", "budget_data.csv")
    output_file = os.path.join(sys.path[0], "budget_analysis.txt") 

    # initalize variables
    month_count = 0
    net_total = 0
    greatest_increase = 0
    greatest_decrease = 0
    total_change = 0
    last_budget = 0

    with open(input_file) as f:
        # reads csv and skips header row
        budget_data = csv.reader(f, delimiter = ",")
        next(budget_data, None)

        for row in budget_data:
            # counts months and tracks running total of budget
            month_count += 1
            net_total += int(row[1])

            # computes budget change from last month and checks if greater or less than last stored budget change
            diff = int(row[1]) - last_budget
            if diff > greatest_increase: 
                greatest_increase = diff
                great_inc_date = row[0]
            elif diff < greatest_decrease:
                greatest_decrease = diff
                great_dec_date = row[0]

            # keeps a running total of budget changes as long as two months have passed
            if month_count > 1:
                total_change += diff

            # stores budget to compute difference with next month's budget
            last_budget = int(row[1])

    # stores results
    output = (
        f"Financial Analysis\n"
        f"{line}\n"
        f"Total Months: {month_count}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${total_change / (month_count-1):.2f}\n"
        f"Greatest Increase in Profits: {great_inc_date} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {great_dec_date} (${greatest_decrease})\n"
    )

    # print results to terminal
    print(output)

    # print results to text file
    with open(output_file, "w") as txt_file:
        txt_file.write(output)

if __name__ == "__main__": main()
