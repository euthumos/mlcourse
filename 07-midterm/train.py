import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import lightgbm as lgb
from preprocessing import feature_eng

labeled_data = pd.read_csv('data/train.csv')

train, val = train_test_split(labeled_data, test_size=0.1, random_state=24, stratify=labeled_data.smoking) 

X_tr = train.iloc[:, :-1].drop('id', axis=1)
y_tr = train.iloc[:, -1]

X_val = val.iloc[:, :-1].drop('id', axis=1)
y_val = val.iloc[:, -1]

feature_eng(X_tr)
feature_eng(X_val)

model = lgb.LGBMClassifier(n_estimators=100,  
                           subsample=0.8, 
                           colsample_bytree=0.8, 
                           reg_lambda=10.0,
                           random_state=1)
model.fit(X_tr, y_tr)

y_val_pred = model.predict_proba(X_val)[:, 1]
roc_auc = roc_auc_score(y_val, y_val_pred)
print(f'ROC-AUC Score on validation set: {roc_auc:.6f}')


with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)