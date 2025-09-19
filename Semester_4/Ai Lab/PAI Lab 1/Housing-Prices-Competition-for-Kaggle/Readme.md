# Housing Prices Competition for Kaggle Learn Users

![Ames Housing Banner](https://storage.googleapis.com/kaggle-media/competitions/kaggle/5407/media/housesbanner.png)

---

## Overview

This repository contains a solution for the [Kaggle Housing Prices Competition](https://www.kaggle.com/competitions/home-data-for-ml-course), which challenges participants to predict the final price of homes in Ames, Iowa using advanced regression techniques and creative feature engineering.

---

## Technologies Used

- **Python 3.12**
- **Jupyter Notebook**
- **Pandas** (data manipulation)
- **NumPy** (numerical operations)
- **Scikit-learn** (preprocessing, model selection, metrics)
- **XGBoost** (gradient boosting regression)
- **Matplotlib/Seaborn** (for EDA, optional)

---

## Step-by-Step Explanation

### 1. Data Loading

We load the training and test datasets using Pandas.  
**Why:** To access and manipulate the data for analysis and modeling.

```python
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
```

---

### 2. Saving Test IDs

We save the `Id` column from the test set for use in the final submission.  
**Why:** Kaggle requires predictions to be matched to these IDs.

```python
test_ids = test["Id"]
```

---

### 3. Combining Data for Feature Engineering

We concatenate train and test data (excluding the target variable) to ensure consistent feature engineering and encoding.  
**Why:** Prevents mismatches in categorical encoding and feature creation.

```python
all_data = pd.concat([train.drop("SalePrice", axis=1), test], sort=False)
all_data.drop("Id", axis=1, inplace=True)
```

---

### 4. Missing Value Imputation

- **Categorical columns:** Fill missing values with `"None"`.
- **Numerical columns:** Fill missing values with the median value.

**Why:** Ensures the model receives complete data and handles missingness appropriately.

```python
for col in all_data.columns:
    if all_data[col].dtype == "object":
        all_data[col] = all_data[col].fillna("None")
    else:
        all_data[col] = all_data[col].fillna(all_data[col].median())
```

---

### 5. Label Encoding Categorical Features

We convert categorical variables to numeric using `LabelEncoder`.  
**Why:** XGBoost and most ML algorithms require numeric input.

```python
for col in all_data.select_dtypes(include="object"):
    le = LabelEncoder()
    all_data[col] = le.fit_transform(all_data[col].astype(str))
```

---

### 6. Feature Engineering

We create new features to help the model capture more information:

- **TotalSF:** Total square footage (`TotalBsmtSF` + `1stFlrSF` + `2ndFlrSF`)
- **TotalBath:** Total bathrooms (full + half baths, including basement)
- **HouseAge:** Age of the house at the time of sale
- **RemodAge:** Years since last remodel

**Why:** New features can improve model performance by providing additional signals.

```python
all_data["TotalSF"] = all_data["TotalBsmtSF"] + all_data["1stFlrSF"] + all_data["2ndFlrSF"]
all_data["TotalBath"] = (
    all_data["FullBath"] + all_data["BsmtFullBath"] +
    0.5 * (all_data["HalfBath"] + all_data["BsmtHalfBath"])
)
all_data["HouseAge"] = all_data["YrSold"] - all_data["YearBuilt"]
all_data["RemodAge"] = all_data["YrSold"] - all_data["YearRemodAdd"]
```

---

### 7. Log-Transforming Skewed Features

We apply a log transformation to features with high skewness.  
**Why:** Reduces the impact of outliers and helps the model generalize better.

```python
skewed_feats = all_data.apply(lambda x: x.skew()).sort_values(ascending=False)
skewed = skewed_feats[abs(skewed_feats) > 0.75].index
all_data[skewed] = np.log1p(all_data[skewed])
```

---

### 8. Splitting Data Back

We separate the combined data back into training and test sets.  
**Why:** To train the model and make predictions on the test set.

```python
X = all_data.iloc[:train.shape[0], :]
X_test = all_data.iloc[train.shape[0]:, :]
y = np.log1p(train["SalePrice"])
```

---

### 9. Feature Standardization

We scale features to have zero mean and unit variance using `StandardScaler`.  
**Why:** Helps gradient boosting models converge faster and perform better.

```python
scaler = StandardScaler()
X = scaler.fit_transform(X)
X_test = scaler.transform(X_test)
```

---

### 10. Model Training and Cross-Validation

We use XGBoost with tuned hyperparameters and 5-fold cross-validation to estimate model performance.  
**Why:** Cross-validation provides a robust estimate of generalization error.

```python
model = XGBRegressor(
    n_estimators=5000,
    learning_rate=0.01,
    max_depth=3,
    subsample=0.7,
    colsample_bytree=0.7,
    random_state=42
)
kf = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = -cross_val_score(model, X, y, scoring="neg_root_mean_squared_error", cv=kf)
print("CV RMSE:", np.mean(cv_scores))
```

---

### 11. Final Model Training and Prediction

We train the model on the full training data and predict on the test set.  
**Why:** To generate predictions for submission.

```python
model.fit(X, y)
preds = np.expm1(model.predict(X_test))
```

---

### 12. Submission File Creation

We create a CSV file in the required format for Kaggle submission.  
**Why:** To submit predictions and get a score on the leaderboard.

```python
submission = pd.DataFrame({"Id": test_ids, "SalePrice": preds})
submission.to_csv("submission1.csv", index=False)
print("submission.csv ready!")
```

---

## How to Improve Further

- **Hyperparameter Tuning:** Use GridSearchCV or Optuna for better model parameters.
- **Ensembling:** Combine predictions from multiple models (e.g., XGBoost, LightGBM, Ridge, Lasso).
- **Stacking:** Use meta-models to blend outputs from several base models.
- **Advanced Feature Engineering:** Create polynomial features, interaction terms, or use domain knowledge for new features.
- **Outlier Handling:** Remove or cap outliers in the target and features.
- **Feature Selection:** Use feature importance or recursive feature elimination to keep only the most relevant features.
- **External Data:** If allowed, use additional datasets for more features.

---

## References

- [Kaggle Competition Page](https://www.kaggle.com/competitions/home-data-for-ml-course)
- [Ames Housing Dataset](https://www.kaggle.com/datasets/prevek18/ames-housing-dataset)
- [XGBoost Documentation](https://xgboost.readthedocs.io/en/latest/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)

---
