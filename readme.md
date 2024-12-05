# 🗣️ Speech-to-Text Using VOSK

### 🚀 Transform Audio into Text with Precision and Speed

This project demonstrates how to build a real-time **Speech-to-Text** system using the **VOSK** library. Whether you're creating transcription tools, virtual assistants, or voice-controlled systems, this implementation ensures high accuracy and efficiency.

---
![Demo GIF](https://github.com/user-attachments/assets/255c2c3d-99dc-4752-8469-6ef64f42e267)

## 📋 Features

- **Real-Time Transcription**: Converts live audio into text instantly.
- **Lightweight & Offline**: Works offline without requiring heavy resources.
- **High Accuracy**: Supports multiple languages with pre-trained models.
- **Customizable**: Easily adapt the code for different use cases.

---

## 🛠️ Setup

### Prerequisites

1. **Python (3.6 or higher)**: Ensure Python is installed on your machine.
2. **Create a Virtual Environment (optional but recommended)**:
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
3. **Install Dependencies**:
   - Install the required Python libraries:
     ```bash
     pip install -r requirements.txt
     ```

4. **Download a VOSK Model**:
   - Download a pre-trained VOSK model from the official VOSK model page: [VOSK Models](https://alphacephei.com/vosk/models).
   - **Models available**:
     | Model Name                       | Languages     | Link                                                                                       |
     | -------------------------------- | ------------- | ------------------------------------------------------------------------------------------ |
     | `vosk-model-small-en-us-0.15`    | English (US)  | [Download](https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15)                |
     | `vosk-model-small-hi-in-0.22`    | Hindi (IN)    | [Download](https://alphacephei.com/vosk/models/vosk-model-small-hi-in-0.22)                |
     | `vosk-model-en-us`               | English (US)  | [Download](https://alphacephei.com/vosk/models/vosk-model-en-us)                           |
     | `vosk-model-small-fr-fr-0.15`    | French        | [Download](https://alphacephei.com/vosk/models/vosk-model-small-fr-fr-0.15)                |
     | `vosk-model-small-de-de-0.15`    | German        | [Download](https://alphacephei.com/vosk/models/vosk-model-small-de-de-0.15)                |

   - Extract the downloaded model into a directory (e.g., `vosk-model-small-en-us-0.15`).

---

## 📂 Project Structure

```
├── SpeechToTextUsingVosk.py        # Main Python file to run the application
├── models                         # Directory containing the downloaded models
    └── vosk-model-small-en-us-0.15
        ├── README
        ├── am
        │   └── final.mdl
        ├── conf
        │   ├── mfcc.conf
        │   └── model.conf
        ├── graph
        │   ├── Gr.fst
        │   ├── HCLr.fst
        │   ├── disambig_tid.int
        │   └── phones
        │       └── word_boundary.int
        └── ivector
            ├── final.dubm
            ├── final.ie
            ├── final.mat
            ├── global_cmvn.stats
            ├── online_cmvn.conf
            └── splice.conf
├── readme.md                      # Project documentation
└── requirements.txt               # Python dependencies
```

---

## 🚀 Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YourUsername/speech-to-text-vosk.git
   cd speech-to-text-vosk
   ```

2. **Set Model Path**:
   Replace the `MODEL_PATH` in `SpeechToTextUsingVosk.py` with the path to your downloaded VOSK model directory.

3. **Run the Application**:
   ```bash
   python SpeechToTextUsingVosk.py
   ```

4. **Start Speaking**:
   Speak into your microphone and watch as your speech is converted into text in real-time!

---

## 🧩 How It Works

1. **Audio Capture**: The `sounddevice` library is used to capture live audio input from the microphone.
2. **Processing with VOSK**: The captured audio is processed in real-time by VOSK's speech recognizer.
3. **Real-Time Output**: The system outputs both partial and final transcriptions as you speak.

---

## 📈 Performance Tips

- **For Faster Transcription**: Use smaller models such as `vosk-model-small-en-us-0.15` for real-time transcription on low-resource systems.
- **For Higher Accuracy**: Download larger models for better accuracy, such as `vosk-model-en-us`.
- **Ensure a Quiet Environment**: Background noise can affect transcription accuracy. Ensure you're in a quiet space for optimal results.

---

## 📋 Example Output

### Input:
_"Hello, welcome to the VOSK speech-to-text demo!"_

### Output:
```json
{
  "text": "hello welcome to the vosk speech to text demo"
}
```

---

## 📚 Resources

- [VOSK Documentation](https://alphacephei.com/vosk/)
- [Pre-Trained Models](https://alphacephei.com/vosk/models)
- [SoundDevice Library](https://python-sounddevice.readthedocs.io/)

---

## 🤝 Contribution

Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests.  

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🧑‍💻 About the Creator

Developed with 💡 by **Anubhav Chaturvedi** (@NetHyTech).  
Check out more open-source projects on [GitHub](https://github.com/AnubhavChaturvedi-GitHub).  

