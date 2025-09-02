👤 Author

William Akitikori

Adaptable Technical Support Specialist & Aspiring Engineer
Passionate about data engineering and user‑focused innovation.



# 🛠️ Lightweight ETL Pipeline for Multi‑Source Sales Data

## 📌 Overview
This project implements a **lightweight ETL (Extract, Transform, Load) pipeline** that consolidates sales and transaction data from **Shopify**, **Square**, **Dojo**, and **Tide** into a single, clean dataset.  
The unified dataset is designed for **future analytics, reporting, or dashboard integration**, providing a reliable foundation for business decision‑making.

---

## 💡 Why This Project Matters
From a data engineering perspective, this project demonstrates:
- Real‑world **data wrangling** from multiple, inconsistent sources
- **Pipeline design** and **data standardisation** techniques
- Foundations of **automation** and **reproducibility**
- Creation of a **business‑relevant asset** for *Awe Kids*

---

## 📊 Data Sources
The pipeline processes CSV exports from:
1. **Shopify** – Orders/Sales report (October 2024)
2. **Square** – Point‑of‑sale transactions (markets & trade supply meetings)
3. **Dojo** – Card terminal transactions
4. **Tide** – Bank statement or transaction export of income

> Each dataset varies in structure and schema. The pipeline standardises and unifies them into a consistent format.

---

## ⚙️ Tools & Technologies
- **Python**: `pandas`, `datetime`
- **Jupyter Notebook** / **Google Colab**
- **Git & GitHub** for version control

---

## 🔄 ETL Process

### 1. **Extract**
- Load CSV exports from each platform into pandas DataFrames
- Handle different file encodings and delimiters

### 2. **Transform**
- Standardise column names and data types
- Parse and normalise date formats
- Map transaction types and payment methods to a common schema
- Remove duplicates and handle missing values
- Merge datasets into a single DataFrame

### 3. **Load**
- Export the cleaned dataset to:
  - **CSV** for portability

---

## 🚀 Getting Started

### Clone the Repository
```bash
git clone https://github.com/yourusername/etl-sales-pipeline.git
cd etl-sales-pipeline

### Install Dependencies
pip install -r requirements.txt

### Run the Pipeline
python src/main.py

---

🔮 Future Enhancements
- Automate data ingestion from APIs instead of manual CSV exports
- Integrate with Apache Airflow for scheduling
- Deploy to cloud storage (AWS S3 / Azure Blob)
- Add unit tests for data validation
