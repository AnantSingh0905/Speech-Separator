import warnings
import os
import shutil
import torchaudio
import librosa
import soundfile as sf
from speechbrain.inference.separation import SepformerSeparation as separator
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning, module="speechbrain")

# Initialize models
sep_model = separator.from_hparams(source="speechbrain/sepformer-wsj03mix", savedir='pretrained_models/sepformer-wsj03mix')
enhance_model = separator.from_hparams(source="speechbrain/sepformer-wham-enhancement", savedir='pretrained_models/sepformer-wham-enhancement')

# Define the result directory
result_dir = 'result'

# Create or clear the result directory
if os.path.exists(result_dir):
    shutil.rmtree(result_dir)  # Remove existing directory
os.makedirs(result_dir)  # Create a new one

def separate_sources(input_audio_path):
    """Separates sources from the input audio and saves each separated file."""
    est_sources = sep_model.separate_file(input_audio_path)
    separated_files = []
    
    for idx in range(est_sources.shape[2]):
        output_path = f"source_{idx + 1}.wav"
        torchaudio.save(output_path, est_sources[:, :, idx].detach().cpu(), 8000)
        separated_files.append(output_path)
    
    return separated_files

def enhance_audio(audio_file):
    """Enhances the separated audio file and saves the enhanced result."""
    est_sources = enhance_model.separate_file(audio_file)
    enhanced_path = f"enhanced_{audio_file}"
    torchaudio.save(enhanced_path, est_sources[:, :, 0].detach().cpu(), 8000)
    
    return enhanced_path

def upsample_audio(audio_file, upsample_factor=2):
    """Upsamples the audio file and saves the result."""
    y, sr = librosa.load(audio_file, sr=None)
    new_sr = sr * upsample_factor
    y_upsampled = librosa.resample(y, orig_sr=sr, target_sr=new_sr)
    
    upsampled_path = os.path.join(result_dir, f"upsampled_{os.path.basename(audio_file)}")  # Save in result folder
    sf.write(upsampled_path, y_upsampled, new_sr)
    
    return upsampled_path

def process_audio(input_audio_path):
    """Processes the audio file by separating, enhancing, and upsampling."""
    processed_files = []
    enhanced_files = []  # List to store paths of enhanced files

    # Step 1: Separate sources
    separated_files = separate_sources(input_audio_path)
    update_progress(33)  # Update progress after separation

    # Step 2: Enhance and upsample each separated file
    for audio_file in separated_files:
        # Enhance each separated audio file
        enhanced_file = enhance_audio(audio_file)
        enhanced_files.append(enhanced_file)  # Store enhanced file path
        update_progress(66)  # Update progress after enhancement
        
        # Upsample the enhanced audio file
        upsample_audio(enhanced_file)  # Use the enhanced file for upsampling
        update_progress(100)  # Update progress after upsampling

        processed_files.append(audio_file)  # Collect processed file paths

    # Clean up: Delete separated source files
    for audio_file in separated_files:
        if os.path.exists(audio_file):
            os.remove(audio_file)  # Remove separated source files

    # Clean up: Delete enhanced files
    for enhanced_file in enhanced_files:
        if os.path.exists(enhanced_file):
            os.remove(enhanced_file)  # Remove enhanced audio files

    return processed_files

def update_progress(value):
    """Update the progress bar value."""
    progress_bar['value'] = value
    app.update_idletasks()  # Update the UI immediately

def upload_file():
    """Handle file upload."""
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
    if file_path:
        file_name = os.path.basename(file_path)  # Get the file name from the path
        file_label.config(text=f"Processing: {file_name}")

        # Hide the upload button and show the progress bar
        upload_button.pack_forget()
        progress_bar.pack(pady=20)  # Show the progress bar

        # Start processing in a separate thread
        threading.Thread(target=process_audio_and_update, args=(file_path,)).start()

    else:
        messagebox.showwarning("Warning", "No file selected.")

def process_audio_and_update(input_audio_path):
    """Process audio and update progress."""
    processed_files = process_audio(input_audio_path)
    
    # Complete processing
    update_progress(100)  # Set progress to 100%
    
    # Show a message box with the processed files
    if processed_files:
        messagebox.showinfo("Processing Complete", "Audio processing is done!")
    else:
        messagebox.showwarning("Warning", "No files processed.")

# Create the main application window
app = tk.Tk()
app.title("Three Person Speech Separator")
app.geometry("500x300")  # Change this to your desired size

# Set a light background color
app.configure(bg="#f0f0f0")

# Create a label to display uploaded file name
file_label = tk.Label(app, text="No file uploaded", padx=10, pady=10, bg="#f0f0f0", font=("Arial", 12))
file_label.pack(pady=20)  # Add some vertical space

# Create an upload button with a style
upload_button = tk.Button(app, text="Upload Audio File", command=upload_file, bg="#4CAF50", fg="white", font=("Arial", 12), relief="raised")
upload_button.pack(pady=20)  # Add some vertical space

# Create a progress bar
progress_bar = ttk.Progressbar(app, orient='horizontal', length=300, mode='determinate')
progress_bar.pack(pady=20)
progress_bar['value'] = 0  # Initialize progress bar

# Hide the progress bar initially
progress_bar.pack_forget()

# Run the application
app.mainloop()
