# 🚦 Traffic Sign Classification

This project implements a convolutional neural network (CNN) to classify traffic signs using the German Traffic Sign Recognition Benchmark (GTSRB). The model is built and trained using TensorFlow/Keras.

---

## 🧠 Model Architectures & Results

| Model | Architecture | Dropout | Test Accuracy | Test Loss | Inference Time |
|-------|--------------|---------|---------------|-----------|----------------|
| **1** | `Conv(32) → Pool → Dense(128)` | ✅ | **97.02%** | 0.1261 | ~2s |
| **2** | `Conv(32) → Pool → Conv(64) → Pool → Dense(128)` | ✅ | **98.84%** | 0.0555 | ~2s |
| **3** | `Conv(32) → Pool → Conv(64) → Pool → Dense(128) → Dropout(0.5) → Dense(128) → Dropout(0.5)` | ✅ | **97.30%** | 0.1289 | ~2s |
| **4** | `Conv(32) → Pool → Conv(64) → Pool → Conv(128) → Pool → Dense(128) → Dropout(0.5)` | ✅ | **98.86%** | 0.0466 | ~3s |
| **5** | `Conv(32) → Pool → Conv(64) → Pool → Conv(128) → Pool → Dense(512) → Dropout(0.5)` | ✅ | **98.97%** | 0.0386 | ~3s |
| **6** | `Conv(32) → Pool → Conv(64) → Pool → Conv(128) → Pool → Dense(512) → Dropout(0.5) → Dense(256) → Dropout(0.5)` | ✅ | **98.12%** | 0.0765 | ~3s |

---

## 🧪 Experiment Setup

- **Input shape**: 30 × 30 RGB images
- **Data source**: GTSRB, structured by category ID folders
- **Train/Test split**: 60% train, 40% test
- **Optimizer**: Adam (default parameters)
- **Loss function**: Categorical Crossentropy
- **Activations**: ReLU in hidden layers, Softmax in output
- **Normalization**: `images / 255.0`
- **Epochs**: 10
- **Batch size**: Default

---

## 📈 Observations

- Increasing depth (adding Conv and Pool layers) improved accuracy significantly.
- Model 2 already gave a strong result with only two Conv layers.
- Dropout helped prevent overfitting but too many dropout layers (Model 3) slightly decreased performance.
- Best performance came from Model 4, using 3 Conv + Pool layers and one Dense layer with dropout.

---
## 🗂️ Project Structure
traffic/
├── traffic.py # Main training and evaluation script
├── gtsrb/ # Dataset directory (0 to NUM_CATEGORIES-1)
├── requirements.txt # Python dependencies
└── README.md # Project documentation
