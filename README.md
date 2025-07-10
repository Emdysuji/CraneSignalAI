# 🏗️ Crane Signal AI: Real-Time Crane Gesture Recognition

> A real-time AI-powered system for recognizing standardized crane hand signals from live video using deep learning and TensorFlow Lite.

---

## 🔍 Overview

**Crane Signal AI** is a computer vision system that recognizes **crane hand signals** from real-time webcam video or recorded clips. It uses a lightweight [MoViNet](https://arxiv.org/abs/2103.11511) model trained on labeled gesture data and optimized with TensorFlow Lite for deployment on edge devices or safety systems.

---

## 💡 Use Cases

### ✅ Current Applications

- 🦺 **Construction Safety Monitoring**  
  Detect ambiguous or unsafe crane hand signals in real-time.

- 📹 **Crane Operation Assistance**  
  Acts as a second set of eyes for crane operators in noisy or high-risk environments.

- 🧪 **Dataset Labeling Tool**  
  Helps auto-label crane videos for more accurate training and testing datasets.

### 🚀 Future Possibilities

- 🏗️ **AI-Controlled Cranes**  
  Autonomous cranes responding to recognized hand signals.

- 🧠 **Smart Surveillance**  
  Detect safety violations using existing site security camera feeds.

- 🕹️ **Remote-Controlled Systems**  
  Use gesture inputs to teleoperate or monitor crane activity remotely.

- 👓 **AR Glasses Integration**  
  Display detected signal instructions live through smart glasses or helmet HUDs.

---

## 🧠 Model Architecture

| Component         | Details               |
|------------------|------------------------|
| Base Model       | MoViNet-A2             |
| Input Resolution | 224x224                |
| Frames per Clip  | 30                     |
| Mode             | Offline & Streaming    |
| Format           | TensorFlow Lite (.tflite) |

---

## ⚙️ Features

- ✅ Real-time crane gesture classification
- ✅ Streaming mode (frame-by-frame with memory states)
- ✅ Offline clip-based inference mode
- ✅ TFLite support for edge deployment
- ✅ Web API with live video overlay (via Flask)
- ✅ Dataset augmentation with Albumentations
- ✅ Visualization tools for predictions

---

## 📁 Project Structure

```bash
CraneSignalAI/
├── API/
│   ├── api_live_base.py        # Offline clip-based video API
│   ├── api_live_stream.py      # Streaming (frame-by-frame) video API
│
├── Models/
│   ├── model_3_b30.tflite      # Base (non-streaming) model
│   ├── model_3.tflite          # Streaming inference model
│
├── utils/
│   ├── cut_video_clips.py      # Slice video into short labeled segments
│   ├── augment_videos.py       # Run augmentation on dataset
│
├── crane_model_training.ipynb  # Full model training + export notebook
├── requirements.txt
└── README.md
```


---

## 🧑‍💻 Author

**Michael-David Osuji**  
Machine Learning Engineer / Mechatronics Enthusiast  
📫 [LinkedIn](https://www.linkedin.com/in/yourprofile) • [GitHub](https://github.com/yourusername)

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [TensorFlow Model Garden – MoViNet](https://www.kaggle.com/code/minhdunk/movinet-streaming#Convert-to-TF-Lite)  
- [Albumentations](https://albumentations.ai) – for high-performance image augmentations
- [Crane Hand Signals Video Used For Dataset](https://www.youtube.com/results?search_query=crane+hand+signals) 

---

