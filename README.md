# Approach to Solve the Problem of Speech Separation

**Project Overview:**
This project addresses the challenge of speech separation, aiming to isolate individual speech signals from a mixture of audio sources. This technique is valuable in scenarios with multiple speakers or background noise, where enhancing each speaker's intelligibility is crucial. Applications span across telecommunications, hearing aids, and automated transcription services.

**Project Focus:**
This project is specifically designed for two-person and three-person conversations. Separating speech in these scenarios requires models that can accurately differentiate overlapping voices while maintaining the clarity of each speaker’s audio.

**Models Used:**
1. Sepformer-WHAM-Enhancement
Enhances audio quality by separating speech from noisy backgrounds. Utilizes advanced signal processing for improved intelligibility in noisy environments, making it suitable for real-world applications.

2. Sepformer-WHAMR16K
Focused on separating speech in two-person scenarios. Employs a robust architecture to effectively distinguish between overlapping voices, ensuring high accuracy in audio separation.

3. Sepformer-WSJ03Mix
Optimized for three-person speech separation. Incorporates additional complexity to manage overlapping audio streams, ensuring clear isolation of each speaker’s voice.

**Model Capabilities:**
These models are capable of performing speech separation in both noisy and quiet backgrounds. They leverage deep learning techniques to analyze audio signals and separate voices effectively, making them ideal for real-world applications where background noise can interfere with clarity.

Approach to Speech Separation:
1. Initial Audio Processing
Two-Person Speech Separation: Utilizes the Sepformer-WHAMR16K model to process audio, handling two overlapping speech signals, even in complex acoustic conditions.
Three-Person Speech Separation: Uses the Sepformer-WSJ03Mix model to manage the added complexity of three simultaneous speakers, accurately isolating each voice.
2. Enhancement of Audio Quality
After initial separation, outputs from the models are enhanced by the Sepformer-WHAM-Enhancement model. This step reduces background noise and improves voice clarity, ensuring the separated audio is intelligible and of high quality.

3. Upsampling
Enhanced audio signals undergo upsampling to increase the sampling rate and capture finer sound details. This improves audio resolution, making the output suitable for further analysis or playback without loss of quality.

4. Storage of Results
Processed audio data is stored in a designated results folder for organized access, allowing easy retrieval for further evaluation or application integration.

**Installation and Usage:**
- Clone the repository.
- Install dependencies from requirements.txt.
- Run the script by specifying the audio input path and desired output folder.
- Future Enhancements:
-Expanding to multi-speaker separation with noise classification.
-Adding real-time speech enhancement capabilities.

**Future Enhancements:**
- Expanding to multi-speaker separation with noise classification.
- Adding real-time speech enhancement capabilities.


