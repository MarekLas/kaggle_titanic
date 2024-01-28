![GitHub last commit](https://img.shields.io/github/last-commit/MarekLas/kaggle_titanic)

<img align="center" width ="100%" src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/titanic4.gif" />

# Titanic - Machine Learning from Disaster

## Context
The sinking of the Titanic is one of the most infamous shipwrecks in history.

On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew.

While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others.


## Data Dictionary

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/data_dictionary.JPG" align="center" width ="71%"/> 

* embarked	Port of Embarkation	C = Cherbourg, Q = Queenstown, S = Southampton
  Variable Notes
  pclass: A proxy for socio-economic status (SES)
  1st = Upper
  2nd = Middle
  3rd = Lower

* age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5

* sibsp: The dataset defines family relations in this way...
  Sibling = brother, sister, stepbrother, stepsister
  Spouse = husband, wife (mistresses and fiancés were ignored)

* parch: The dataset defines family relations in this way...
  Parent = mother, father
  Child = daughter, son, stepdaughter, stepson
  Some children travelled only with a nanny, therefore parch=0 for them.
  
Link to Kaggle: https://www.kaggle.com/competitions/titanic/overview

## <b>Link to the script</b>

### <b>https://github.com/MarekLas/kaggle_titanic/blob/main/scripts/Titanic_Kaggle_2023.ipynb</b>

## Modules used in the script

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/01_t_modules.png" align="center" width ="80"/> 

## Import and copy data

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/02_t_import_and_copy_data.png" align="center" width ="80%"/> 

## Data sample

* training data set

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/03_t_sample_train_data.JPG" align="center" width ="80%"/> 

* test data set

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/04_t_sample_test_data.JPG" align="center" width ="65%"/> 

* gender submision

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/05_t_sample_gender_submision.JPG" align="center" width ="15%"/> 

## Data information

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/06_t_info.JPG" align="center" width ="30%"/> 

## Data describe

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/07_t_describe.JPG" align="center" width ="40%"/> 

## Missing values

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/08_t_missing_values.jpg" align="center" width ="100%"/> 

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/09_t_is_null.jpg" align="center" width ="15%"/> 

## Data types

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/10_t_datatypes.JPG" align="center" width ="15%"/> 

## Survived dependences

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/11_t_dependences_pairplot.jpg" align="center" width ="70%"/> 

## Gender dependences

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/12_t_dependeces_pairplot_sex.jpg" align="center" width ="70%"/> 

## Correlation matrix

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/13_t_heatmap.jpg" align="center" width ="50%"/> 

## Survived count

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/14_t_survived_count.jpg" align="center" width ="70%"/> 

## Feature: Pclass
Description: The ticket class of the passanger.

Key: 1 = 1st, 2 = 2nd, 3 = 3rd

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/15_t_pclass_survived_count.jpg" align="center" width ="70%"/> 

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/17_t_dependency_sex_pclass_survived.jpg" align="center" width ="40%"/> 

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/18_t_pclass_chance_to_survive.JPG" align="center" width ="50%"/> 

## Feature: Name
Description: The name of the passenger

## Feature: Sex
Description: The sex of the passenger (male or female)

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/19_t_sex_survived_count.JPG" align="center" width ="70%"/> 

## Feature: Age

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/20_t_age_distribution.jpg" align="center" width ="40%"/> 

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/21_t_sex_age_survived.jpg" align="center" width ="40%"/> 

### Missing Age values

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/22_t_missing_age_values.jpg" align="center" width ="30%"/>

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/23_t_pclass_survived_sex.jpg" align="center" width ="30%"/>

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/24_t_mean_age_by_pclass.JPG" align="center" width ="20%"/>

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/25_t_function_fill_age_column.png" align="center" width ="80%"/>

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/26_t_cat_age.png" align="center" width ="80%"/>

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/25_t_count_age_groups.JPG" align="center" width ="15%"/>

## Feature SibSp
Description: The number of siblings the passenger has aboard the Titanic

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/27_t_survival_siblings.jpg" align="center" width ="40%"/>

## Feature: Parch
Description: The number of parent/childeren the passenger has aboard the Titinic.

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/28_t_survival_parch.jpg" align="center" width ="40%"/>

## Feature: Ticket
Description: The ticket number of the boarding passanger.

## Feature: Fare
Description: How much the ticket cost.

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/29_t_fare_distribution.jpg" align="center" width ="50%"/>

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/29b_t_fare_groups.jpg" align="center" width ="20%"/>

## Feature: Cabin
Description: The cabin number where the passanger was staying.

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/29c_t_drop_cabin.png" align="center" width ="60%"/>

## Feature: Embarked
Description: The port where the passenger baoarded the Titinic.
Key: C = Cherbourg, Q = Queenstown, S = Southampton

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/30_t_embarked_missing.jpg" align="center" width ="70%"/>

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/31_t_fill_embarked.png" align="center" width ="50%"/>

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/32_t_embarked_survival.jpg" align="center" width ="70%"/>

## It's time for the one hot encoding

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/33_t_one_hot_table.jpg" align="center" width ="100%"/>

## Let's label continous values

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/34_t_label_continous_values.jpg" align="center" width ="30%"/>
Link to LabelEncoder() documentation: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html

## Select and scale the data

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/35_t_select_data_scale.png" align="center" width ="70%"/>

## Function for the models

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/36_t_function_for_models.png" align="center" width ="70%"/>

## GridSearch() example

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/37_t_gridsearch.png" align="center" width ="70%"/>

## Very interesting CatBoostClassifier

Link to the documentation: https://catboost.ai/en/docs/concepts/python-reference_catboostclassifier

## Accuracy metric ranking and chart

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/39_t_accuracy_table.JPG" align="center" width ="20%"/>

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/40_t_accuracy_barplot.jpg" align="center" width ="50%"/>

## Accuracy metric ranking and chart after crossvalidation

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/41_t_accuracy_crossvalidation_table.JPG" align="center" width ="20%"/>

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/42_accuracy_crossvalidation_barplot.jpg" align="center" width ="50%"/>

## Feature importance 

* CatBoostClassifier
 
 <img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/43_t_catboost_feature_importance.jpg" align="center" width ="50%"/>
 
* GradientBoostClassifier

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/44_t_gradientboost_feature_importance.jpg" align="center" width ="50%"/>

* DecisionTreeClassifier

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/45_t_decisiontree_feature_importance.jpg" align="center" width ="50%"/>

## Submission for the Kaggle competition

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/46_t_submission_for_the_best_model.png" align="center" width ="60%"/>

![GitHub last commit](https://img.shields.io/github/last-commit/MarekLas/kaggle_titanic)
