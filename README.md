# 🎶 Audio File Processor 🎶

This script enables users to batch process `.wav` files, resampling them to a target sample rate of 44.1kHz and saving them with a 16-bit PCM data type. This format is suitable for various hardware samplers, including Yamaha DTX Multi 12, Roland MC-101, MC-707, and more.

## 🚀 Features:

- 📁 Batch process `.wav` files in selected directory and nested subdirectories.
- 🎚 Resample audio files to 44.1kHz.
- 📉 Save processed files with 16-bit PCM data type.

## 🧰 Prerequisites:

Ensure you have the following Python libraries installed:

- `librosa`
- `numpy`
- `soundfile`
- `tkinter`

You can install the required packages using `pip`:

```bash
pip install librosa numpy soundfile tkinter

🚀 How to Use:

    Run the script:

bash

python to441.py

    A directory prompt will pop up, asking you to select a directory containing .wav files you'd like to process.
    The script will then process each .wav file, resampling and converting it as needed.
    Processed files will be saved with the "_16bit_44100Hz.wav" suffix in their original locations.

📣 Output:

The script provides real-time feedback on the terminal, including:

    Displaying library dependencies and versions.
    Informative prompts for each file being processed.
    Completion message once all files are processed.

🛠️ Future Improvements (TODO):

    Make the output sample rate dynamic with a GUI input option.
    Provide an optional destination folder for processed files while retaining the original file hierarchy.

🙏 Contributing:

Feel free to fork this repository and submit PRs for any improvements or features you think would be beneficial. Your contributions are always welcome!
📜 License: 

This project is open-source and available under the MIT License.
🤖 Author: 

cafeTechne
