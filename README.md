# Shroom ID

## Problem
When forgaging for wild mushrooms, it can be difficult to accurately predict whether or not a species of mushroom is safe for human consumption. To address this, we can use machine learning to develop a classification model that is capable of automatically distinguishing edible mushrooms from poisonous mushrooms.

## Goal
The purpose of developing this model is to help automate the identification of poisonous mushrooms and reduce the risk of misclassification and potential harm. Using attributes such as cap shape, gill size, odor, etc., a reliable model can be built.

## Dataset
From the UCI Machine Learning repository, the [mushroom](https://archive.ics.uci.edu/dataset/73/mushroom) dataset contains a sufficient number of features to train and validate this model effectively. Within it, we utilize the physical characteristics provided from the mushroom samples to analyze any relationships between fruiting body features and human toxicity/edibility.

## How to launch the web app
```
pip install streamlit
streamlit run app.py
```

## Project roadmap
| Goal                                   | Date
|                                       -|-
| Dataset selection and understanding    | 4/19/2024
| Background study and literature review | 4/26/2024
| Exploratory data analysis              | 5/03/2024
| Develop and evaluate prediction models | 5/17/2024
| Record observations and write report   | 5/24/2024
| Develop web app that runs the model    | 5/31/2024
