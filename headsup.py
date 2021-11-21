import random

# Name of the file to read in!
FILE_NAME = 'headups.txt'

def main():
    #Create an empty list that will store all the lines of the file
    list_of_lines = []
    #Another way of saying file = open(FILE_NAME)
    with open(FILE_NAME) as file:
        #Iterate through each line
        for line in file:
            #Add/Append each line to the list_of_lines
            list_of_lines.append(line)
    #Gets the length of the list
    number_of_lines = len(list_of_lines)
    #Prompts the user to press enter
    prompt_use = input("Press Enter Please!")
    #Running a while loop until 0 is entered
    while prompt_use != "0":
        #Generating a random number between 0 and the length of the list so that
        #We can choose a line at random
        random_number = random.randint(0, number_of_lines-1)
        #Storing the random element of list_of_lines into random_choice
        random_choice = list_of_lines[random_number]
        #Displaying the word so that the user can guess!
        print("The word is: " + random_choice)
        #Removing that element from the list so that it does not appear again
        list_of_lines.pop(random_number)
        #Altering the length of the list to avoid "Out of index" errors
        number_of_lines -= 1
        #Prompting the user to press enter again or enter 0 to end the game and updating the while loop
        prompt_use = input("Press Enter Please or Enter 0 to exit the game!")


if __name__ == '__main__':
    main()