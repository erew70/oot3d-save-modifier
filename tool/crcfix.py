def zero_last_4_bytes(filename):
    try:
        # Open the file in read-write binary mode
        with open(filename, 'r+b') as file:
            # Move to the position of the last 4 bytes
            file.seek(-4, 2)
            
            # Read the last 4 bytes
            last_4_bytes = file.read(4)
            
            # Check if the file is at least 4 bytes long
            if len(last_4_bytes) < 4:
                print("The file is too short to modify.")
                return
            
            # Move back to the position to overwrite the last 4 bytes
            file.seek(-4, 2)
            
            # Write 4 zero bytes
            file.write(b'\x00\x00\x00\x00')
            
    
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except IOError as e:
        print(f"An error occurred: {e}")

filename = 'save.bin'

zero_last_4_bytes(filename)