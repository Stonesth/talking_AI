from TTS.api import TTS
import os
import re
import torch

directory = '/Users/thononpierre/Documents/Projet/Python/Project/IA/dark_personal_live'  # Replace with the actual directory path


# Paramètres de génération
speaker = 'Ludvig Milivoj'
language = 'fr'

# Get device
# device = "cpu"  # Or "cuda" if you have a compatible GPU
# print("Device:", device)
if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

print(f"Using device: {device}")


# Init TTS with the target model name
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False).to(device)

for filename in os.listdir(directory):
    if filename.startswith('output_') and filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as file:
            content = file.read()
            # Do something with the file content
            print(content)

            # Split the answer into sentences
            sentences = re.split(r'[$]', content)

            # Process and play each sentence sequentially
            for j, sentence in enumerate(sentences):
                if sentence:
                    file_number = str(j).zfill(2)  # Add leading zeros if necessary
                    tts.tts_to_file(text=sentence, speaker=speaker, language=language, file_path=f"output_{file_number}_{filename}.wav")