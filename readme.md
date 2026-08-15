# 🧬 Protein Enzyme Classification

A machine learning project that predicts whether a protein is an **enzyme** or **non-enzyme** based on features extracted from its amino-acid sequence.

The project includes data collection, exploratory data analysis, protein sequence feature engineering, machine learning model development, model evaluation, and an interactive Streamlit application.

---
## 🌐 Live Demo

Try the deployed application here:

[🧬 Protein Enzyme Classifier](https://feufoller-proteinenzymeclassification-app-31xtl4.streamlit.app/)

## 🚀 Project Overview

Proteins can be classified according to their biological functions. Enzymes are proteins that catalyze biochemical reactions, while non-enzymatic proteins perform a wide range of other biological functions.

This project builds a machine learning classifier that predicts whether a protein sequence is more likely to belong to the **enzyme** or **non-enzyme** class.

The workflow is:

```text
Protein Sequence
       ↓
Feature Engineering
       ↓
Machine Learning Model
       ↓
Enzyme / Non-enzyme Prediction
````

---

## 📊 Dataset

The dataset contains protein sequences obtained from UniProt.

After cleaning and balancing:

* Total proteins: **2,850**
* Enzymes: **1,425**
* Non-enzymes: **1,425**

Sequences were cleaned by removing:

* Duplicate sequences
* Extremely short sequences
* Invalid or missing sequence data

---

## 🔬 Feature Engineering

Protein sequences were converted into numerical features suitable for machine learning.

The features include:

### Sequence-level features

* Sequence length
* Hydrophobic amino-acid fraction
* Aromatic amino-acid fraction
* Positively charged amino-acid fraction
* Negatively charged amino-acid fraction

### Amino-acid composition

The relative proportion of each of the 20 standard amino acids:

```text
A C D E F G H I K L
M N P Q R S T V W Y
```

This produced a feature matrix used to train the classification models.

---

## 🤖 Machine Learning Models

Three models were evaluated:

| Model               |  Accuracy | Precision |    Recall |  F1 Score |   ROC-AUC |
| ------------------- | --------: | --------: | --------: | --------: | --------: |
| Logistic Regression |     0.644 |     0.633 |     0.684 |     0.658 |     0.694 |
| 🏆 Random Forest    | **0.760** | **0.768** |     0.744 | **0.756** | **0.833** |
| Tuned Random Forest |     0.753 |     0.748 | **0.761** |     0.755 |     0.820 |

The **Random Forest classifier** achieved the best overall performance.

### Final Model Performance

* **Accuracy:** 75.96%
* **Precision:** 76.81%
* **Recall:** 74.39%
* **F1 Score:** 75.58%
* **ROC-AUC:** 83.27%

---

## 📈 Key Findings

Feature importance analysis showed that several sequence-derived properties contributed strongly to classification, including:

1. Hydrophobic amino-acid fraction
2. Serine proportion
3. Positively charged amino-acid fraction
4. Histidine proportion
5. Valine proportion
6. Sequence length
7. Aspartic acid proportion

These results suggest that overall protein composition contains useful information for distinguishing enzymes from non-enzymes.

---

## 🖥️ Streamlit Application

The project includes an interactive web application built with Streamlit.

Users can:

1. Enter a protein amino-acid sequence.
2. Validate the sequence.
3. Generate a prediction.
4. View the probability of the sequence belonging to the enzyme class.
5. Inspect basic sequence characteristics.

Run the application locally with:

```bash
python -m streamlit run app.py
```

---

## 📁 Project Structure

```text
protein-enzyme-classification/
│
├── app.py
├── requirements.txt
├── .gitignore
├── readme.md
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── model_comparison.csv
│       └── feature_importance.csv
│
├── figures/
│   ├── roc_curve.png
│   └── feature_importance.png
│
├── models/
│   ├── protein_enzyme_random_forest.joblib
│   └── feature_names.joblib
│
└── notebook/
    └── protein_enzyme_classification.ipynb
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd protein-enzyme-classification
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

---

## ⚠️ Disclaimer

This project is intended as a **machine learning and data science demonstration**.

Predictions should not be considered a substitute for professional protein annotation, biological databases, laboratory experiments, or experimental validation.

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Joblib
* Jupyter Notebook

---


