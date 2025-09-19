# 🚀 Spaceship Titanic Survival Prediction

## 📌 Objective

Predict whether a passenger aboard the Spaceship Titanic was transported to an alternate dimension during the accident.

This is a **binary classification task** (Transported: True/False).

---

## 📂 Dataset

The dataset comes from Kaggle's [Spaceship Titanic competition](https://www.kaggle.com/competitions/spaceship-titanic/).

- **train.csv** → Passenger information + survival label (Transported).
- **test.csv** → Passenger information only (used for prediction).
- **sample_submission.csv** → Kaggle-required submission format.

**Target Column** → `Transported` (boolean: True/False).

---

## ⚙️ Steps Performed

### 1. Exploratory Data Analysis (EDA)

- Checked dataset shape, missing values, and value distributions.
- Explored categorical vs numerical variables.
- Visualized feature relationships with survival.

### 2. Feature Engineering

- Extracted **Group** from `PassengerId` (family/group indicator).
- Split **Cabin** into `Deck`, `CabinNum`, and `Side`.
- Created **TotalSpend** (sum of spending on RoomService, FoodCourt, ShoppingMall, Spa, VRDeck).

### 3. Data Preprocessing

- Filled missing values:
  - **Numerical** → median imputation.
  - **Categorical** → mode imputation.
- Encoded categorical variables using **Label Encoding**.
- Dropped non-predictive columns: `PassengerId`, `Name`.

### 4. Model Training

- Train/Validation split: 80/20 with stratification.
- Used **XGBoost Classifier** with:
  - `n_estimators=500`
  - `learning_rate=0.05`
  - `max_depth=6`
  - `subsample=0.8`
  - `colsample_bytree=0.8`

### 5. Evaluation

- Metrics:
  - **Accuracy**
  - **F1 Score**
  - **Classification Report**

### 6. Kaggle Submission

- Predicted survival on the test dataset.
- Saved submission in required format:
  ```csv
  PassengerId,Transported
  0001_01,True
  0001_02,False
  ...
  ```

---

## 📊 Results

- **Validation Accuracy:** ~82%
- **Validation F1 Score:** ~0.80
- **Leaderboard Score (Kaggle):** depends on test data (public ~0.78–0.80).

---

## 🛠️ Libraries Used

- `pandas` & `numpy` → data handling
- `matplotlib` & `seaborn` → EDA visualization
- `scikit-learn` → preprocessing, evaluation
- `xgboost` → classification model

---

## 📌 Why These Choices?

- **EDA** → Understand data distribution & correlations.
- **Feature Engineering** → Improve predictive power by deriving useful signals.
- **XGBoost** → Strong performer in tabular classification tasks.
- **F1 Score** → Balances precision & recall, better than accuracy alone.

---

👉 This project demonstrates how **EDA + feature engineering + XGBoost** can significantly improve classification performance on tabular datasets.
