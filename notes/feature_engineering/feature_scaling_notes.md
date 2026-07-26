# Feature Scaling Notes

## What this notebook demonstrates
This notebook shows how feature scaling can improve model training when features are on different scales.

## Key steps
1. Load the dataset
2. Remove non-feature columns if needed
3. Split data into train and test sets
4. Apply StandardScaler to the training and test features
5. Compare the distribution and model performance before and after scaling

## Important concepts

### Train-test split
The notebook uses:
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    df.drop('Purchased', axis=1),
    df['Purchased'],
    test_size=0.3,
    random_state=0
)
```

This ensures the model is evaluated on unseen data.

### Standard scaling
StandardScaler transforms features so they have:
- mean close to 0
- standard deviation close to 1

Example:
```python
from sklearn.preprocessing import StandardScaler

scalar = StandardScaler()
scalar.fit(X_train)

X_train_scaled = scalar.transform(X_train)
X_test_scaled = scalar.transform(X_test)
```

### Why scaling matters
Features like Age and EstimatedSalary often have very different ranges. Scaling helps algorithms such as logistic regression to converge more efficiently and can improve results.

## Visual comparison
The notebook plots:
- original feature distribution before scaling
- scaled feature distribution after scaling

This helps show how scaling standardizes the data.

## Model comparison
The notebook trains two logistic regression models:
- one on the unscaled data
- one on the scaled data

Then it compares accuracy:
```python
from sklearn.metrics import accuracy_score

print("Actual", accuracy_score(y_test, y_pred))
print("Scaled", accuracy_score(y_test, y_pred_scaled))
```

## Takeaways
- Scaling is useful for algorithms sensitive to feature magnitude.
- It is especially important for distance-based and linear models.
- Always fit the scaler on the training set only, then transform the test set.
- Use the same scaling parameters for train and test data.

## Summary
Feature scaling is a core part of feature engineering because it makes input features more comparable and improves model training stability.
