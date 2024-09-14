# modify save to skip the opening cutscene
skip_opening_cutscene_bytes_1 = bytes.fromhex("BB 00 00 00 01 00 00 00 00 00 00 00 00 80 00 00")
skip_opening_cutscene_bytes_2 = bytes.fromhex("00 00 30 00 30 00 00 00 00 00 00 00 1A 00 00 00")
skip_opening_cutscene_bytes_3 = bytes.fromhex("09 00 00 00 0A 00 00 00 10 00 00 00 02 00 00 00")

skip_opening_offsets_1 = 0x00
skip_opening_offsets_2 = 0x00

skip_opening_offsets_2 = 0x40
skip_opening_offsets_3 = 0x50

skip_opening_offsets_4 = 0x13C0
skip_opening_offsets_5 = 0x13D0