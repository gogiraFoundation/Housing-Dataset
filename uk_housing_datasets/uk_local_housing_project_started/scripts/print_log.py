import os

def print_log(message):
    """
    Centralized function to handle all print statements.
    Logs messages to a file and prints them to the console.
    """
    # Ensure the message is a string before logging
    message_str = str(message)

    # Print the message to the console
    print(message_str)
    
    # Log the message to a file
    #with open(log_file, "a") as f:
     #   f.write(message_str + '\n')