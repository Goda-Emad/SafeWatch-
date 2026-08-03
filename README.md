# 🛡️ SafeWatch — Smart Human Action Recognition & Surveillance System

> **"See More. Understand Faster. Act Now."**

[![Streamlit App](https://img.shields.io/badge/Live%20App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://fa4rjpbkpefpcs9zdzbpcw.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-TFLite-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![License](https://img.shields.io/badge/License-MIT-63d28c?style=for-the-badge)](LICENSE)

---

## 📌 Overview

**SafeWatch** is an AI-powered surveillance system that classifies **8 human actions in real time** from a single image — using a fine-tuned **MobileNetV2** model deployed as a full-stack web application.

Traditional CCTV cameras record everything but understand nothing. SafeWatch bridges that gap: it automatically detects dangerous behavior (e.g., **fighting**), triggers an instant **email alert** to security personnel, and logs the incident with a timestamped screenshot — all through a clean, bilingual web dashboard.

🌐 **Live Demo:** [https://fa4rjpbkpefpcs9zdzbpcw.streamlit.app/](https://fa4rjpbkpefpcs9zdzbpcw.streamlit.app/)

---

## 🚨 The Problem

| Issue | Reality |
|---|---|
| 🎥 Cameras See Everything | But cannot interpret what is happening |
| 👁️ Human Monitoring is Impossible | Security teams cannot watch hundreds of feeds at once |
| ⚠️ Incidents Go Undetected | Fights and falls are only noticed after the damage is done |
| ⏱️ Delayed Response | Every second of delay increases risk to human safety |

> There is no automated, intelligent system that understands human behavior in real time inside existing CCTV infrastructure — **until now.**

---

## ✅ What SafeWatch Does

- 🧠 **Classifies 8 human actions** from a single image instantly
- 📁 Works via **image upload** OR **live camera capture**
- 🥊 **Automatically detects fighting** and triggers an alert
- 📧 **Sends email notification** to security admin in under 1 second
- 🌐 **Full web dashboard** — supports Arabic and English
- 🌙 **Dark & Light mode** — deployed and accessible from any device

---

## 🎯 Recognized Action Classes

| Class | Description |
|---|---|
| 🥊 Fighting | Aggressive physical contact between individuals |
| 🏃 Running | High-speed locomotion |
| 😴 Sleeping | Horizontal resting posture |
| 🤗 Hugging | Close body contact, arms around another person |
| 💃 Dancing | Rhythmic, expressive body movement |
| 📱 Texting | Hand raised toward face, looking at screen |
| 🍽️ Eating | Hand raised to mouth with object |
| 🚴 Cycling | Seated posture with wheel/bike structure visible |

---

## 🧠 Model & Training

### Architecture — MobileNetV2 + Transfer Learning

```
Input: (224, 224, 3) — RGB Image
    ↓
MobileNetV2 Base (pretrained on ImageNet)
    ├── Initial Conv2D (32 filters)
    ├── 17 Inverted Residual Blocks
    └── Final Conv2D (1280 filters)
    ↓
GlobalAveragePooling2D  →  1280 values
    ↓
Dense (128, ReLU)
    ↓
Dropout (0.3)
    ↓
Dense (8, Softmax)  →  Predicted Class + Confidence Score
```

### Why MobileNetV2?

| Model | Parameters | Accuracy | Speed |
|---|---|---|---|
| VGG16 | 138M | 92.7% | Slow |
| ResNet50 | 25M | 93.0% | Medium |
| **MobileNetV2** | **3.4M** | **92.0%** | **Fast ✅** |

> MobileNetV2 achieves near-identical accuracy to VGG16 using **40× fewer parameters** — the clear choice for web deployment.

### Two-Phase Training

| Phase | Epochs | Frozen Layers | Learning Rate | Result |
|---|---|---|---|---|
| ❄️ Feature Extraction | 1–20 | All MobileNetV2 layers | 0.001 | ~78% test accuracy |
| 🔥 Fine-Tuning | 21–50 | Last 30 layers unfrozen | 0.0001 | **~82% test accuracy** |

### Hyperparameters

| Parameter | Value |
|---|---|
| Optimizer | Adam |
| Loss Function | Categorical CrossEntropy |
| Epochs | 50 (20 + 30) |
| Batch Size | 16 |
| Input Size | 224×224×3 |
| Dropout | 0.3 |

---

## 📊 Dataset

**Source:** [Human Action Recognition — Kaggle](https://www.kaggle.com/datasets/shashankrapolu/human-action-recognition-dataset)

| Detail | Value |
|---|---|
| Original dataset | 15 classes × 714 images = 10,710 images |
| Classes used | **8 classes × 714 images = 5,712 images** |
| Training set (85%) | 4,855 images (~606 per class) |
| Testing set (15%) | 857 images (~107 per class) |
| Image format | JPG / PNG |
| Input size | 224×224 pixels |

> We selected the **8 most visually distinct and security-relevant** actions from 15 available classes to maximize model accuracy.

---

## 📈 Model Performance

**Overall Test Accuracy: 82%**

| Class | Accuracy | Correct / Total |
|---|---|---|
| 🚴 Cycling | **93%** | 100 / 107 |
| 🍽️ Eating | **92%** | 98 / 107 |
| 🤗 Hugging | **86%** | 92 / 107 |
| 🏃 Running | **83%** | 89 / 107 |
| 💃 Dancing | 76% | 81 / 107 |
| 🥊 Fighting | 74% | 79 / 107 |
| 📱 Texting | 72% | 77 / 107 |
| 😴 Sleeping | 69% | 74 / 107 |

**Key confusion patterns:**
- Sleeping ↔ Hugging — similar horizontal body posture
- Fighting ↔ Running/Dancing — motion blur and similar body angles
- Texting ↔ Eating — same hand-raised-to-face gesture

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────┐
│         User (Any Device / Browser)     │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│       Streamlit Web Application         │
│  ┌──────────┐ ┌──────────┐ ┌─────────┐ │
│  │   Home   │ │  Upload  │ │  Camera │ │
│  │Dashboard │ │  Image   │ │  Live   │ │
│  └──────────┘ └──────────┘ └─────────┘ │
│     Dark/Light Mode │ AR/EN Toggle      │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│           Backend Processing            │
│  preprocess.py → predict.py → alert.py  │
│            → email_sender.py            │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│     MobileNetV2 TFLite Quantized        │
│   Input: (1, 224, 224, 3)               │
│   Output: 8 probability scores          │
│   Inference: < 500ms                    │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│             Alert System                │
│  Fighting > threshold → Screenshot      │
│  → Log to CSV → Send Email to Admin     │
└─────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
SafeWatch/
├── app.py                  # Main Streamlit application entry point
├── src/
│   ├── preprocess.py       # Image validation, resize to 224×224, normalize
│   ├── predict.py          # Load TFLite model, run inference, return scores
│   ├── alert.py            # Fighting detection threshold logic
│   └── email_sender.py     # HTML email with screenshot attachment
├── model/
│   └── model_unquant.tflite  # Quantized MobileNetV2 TFLite model
├── pages/
│   ├── home.py             # Home dashboard — session stats & overview
│   ├── upload.py           # Image upload → prediction + confidence bars
│   └── camera.py           # Live camera capture → real-time analysis
├── assets/
│   └── screenshots/        # Auto-saved fighting detection screenshots
├── logs/
│   └── alerts.csv          # Timestamped incident log
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A Gmail account (for email alerts)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Goda-Emad/SafeWatch-.git
cd SafeWatch-

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure email alerts
# Add your Gmail credentials to Streamlit secrets or .env file
# SENDER_EMAIL=your@gmail.com
# SENDER_PASSWORD=your_app_password
# RECEIVER_EMAIL=admin@example.com

# 4. Run the app
streamlit run app.py
```

### Or use the live deployed version directly:

🌐 [https://fa4rjpbkpefpcs9zdzbpcw.streamlit.app/](https://fa4rjpbkpefpcs9zdzbpcw.streamlit.app/)

---

## 📧 Alert System

When **fighting is detected above the confidence threshold (default: 75%)**:

1. 📸 A screenshot is automatically saved with a timestamp
2. 📋 The incident is logged to `logs/alerts.csv`
3. 📧 An HTML email is sent instantly to the configured security admin

---

## 👥 Team

| Name | Role |
|---|---|
| **Goda Emad** | Team Leader & App Developer — Built full Streamlit app, alert system, UI/UX, deployment |
| **Elia Fahmy** | Data Collection & Preparation — Kaggle dataset, class selection, quality verification |
| **Ibrahim Elshafey** | Data Preprocessing & Augmentation — Resize, normalize, augment, train/test split |
| **Ahmed Salama** | AI Model Development — MobileNetV2, Transfer Learning, Fine-Tuning, TFLite export |
| **Alwafa Ashour** | Model Testing & Analysis — Per-class evaluation, confusion matrix, documentation |

---

## 🔮 Roadmap

- [x] 8-class image classification
- [x] Fighting detection & email alert system
- [x] Bilingual UI (Arabic / English) with Dark/Light mode
- [x] Streamlit Cloud deployment
- [ ] Real-time video stream processing (continuous frame analysis)
- [ ] Expand to all 15 original dataset classes
- [ ] Multi-person detection in a single frame
- [ ] Mobile app (iOS / Android)
- [ ] Real CCTV integration
- [ ] Upgrade to EfficientNetV2 or Vision Transformer

---

## 🛠️ Tech Stack

- **Model:** TensorFlow / Keras — MobileNetV2 + TFLite quantization
- **Web App:** Streamlit
- **Backend:** Python (preprocess, predict, alert, email modules)
- **Deployment:** Streamlit Community Cloud
- **Dataset:** Kaggle — Human Action Recognition

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">

**SafeWatch · 2026**

*See More. Understand Faster. Act Now.*

[![Live App](https://img.shields.io/badge/🌐%20Live%20App-Open-FF4B4B?style=for-the-badge)](https://fa4rjpbkpefpcs9zdzbpcw.streamlit.app/)

</div>
