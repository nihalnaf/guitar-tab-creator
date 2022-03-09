import sys

print("Welcome to the Guitar Tab Creator!")
print("This program allows you to create a guitar tab and output it to a .txt file.")
print("The program asks you to enter a fret for each string until you enter 'q'.")
print("Press return if the string is ignored.")
print("")

file_name = input("Enter name of .txt file to save tab (new file will be created if it doesn't already exist): ")
print("")

quit = ''
first_string = "----"
second_string = "----"
third_string = "----"
fourth_string = "----"
fifth_string = "----"
sixth_string = "----"

while (quit != 'q' and quit != 'Q'):
    first_input = input("Enter a fret for the 1st string: ")
    first_string += first_input + ("-" * (5 - len(first_input)))

    second_input = input("Enter a fret for the 2nd string: ")
    second_string += second_input + ("-" * (5 - len(second_input)))

    third_input = input("Enter a fret for the 3rd string: ")
    third_string += third_input + ("-" * (5 - len(third_input)))

    fourth_input = input("Enter a fret for the 4th string: ")
    fourth_string += fourth_input + ("-" * (5 - len(fourth_input)))

    fifth_input = input("Enter a fret for the 5th string: ")
    fifth_string += fifth_input + ("-" * (5 - len(fifth_input)))

    sixth_input = input("Enter a fret for the 6th string: ")
    sixth_string += sixth_input + ("-" * (5 - len(sixth_input)))

    quit = input("Enter 'q' to quit or return to continue: ")
print("")
print("Output saved to .txt file: ")
print(first_string)
print(second_string)
print(third_string)
print(fourth_string)
print(fifth_string)
print(sixth_string)

file_name = file_name + ".txt"

with open(file_name, 'w') as outfile:
    print(first_string, file=outfile)
    print(second_string, file=outfile)
    print(third_string, file=outfile)
    print(fourth_string, file=outfile)
    print(fifth_string, file=outfile)
    print(sixth_string, file=outfile)