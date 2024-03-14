def write_to_file():
  """Writes content to a new file named 'my_file.txt' in write mode."""
  try:
    with open("my_file.txt", "w") as file:
      file.write("This is the first line of text.\n")
      file.write("Here's a line with a number: 42\n")
      file.write("And a final line.\n")
    print("Successfully wrote to 'my_file.txt'.")
  except PermissionError:
    print("Error: Insufficient permissions to write to the file.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
  finally:
    # This block will always execute, even if an exception occurs.
    print("File writing operation completed.")

def read_and_display():
  """Reads the contents of 'my_file.txt' and displays them on the console."""
  try:
    with open("my_file.txt", "r") as file:
      contents = file.read()
      print("Contents of 'my_file.txt':\n", contents)
  except FileNotFoundError:
    print("Error: 'my_file.txt' not found.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

def append_to_file():
  """Opens 'my_file.txt' in append mode and adds new lines of text."""
  try:
    with open("my_file.txt", "a") as file:
      file.write("Appending this line.\n")
      file.write("Another line for good measure.\n")
      file.write("The final line of appended text.\n")
    print("Successfully appended to 'my_file.txt'.")
  except PermissionError:
    print("Error: Insufficient permissions to append to the file.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Function calls for execution
write_to_file()
read_and_display()
append_to_file()
read_and_display()  # Read again to show appended content
