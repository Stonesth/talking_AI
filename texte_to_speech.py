from TTS.api import TTS
from openai import OpenAI
import pygame
import time
import torch
import os
import re
import concurrent.futures

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

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

while True:
    # je voudrais supprimer tout les fichier output_x.wav.played avant de commencer
    # Delete all output files before starting
    for file in os.listdir():
        if file.startswith("output_") and file.endswith(".wav.played"):
            os.remove(file)

    user_prompt = input("> ")

    completion = client.chat.completions.create(
        model="model-identifier",
        messages=[
            {"role": "system", "content": "Tu es un écrivain d'histoire phantastique. Tu écrit tes histoire avec des phrases courtes et simples. "},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
    )

    answer = completion.choices[0].message.content
    print(answer)

    # Increment the file name
    file_number = len(os.listdir()) // 2  # Divide by 2 because each output file has a corresponding .played file
    file_name = f"output_{file_number}.txt"

    # Save the question and answer to the file
    with open(file_name, "a") as file:
        file.write(f"Question: {user_prompt}\n")
        file.write(f"Answer: {answer}\n")


    # Split the answer into sentences
    sentences = re.split(r'[.?!]', answer)

    # je voudrais savoir se qui se trouve dans sentences un par un 
    print("Sentences:", sentences)
    print("Length of sentences:", len(sentences))
    
    # Process and play each sentence sequentially
    for j, sentence in enumerate(sentences):
        if sentence:
            file_number = str(j).zfill(2)  # Add leading zeros if necessary
            tts.tts_to_file(text=sentence, speaker=speaker, language=language, file_path=f"output_{file_number}.wav")


