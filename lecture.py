import pygame
import time
import os

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)

while True:
#     # je voudrais supprimer tout les fichier output_x.wav avant de commencer
#     # Delete all output files before starting
#     for file in os.listdir():
#         if file.startswith("output_") and file.endswith(".wav"):
#             os.remove(file)

    # je voudrais donc jouer le ouput_x.wav en commencant par le output_0.wav,
    # Get the list of all output files in the directory
    for file in os.listdir():

        if file.startswith("output_") and file.endswith(".wav"):

            play_audio(file)
            # je voudrais modifier le nom du fichier output_x.wav en output_x.wav.played
            # Rename the file to indicate that it has been played
            os.rename(file, f"{file}.played")
            

    # print("Output files:", output_files)

    # # Sort the output files in ascending order
    # output_files.sort()

    # # Play each output file sequentially
    # for file in output_files:
    #     # afficher le nom du fichier
    #     print(file)

    #     play_audio(file)
    #     # je voudrais modifier le nom du fichier output_x.wav en output_x.wav.played
    #     # Rename the file to indicate that it has been played
    #     os.rename(file, f"{file}.played")







    # # Process and play each sentence in parallel
    # with concurrent.futures.ThreadPoolExecutor() as executor:

        

        
        
    #     # Submit TTS tasks for each sentence
    #     tts_tasks = [executor.submit(tts.tts_to_file, text=sentence, speaker=speaker, language=language, file_path=f"output_{j}.wav") for j, sentence in enumerate(sentences) if sentence]
        
    #     # Check the status of each TTS task
    #     for task in tts_tasks:
    #         # Check if the task is done
    #         # if task.done():
    #         #     print("Task is done")

    #         # Je voudrais donc jouer le ouput_x.wav en commencant par le output_0.wav, 
    #         # mais je ne veux pas attendre spécialement que toutes les tts_tasks soit finie. 
    #         # Je veux juste traiter les output_x.wav de mnière séquentielle

    #         # Get the number of completed TTS tasks
    #         completed_tasks = sum(task.done() for task in tts_tasks)

    #         # Check if any TTS tasks are completed
    #         print("Completed tasks:", completed_tasks)
    #         if completed_tasks > 0:
    #             # Play the audio for each completed task in sequence
    #             for i in range(completed_tasks):
    #                 output_file = tts_tasks[i].result()
    #                 play_audio(output_file)
    #                 # Increment the file number
    #                 file_number = i + 1
    #                 next_file = f"output_{file_number}.wav"
    #                 # Check if the next file exists
    #                 if os.path.exists(next_file):
    #                     play_audio(next_file)
    #         else:
    #             print("No completed TTS tasks yet")
    #         # else:
    #         #     print("Task is still running")


        # # Play the audio for each sentence as soon as it is ready
        # for i, future in enumerate(concurrent.futures.as_completed(tts_tasks)):
        #     output_file = future.result()
        #     play_audio(output_file)
        #     # Increment the file number
        #     file_number = i + 1
        #     next_file = f"output_{file_number}.wav"
        #     # Check if the next file exists
        #     if os.path.exists(next_file):
        #         play_audio(next_file)
        

        # # Check if the previous 5 audio files are ready
        # ready_files = [f"output_{j}.wav" for j in range(i-4, i+1)]
        # if all(os.path.exists(file) for file in ready_files):
        #     # Play the audio for each file
        #     for file in ready_files:
        #         play_audio(file)

    # # Run TTS
    # tts.tts_to_file(text=answer, speaker=speaker, language=language, file_path="output.wav")
    # # tts.tts_to_file(text=answer, file_path="output.wav")
    # play_audio("output.wav")











    # # Init TTS with the target model name
    # tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False).to(device)
    # # tts = TTS(model_name="tts_models/en/jenny/jenny", progress_bar=False).to(device)

    # # Split the answer into chunks
    # chunk_size = 100  # Set the desired chunk size
    # chunks = [answer[i:i+chunk_size] for i in range(0, len(answer), chunk_size)]


    # # Process and play each chunk in parallel
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     # Submit TTS tasks for each chunk
    #     tts_tasks = [executor.submit(tts.tts_to_file, text=chunk, speaker=speaker, language=language, file_path=f"output_{i}.wav") for i, chunk in enumerate(chunks)]
        
    #     # Play the audio for each chunk as soon as it is ready
    #     for future in concurrent.futures.as_completed(tts_tasks):
    #         output_file = future.result()
    #         play_audio(output_file)



    # # Run TTS
    # tts.tts_to_file(text=answer, speaker=speaker, language=language, file_path="output.wav")
    # # tts.tts_to_file(text=answer, file_path="output.wav")

    # play_audio("output.wav")
