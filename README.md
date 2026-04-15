# 🛡️ Real-Time Credit Card Fraud Detection (MLOps)

An end-to-end MLOps system designed to detect fraudulent transactions in milliseconds. This project integrates high-performance modeling with a production-ready infrastructure using Docker, FastAPI, and MLflow.

---

### 📌 Business Case
According to Juniper Research, online payment fraud losses will exceed **$91B by 2028**. Beyond the stolen amount, every fraudulent transaction costs companies **4.60x the original value** in fees and logistics (LexisNexis). 

This project addresses the need for an automated, intelligent system capable of blocking threats instantly to minimize financial and operational impact.

### 🎯 Key Technical Achievements & MLOps Workflow
This system is built for scalability and reproducibility, following a modern MLOps architecture:

*   **Extreme Class Imbalance Handling:** Solved the 0.17% fraud rate challenge by implementing `scale_pos_weight` in XGBoost and stratified splitting.
*   **Experiment Tracking (MLflow):** Every hyperparameter (`max_depth`, `learning_rate`) and metric is logged to ensure model lineage and performance auditing.
*   **High-Performance Serving:** Built a dedicated **FastAPI** prediction endpoint for low-latency real-time inference.
*   **Containerization:** Fully dockerized environment to guarantee "it works on my machine" consistency from local development to Streamlit Cloud.

### 🛠️ Tech Stack


| Layer | Technology |
| :--- | :--- |
| **Modeling** | XGBoost, Scikit-learn |
| **Experiment Tracking** | MLflow |
| **API / Serving** | FastAPI, Uvicorn |
| **Containerization** | Docker |

### 📈 Model Performance
We prioritize **Recall** because missing a single fraud is significantly more expensive than a false alarm.


| Metric | Value |
| :--- | :--- |
| **Recall (Fraud)** | **0.84** |
| **Precision (Fraud)** | 0.76 |
| **F1-Score** | 0.80 |
| **AUC-ROC** | 0.97 |

### ⚙️ Installation & Deployment

1. **Clone & Setup**
   ```bash
   git clone https://github.com
   cd real-time-fraud-detection-mlops
   pip install -r requirements.txt
