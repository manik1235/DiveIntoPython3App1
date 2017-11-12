line_number = 0
with open('/Users/andre/Documents/Visual Studio 2017/Projects/DiveIntoPython3App1/DiveIntoPython3App1/favorite-people.txt', encoding='utf-8') as a_file:
    import time
    for a_line in a_file:
        line_number += 1
        time.sleep(0.5)
        print('{:>6} {}'.format(line_number, a_line.rstrip()))
        print('{:>5} {}'.format(line_number, a_line.rstrip()))
        print('{:>4} {}'.format(line_number, a_line.rstrip()))
        print('{:>3} {}'.format(line_number, a_line.rstrip()))
        print('{:>2} {}'.format(line_number, a_line.rstrip()))
        print('{:>1} {}'.format(line_number, a_line.rstrip()))
        
with open('test.log', mode='w', encoding='utf-8') as a_file:
    a_file.write('test succeeded')
