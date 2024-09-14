def inject_bytes(filename, start_offset, end_offset, bytes_to_inject):
    # Open the file in binary read-write mode
    with open(filename, 'r+b') as file:
        # Read the existing content of the file
        file_content = file.read()
        
        # Make sure start_offset and end_offset are within the file's bounds
        if start_offset > len(file_content):
            raise ValueError("Start offset is beyond the end of the file.")
        if end_offset > len(file_content):
            end_offset = len(file_content)  # Adjust end_offset if it's beyond the file size

        # Create new content
        new_content = file_content[:start_offset] + bytes_to_inject + file_content[end_offset:]
        
        # Go to the beginning of the file and overwrite it
        file.seek(0)
        file.write(new_content)
        file.truncate()  # Truncate the file to the new length if necessary

