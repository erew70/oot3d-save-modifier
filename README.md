# oot3d-save-modifier

(Currently being worked on!) Ocarina of time 3d save modifier is a tool that mimics the saving of the game with extra options

You can add certain items, weapons, medallions, and more! For example you could add that you have completed the deku tree to your save file, add that you have obtained a GS (gold skulltula), and even obtain things like dungeoun-specific maps, dungeoun-specific compasses, tunics, obtainbles (such as the gerudo token), and spiritual stones. You get the idea. 

What has been implemented so far:

Skip opening cutscene ✅

Intial Saving without corruption:  (CRC checksum gen) ❌

CRC Checksum gen is broken 

How saving works: (crc checksum generation)

Your save file is put through the CRC-16 algorithim with the last 4 bytes removed, (the old checksum) it is then reversed and replaces the old one

For example, my CRC-16 that was just generated is 3F2E, to get it to validate we must flip it to 2E3F, this checksum is filled in the first 2 bytes of the last 4 bytes of your save, the last 2 bytes must be 0's

Contribution:

Send me snapshots (copy of your save file) after you obtain an item, completed a dungeon, or anything that is progressive towards the game. We can compare it to a blank savefile and add it to this modifier. AND PLEASE, PLEASE add a detailed explanation and explain as much as you can (completed deku tree, got slingshot, etc) Making multiple saves with different names is also helpful (might add name editor)

Send me your snapshots at my discord: erew0962
