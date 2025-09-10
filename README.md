# 🚗 Cars 24x7: Car Damage Detection  

A deep learning project to automatically detect and classify **car damages** into 6 categories using CNN-based models.  
This project also includes **hyperparameter tuning with Optuna** and a **Streamlit app** for real-time analysis.  

---

## 📸 Live Demo

Check out the live Streamlit app here: [Cars 24x7: Car Damage Detection](https://cars-24x7-car-damage-prediction-4brstu74jcammbugjw6wr6.streamlit.app/)

---

## 🖥️ Streamlit App Interface

![App Screenshot](https://github.com/prabalpkd/Cars-24X7-Car-Damage-Prediction/blob/main/App_Interface.png)


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
