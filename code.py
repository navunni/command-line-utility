import argparse
import os 
import mutagen 


parser = argparse.ArgumentParser(description='A command line utility for managing music files')

parser.add_argument('-p', '--path', help='Path to the music directory')
parser.add_argument('-t', '--tag', help='Tag to update (e.g. artist, album, title)')
parser.add_argument('-v', '--value', help='Value to set for the tag')

# Parse the arguments
args = parser.parse_args()

# Check if the path is valid
if not os.path.exists(args.path):
    print("Error: Invalid path")
    exit()

# Loop through the music files in the directory
for file in os.listdir(args.path):
    # Check if the file is an audio file
    if file.endswith(".mp3") or file.endswith(".flac"):
        # Load the audio file using Mutagen
        audio_file = mutagen.File(os.path.join(args.path, file))
        # Update the specified tag with the new value
        audio_file[args.tag] = args.value
        # Save the changes to the audio file
        audio_file.save()

print("update is successful")
