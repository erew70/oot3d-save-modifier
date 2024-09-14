from util.data.data_offsets import *
from util.byter import *
from util.cks_rw import *

file_path = "save.bin"

def show_menu():
    print("Welcome to the OOT3D Save Editor!")
    print("1. Skip Cutscene")
    print("3. exit")

def skip_scene():
   # inject_bytes(file_path, skip_opening_offsets_1, skip_opening_offsets_2, skip_opening_cutscene_bytes_1) this causes partial save wiping???
    inject_bytes(file_path,skip_opening_offsets_2, skip_opening_offsets_3, skip_opening_cutscene_bytes_2)
    inject_bytes(file_path,skip_opening_offsets_4, skip_opening_offsets_5, skip_opening_cutscene_bytes_3)
    print("done")


def main():
    while True:
        show_menu()
        
        try:
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == 1:
            skip_scene()
            crc = getCRC()
            flipped = flip_crc(crc)
            print(flipped)
            inject_new_crc(file_path, flipped)


        if choice == 2:
            break

main()



# calculate_and_insert_checksum(file_path)
