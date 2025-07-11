import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("wrong usage")

    # TODO: Read database file into a variable
    row = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for rows in reader:
            row.append(rows)
    # print(row[0])
    hehe = list(row[0].keys())
    hehe.pop(0)
    # print(hehe)
    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as file:
        x = file.read()
        # print(x)

    # TODO: Find longest match of each STR in DNA sequence
    res = []
    for thing in hehe:
        a = longest_match(x, thing)
        res.append(a)
    # print(res)
    # print(a,b,c)
    # TODO: Check database for matching profiles
    guy = True
    for name in row:
        for x in range(len(hehe)):
            if int(name[hehe[x]]) != res[x]:
                guy = False
        if guy == True:
            print(name["name"])
            return
        else:
            guy = True
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
