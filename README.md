<img align="center" width ="100%" src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/titanic4.gif" />

# Titanic - Machine Learning from Disaster

## Context
The sinking of the Titanic is one of the most infamous shipwrecks in history.

On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew.

While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others.


## Data Dictionary

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/data_dictionary.JPG" align="center" width ="70%"/> 

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

## Link to the script

https://github.com/MarekLas/kaggle_titanic/blob/main/ipynb/Titanic_Kaggle_2023.ipynb

## Modules used in the script

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/01_t_modules.png" align="center" width ="70%"/> 

## Import and copy data

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/02_t_import_and_copy_data.png" align="center" width ="70%"/> 

## Data sample

* training data set

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/03_t_sample_train_data.JPG" align="center" width ="70%"/> 

* test data set

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/04_t_sample_test_data.JPG" align="center" width ="60%"/> 

* gender submision

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/05_t_sample_gender_submision.JPG" align="center" width ="16%"/> 

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

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/17_t_dependency_sex_pclass_survived.jpg" align="center" width ="30%"/> 

<img src="https://github.com/MarekLas/kaggle_titanic/blob/main/readme_files/18_t_pclass_chance_to_survive.JPG" align="center" width ="50%"/> 

## Feature: Name
Description: The name of the passenger

## Feature: Sex
Description: The sex of the passenger (male or female)
