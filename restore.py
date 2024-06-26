import pygame
import time
import os


# Get the list of all output files in the directory
output_files = [file for file in os.listdir() if file.startswith("output_") and file.endswith(".wav.played")]
# Sort the output files in ascending order
output_files.sort()
# Play each output file sequentially
for file in output_files:
    # je voudrais modifier le nom du fichier output_x.wav.played en output_x.wav
    # Rename the file to indicate that it can been played in the future
    os.rename(file, file.replace(".played", ""))
        
            