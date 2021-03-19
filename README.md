# SMART FAQ
## Bordeaux Ynov Campus - NLP Project
**Creation date :** 25/02/2020
**Update date :** 19/03/2021

**Authors :**  
- Laëtitia CONSTANTIN
- Mouna DAHMANI
- Marianne SEBILLE
- Axel CHENU

## Context 
Full text of all questions and answers from Stack Overflow that are tagged with the python tag. 
/n Useful for natural language processing and community analysis.

## Data Description 
This data is taken from [kaggle](https://www.kaggle.com/stackoverflow/pythonquestions)

This dataset is organized as **3 tables** between August 2, 2008 and October 19, 2018 :

- **Questions** contains the title, body, creation date, score, and owner ID for each Python question.
- **Answers** contains the body, creation date, score, and owner ID for each of the answers to these questions. 
/n The ParentId column links back to the Questions table.
- **Tags** contains the tags on each question besides the Python tag.

## PROJECT DEVELOPMENT

### Model builder
* [`00.Get_data/`](model_builder/00.Get_data)
* [`01.Data_Exploration/`](model_builder/01.Data_Exploration)
* [`02.Preprocessing/`](model_builder/02.Preprocessing)

### DL and ML Models
* [`DecisionTreeRegressor/`](model_builder/ML_models/DecisionTreeRegressor)
* [`RandomForestRegressor/`](model_builder/ML_models/RandomForestRegressor)
* [`XGBRegressor/`](model_builder/ML_models/XGBRegressor)
* [`CNN/`](model_builder/DL_models/CNN)

### Src : script python
* [`cleanTxt/`](src/cleanTxt)


## **Models performances**

|  Cols    |     Clean    |   Model | Metrics | Score |
| ---      | :-:          | :-:     | :-:     | :-:   |
|  Question, Question_body, Answer    |        Remove HTML, stop words, 10 000 lines, OneHotEncoder        |      DecisionTreeRegressor | mean_squared_error <br> mean_absolute_error |  4870.8 <br>  12.1 |
|  Question, Question_body, Answer    |        Remove HTML, stop words, 10 000 lines, OneHotEncoder        |      XGBRegressor          | mean_squared_error <br> mean_absolute_error |  4842.6 <br> 15.8 |
|   Question_body                     |        Remove HTML, stop words, 10 000 lines, OneHotEncoder        |      RandomForestRegressor | mean_squared_error <br> mean_absolute_error | 4814.2 <br> 15.19 |
|   Answer                            |        Remove HTML, stop words, 10 000 lines, Word2Vec             |      **CNN**                   | mean_squared_error <br> mean_absolute_error | 147.6 <br> 2.9 |


## Requirements
* [`requirements.txt`](requirements.txt) 

## Usefull links 
- [Trello](https://trello.com/b/gt8jrwmb/kaizen)
- [Git](https://github.com/yuhec/smartFAQ)
- [Kaggle](https://www.kaggle.com/stackoverflow/pythonquestions)

## Copyright Kaizen Members
- [Mouna DAHMANI](https://gitlab.com/MounaDahmani) 
- [Laëtitia CONSTANTIN](https://gitlab.com/yuhec) 
- [Marianne Sebille](https://gitlab.com/lipotre) 
- [Axel CHENU](https://gitlab.com/ACHENU26) 

**License**
Ynov Bordeaux.