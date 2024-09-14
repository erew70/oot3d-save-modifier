import crcmod
crc16 = crcmod.mkCrcFun(0x18005, 0, True)


def get_hex_bytes(file_path):
    try:
        with open(file_path, 'rb') as file:
            
            file_content = file.read()
            
            
            hex_bytes = file_content.hex()
            
            return hex_bytes
    except FileNotFoundError:
        print(f"Error: The file at {file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


file_path = 'save.bin' 
hex_bytes = get_hex_bytes(file_path)


def getCRC():
    ecrc = crc16(bytes.fromhex(f"{hex_bytes}"))
    the_crc = hex(ecrc)
    if the_crc.startswith('0x'):
        return the_crc[2:]
    else:
        print("not a crc!")

# hash = int.to_bytes(ecrc, 2)

def flip_crc(crc):
    if len(crc) < 4:
        return crc  # If text length is less than 4, it can't be flipped in the given manner
    # Perform the flip: move the first two characters to the end
    return crc[2:] + crc[:2]

def inject_new_crc(save_file, crc):
    # Convert the hex string into bytes
    # Assuming crc is a string like '171b'
    crc_bytes = bytes.fromhex(crc)
    
    # Open the file in binary read-write mode
    with open(save_file, 'r+b') as f:
        # Move to the end of the file and read the last 4 bytes
        f.seek(-4, 2)
        last_4_bytes = f.read(4)
        
        if len(last_4_bytes) < 4:
            raise ValueError("File is too short to modify last 4 bytes")
        
        # Create the new last 4 bytes with the modified first 2 bytes
        new_last_4_bytes = crc_bytes + last_4_bytes[2:]
        
        # Move to the position of the last 4 bytes and write the new bytes
        f.seek(-4, 2)
        f.write(new_last_4_bytes)

