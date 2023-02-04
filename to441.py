from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import librosa
import numpy as np
import soundfile as sf


#prints the dependencies
print("Showing Dependencies: \n")
librosa.show_versions()

defaultOutputSampleRate = 44100 #hardcoded samplerate can be made dynamic in future iterations. TODO: Make a Tkinter input to solicit desired output sample rate.
root = tk.Tk() #tkinter boilerplate.
root.withdraw() #hides tkinter window

directory = filedialog.askdirectory() #brings up the directory prompt to ask the user for a directory containing .wav files

wav_files = []

#makes a list of all the .wav files in all of the nested subdirectories
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.wav'):
            wav_files.append(os.path.join(root, file))

#casted the audio data into the form of a numpy array
#this will allow us to also write it out with soundfile
audio_data = np.array(wav_files)

# Create a new folder
##changed src_folder to directory #TODO: Implement a destination folder for processing. Right now it leaves the file hierarchy of samples in the subdirectory intact. If we implemented this, it should be optional because it would put all of the files into a new folder.

#dst_folder = os.path.join(directory, "Processed_Files")
#os.makedirs(dst_folder, exist_ok=True)

#Process files
for index, w in enumerate(audio_data): #enumerated to grab the index

# pulls the filename from the directory path name
  file_name = os.path.splitext(w)[0]

# Load an audio signal, the sr bit is the samplerate (int)
  signal, sr = librosa.load(w, dtype=np.float32)

# resampled is the processed to 44.1kHz, but still needs to be reformated by sf.write() below to be crushed down to a 16 bit pulse code modulation (PCM) format for the hardware synths/grooveboxes/drum-machines that take samples in this target format.
  resampled = librosa.resample(signal, orig_sr=sr, target_sr=defaultOutputSampleRate)

  print("Processing " + file_name + " now.")



# Save the audio signal with 16-bit PCM data type appropriate for hardware samplers that use this standard like the yamaha dtx multi 12, roland mc-101, mc-707, etc.!
  sf.write(file_name + "_16bit_44100Hz.wav", resampled, 44100, subtype='PCM_16')
  print("File Processed!")

print("Finished! Program Terminated.")
