import shutil
import os
import glob

from termcolor import colored

# List available playlists
print(colored("Available .m3u playlists: ", "green"))
for file in glob.glob("*.m3u"):
    print(file, end="   ")
print("\n")

# Enter the playlist name. If there's no such playlist - throw NameError
playlist_name = input("Enter playlist name (including extension): ")
if not os.path.isfile(playlist_name):
    raise NameError("Playlist doesn't exist.")

# Enter the folder name, check if it exists, and if not create it
output_folder_name = input("Enter output folder name (\"output\" by default): ")
if output_folder_name == '':
    output_folder_name = "output"
if os.path.exists(output_folder_name):
    print(output_folder_name + " exists.")
else:
    os.mkdir(output_folder_name)

playlist = open(playlist_name).read().split('\n')

# Iterate through the playlist, copying music files in process
for song in playlist:
    try:
        shutil.copy2(song, output_folder_name)
        print("Copied song " + song)
    except:
        if song == "":
            pass
        else:
            print(colored("Can't find song \"" + song + "\"", "green"))

print("Done.")
