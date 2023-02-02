# Easy function for quick checkin missing values
def missing_values (target_column):
    print(train[target_column].isnull().sum())
    
'''
Function to fill the column Age with mean age
values depending on the data groups: Pclass and Sex.
train['Age_Full'] = train.apply(lambda row: categorise(row), axis=1)
'''

def categorise(row):
  if np.isnan(row['Age']):
    if row['Pclass'] == 1 and row['Sex'] == 'female':
      return mean_age_by_pclass_sex[1].female
    if row['Pclass'] == 1 and row['Sex'] == 'male':
      return mean_age_by_pclass_sex[1].male
    if row['Pclass'] == 2 and row['Sex'] == 'female':
      return mean_age_by_pclass_sex[2].female
    if row['Pclass'] == 2 and row['Sex'] == 'male':
      return mean_age_by_pclass_sex[2].male
    if row['Pclass'] == 3 and row['Sex'] == 'female':
      return mean_age_by_pclass_sex[3].female
    if row['Pclass'] == 3 and row['Sex'] == 'male':
      return mean_age_by_pclass_sex[3].male
  else:
    return row['Age']

# Function to fit the model and return the accuracy scores

def fit_ml_algo(algo, X_train, y_train, cv):
    
    # One Pass
    model = algo.fit(X_train, y_train)
    acc = round(model.score(X_train, y_train) * 100, 2)

    # Cross Validaton
    train_pred= model_selection.cross_val_predict(algo,
                                                  X_train,
                                                  y_train,
                                                  cv=cv,
                                                  n_jobs=-1)
    acc_cv = round(metrics.accuracy_score(y_train, train_pred) *100, 2)
    
    return train_pred, acc, acc_cv

'''
Function to show which features are most important in the model.
::param_model:: Which model to use?
::param_data:: What data to use?
'''
def feature_importance(model, data):
    fea_imp=pd.DataFrame({'imp': model.feature_importances_, 'col': data.columns})
    fea_imp =fea_imp.sort_values(['imp', 'col'], ascending=[True, False]).iloc[-30:]
    _= fea_imp.plot(kind='barh', x='col', y='imp', figsize=(10,5), colormap = "Set2").set(title='Feature importance')
    
    return fea_imp
