import os
import random
import shutil


def create_folder_and_file():

    while True:

        """Creates a folder and saves a file with 100 random numbers."""

        folder_name = input("Enter the name of the folder to create: ")

        # Check if the folder exists and remove it if necessary
        if os.path.exists(folder_name):

            # Delete an entire directory tree; path must point to a directory
            # (but not a symbolic link to a directory)
            shutil.rmtree(folder_name)

            print(f"Existing folder '{folder_name}' removed.")

        # Create the folder
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created.")

        # Generate 100 random numbers
        random_numbers = [random.randint(1, 1000) for _ in range(100)]
        # Save the random numbers to a file
        file_name = "random_numbers.txt"
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, "w") as file:
            for number in random_numbers:
                file.write(str(number) + "\n")

        print(f"File '{file_name}' saved with 100 random numbers.")
        user_input = input(
            "Do you want to continue (type 'y' to continue  and 'n'to quit): "
        )
        if user_input.lower() == "y":
            continue
        elif user_input.lower() == "n":
            print("Program Exiting....")
            break


if __name__ == "__main__":
    create_folder_and_file()
