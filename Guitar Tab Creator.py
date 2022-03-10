print("Welcome to the Guitar Tab Creator!")
print("This program allows you to create a guitar tab and output it to a .txt file.")
print("The program asks you to enter a fret for each string until you enter 'q'.")
print("Press return if the string is ignored.")
print("")

file_name = input("Enter name of .txt file to save tab (new file will be created if it doesn't already exist): ")
print("")

quit = ""
first_string = "|"
second_string = "|"
third_string = "|"
fourth_string = "|"
fifth_string = "|"
sixth_string = "|"

width = int(input("Enter spacing desired between each note: "))

first_string += "-" * width
second_string += "-" * width
third_string += "-" * width
fourth_string += "-" * width
fifth_string += "-" * width
sixth_string += "-" * width

while (quit != "q" and quit != "Q"):
    first_input = input("Enter a fret for the 1st string: ")
    second_input = input("Enter a fret for the 2nd string: ")
    third_input = input("Enter a fret for the 3rd string: ")
    fourth_input = input("Enter a fret for the 4th string: ")
    fifth_input = input("Enter a fret for the 5th string: ")
    sixth_input = input("Enter a fret for the 6th string: ")

    lengths = []
    lengths.append(len(first_input))
    lengths.append(len(second_input))
    lengths.append(len(third_input))
    lengths.append(len(fourth_input))
    lengths.append(len(fifth_input))
    lengths.append(len(sixth_input))

    max_length = max(lengths)

    first_string += first_input + ("-" * (width + (max_length - len(first_input))))
    second_string += second_input + ("-" * (width + (max_length - len(second_input))))
    third_string += third_input + ("-" * (width + (max_length - len(third_input))))
    fourth_string += fourth_input + ("-" * (width + (max_length - len(fourth_input))))
    fifth_string += fifth_input + ("-" * (width + (max_length - len(fifth_input))))
    sixth_string += sixth_input + ("-" * (width + (max_length - len(sixth_input))))


    quit = input("Enter 'q' to quit or return to continue: ")
print("")

first_string += "|"
second_string += "|"
third_string += "|"
fourth_string += "|"
fifth_string += "|"
sixth_string += "|"

print("Output saved to .txt file: ")
print(first_string)
print(second_string)
print(third_string)
print(fourth_string)
print(fifth_string)
print(sixth_string)

file_name = file_name + ".txt"

with open(file_name, "w") as outfile:
    print(first_string, file=outfile)
    print(second_string, file=outfile)
    print(third_string, file=outfile)
    print(fourth_string, file=outfile)
    print(fifth_string, file=outfile)
    print(sixth_string, file=outfile)
