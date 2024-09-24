import os
import random

def create_folder(folder_name):
    # Check if the folder already exists
    if os.path.exists(folder_name):
        # Remove the existing folder
        os.rmdir(folder_name)
    
    # Create the new folder
    os.mkdir(folder_name)

def save_random_numbers(folder_name):
    # Generate 100 random numbers
    random_numbers = [random.randint(0, 1000) for _ in range(100)]
    
    # Create the file path
    file_path = os.path.join(folder_name, "numbers100.txt")
    
    # Save the random numbers to the file
    with open(file_path, "w") as file:
        for number in random_numbers:
            file.write(str(number) + "\n")

# Ask the user for the folder name
folder_name = input("Enter the folder name: ")

# Create the folder and save the file
create_folder(folder_name)
save_random_numbers(folder_name)