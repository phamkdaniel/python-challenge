import os
import sys
import csv

line = "-" *25

# main function
def main():
    # paths to input and output files
    input_file = os.path.join(sys.path[0], "election_data.csv")
    output_file = os.path.join(sys.path[0], "election_analysis.txt") 

    # create dictionary to store candidate names and tallies
    vote_tally = {}
    total_votes = 0

    with open(input_file) as f:
        # reads csv file and skips header row
        vote_data = csv.reader(f, delimiter = ",")
        next(vote_data, None)

        for row in vote_data:
            # increment total_votes for each vote found
            total_votes += 1

            # if candidate key exists, increment corresponding tally
            if row[2] in vote_tally:
                vote_tally[row[2]] +=1
            # if key not found, make new candidate key and tally
            else:
                vote_tally[row[2]] = 1

    win_count = 0
    candidate_info = ""
    for name in vote_tally:
        # store tally info for each candidate
        candidate_info += f'{name}: {vote_tally[name] / total_votes *100:.3f}% ({vote_tally[name]})\n'

        # determine winner by finding maximal tally
        if vote_tally[name] > win_count:
            win_count = vote_tally[name]
            winner = name

    # stores results
    result = (
        f"Election Results\n"
        f"{line}\n"
        f"Total Votes: {total_votes}\n"
        f"{line}\n"
        f"{candidate_info}"        
        f"{line}\n"
        f"Winner: {winner}\n"
        f"{line}\n"
    )

    # print results to terminal
    print(result)

    # print results to text file
    with open(output_file, "w") as txt_file:
        txt_file.write(result)

if __name__ == "__main__": main()
