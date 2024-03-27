# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model is a Random Forest Model which predicts if an individual's income is more than $50K/yr based on census data. It was developed as part of a machine learning pipeline that processes data, trains the model, and evaluates its performance on a test dataset as well as various slices of the data based on categorical features.

## Intended Use
The model is intended for finding insights into income distribution across different demographic groups. It can be useful in policy making and for social science. 

## Training Data
The training data comes from the U.S. Census Bureau and includes several features such as age, work class, education, marital status, occupation, relationship, race, sex, hours-per-week, and native-country.

## Evaluation Data
The evaluation of the model was conducted using a split of the original dataset. 80% of the data was used for training while 20% was used for testing.

## Metrics
The model's performance was evaluated using precision, recall, and F1 score metrics. The performance metrics on the dataset are as follows:

Precision: 0.7380 | Recall: 0.6365 | F1: 0.6835

## Ethical Considerations
This model makes predictions based on demographic information. There is a risk of introducing human bias into the model. Users should consider the implications of using potentially biased models.

## Caveats and Recommendations
The model's accuracy may vary across demographic groups, as shown by performance metrics on data slices.
It is recommended to regularly update the model with new data to ensure its accuracy.
