# 🚗 Cars 24x7: Car Damage Detection  

A deep learning project to automatically detect and classify **car damages** into 6 categories using CNN-based models.  
This project also includes **hyperparameter tuning with Optuna** and a **Streamlit app** for real-time analysis.  

---

## 📸 Demo


---

## 📌 Project Overview  

The goal of this project is to classify car images into one of the following 6 classes:  
- **Front Breakage**  
- **Front Crushed**  
- **Front Normal**  
- **Rear Breakage**  
- **Rear Crushed**  
- **Rear Normal**  

---

## 🧠 Models Used  

- **Custom CNN** – Baseline model  
- **EfficientNetB0** – Lightweight & efficient model  
- **ResNet50** – Final chosen model (best performing)  
  - Fine-tuned with **Optuna** hyperparameter optimization  
  - Used transfer learning with selective layer unfreezing  

---

## ⚙️ Tech Stack  

- **Python** 🐍  
- **PyTorch** – Model training  
- **Optuna** – Hyperparameter tuning  
- **Streamlit** – Interactive web app  
- **PIL, Torchvision** – Image preprocessing  

---

## 📂 Project Structure  

```bash
├── damage_prediction.ipynb      # Main notebook (training + evaluation)
├── hyperparameter_Tuning.ipynb  # Optuna tuning for ResNet50
├── app.py                       # Streamlit app for real-time predictions
├── model_helper.py              # Helper functions for loading model & inference
├── model/saved_model.pth        # Trained ResNet50 weights
```
---

## 🚀 How to Run
1️⃣ Clone the repository

git clone https://github.com/yourusername/cars24x7-damage-detection.git
cd cars24x7-damage-detection

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run Streamlit app
streamlit run app.py

---

## 📊 Results

•  Compared CNN, EfficientNetB0, and ResNet50

•  ResNet50 (Optuna tuned) achieved the best accuracy and generalization

•  Real-time predictions work seamlessly via the Streamlit app

---

📌 Future Improvements

•  Extend dataset for more diverse damages

•  Deploy app on cloud (AWS / GCP)

•  Add explainability (Grad-CAM heatmaps)

---

## 🙌 Acknowledgments

•  Pre-trained models from Torchvision

•  Hyperparameter optimization with Optuna

•  Streamlit for simple & fast deployment

---

Thank You❤️❤️❤️
