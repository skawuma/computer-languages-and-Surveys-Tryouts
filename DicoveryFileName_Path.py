import platform
import os

"""
Project: Discovery and File Name and Path
Author: Samuel Kawuma
Description:  Discovers the current OS 
and ask the user for a file name and path,
and convert it according to the system!
"""
#function that returns current Operating System
system=platform.system()

def convert_path(filepath):
   
    """
    Converts a file path based on the current operating system.
    Args:
        filepath (str): The file path to convert.
    
    Returns:
       
        str: The converted file path.
    """
   

    if system == "Windows":
        filepath = filepath.replace("/", "\\")
    elif system == "Darwin" or system == "Linux":
        filepath = filepath.replace("\\", "/")
    return  filepath 

def main():
  
    details ="\nThe operating System is "+ os.name +" And running on "+ system+ " Platform"
    print (details)
    """
    Gets the user's file path and converts it based on the OS. 
    """
    print(" Please Enter the full file path:")
    filepath = input()
    
    converted_path = convert_path(filepath)
    print(f"\nConverted path: {converted_path}")

if __name__ == "__main__":
    main()