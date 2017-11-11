line_number = 0
with open('/Users/andre/Documents/Visual Studio 2017/Projects/DiveIntoPython3App1/DiveIntoPython3App1/favorite-people.txt', encoding='utf-8') as a_file:
    for a_line in a_file:
        line_number += 1
        print('{:>4} {}'.format(line_number, a_line.rstrip()))
