# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model is a Random Forest Model which predicts if an individual's income is more than $50K/yr based on census data. It was developed as part of a machine learning pipeline that processes data, trains the model, and evaluates its performance on a test dataset as well as various slices of the data based on categorical features.

## Intended Use
The model is intended for finding insights into income distribution across different demographic groups. It can be useful in policy making and for social science. 

## Training Data
The training data comes from the U.S. Census Bureau and includes several features such as age, work class, education, marital status, occupation, relationship, race, sex, hours-per-week, and native-country.

## Evaluation Data
The evaluation of the model was conducted using a split of the original dataset.

## Metrics
The model's performance was evaluated using precision, recall, and F1 score metrics. The performance metrics on the test dataset are as follows:
    workclass: ?, Count: 389
    Precision: 0.6667 | Recall: 0.4286 | F1: 0.5217
    workclass: Federal-gov, Count: 191
    Precision: 0.7714 | Recall: 0.7714 | F1: 0.7714
    workclass: Local-gov, Count: 387
    Precision: 0.7549 | Recall: 0.7000 | F1: 0.7264
    workclass: Private, Count: 4,578
    Precision: 0.7416 | Recall: 0.6394 | F1: 0.6867
    workclass: Self-emp-inc, Count: 212
    Precision: 0.7699 | Recall: 0.7373 | F1: 0.7532
    workclass: Self-emp-not-inc, Count: 498
    Precision: 0.7103 | Recall: 0.4841 | F1: 0.5758
    workclass: State-gov, Count: 254
    Precision: 0.7313 | Recall: 0.6712 | F1: 0.7000
    workclass: Without-pay, Count: 4
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    education: 10th, Count: 183
    Precision: 0.3333 | Recall: 0.1667 | F1: 0.2222
    education: 11th, Count: 225
    Precision: 1.0000 | Recall: 0.2727 | F1: 0.4286
    education: 12th, Count: 98
    Precision: 1.0000 | Recall: 0.4000 | F1: 0.5714
    education: 1st-4th, Count: 23
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    education: 5th-6th, Count: 62
    Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
    education: 7th-8th, Count: 141
    Precision: 1.0000 | Recall: 0.1667 | F1: 0.2857
    education: 9th, Count: 115
    Precision: 1.0000 | Recall: 0.3333 | F1: 0.5000
    education: Assoc-acdm, Count: 198
    Precision: 0.7105 | Recall: 0.5745 | F1: 0.6353
    education: Assoc-voc, Count: 273
    Precision: 0.6667 | Recall: 0.5714 | F1: 0.6154
    education: Bachelors, Count: 1,053
    Precision: 0.7373 | Recall: 0.7111 | F1: 0.7240
    education: Doctorate, Count: 77
    Precision: 0.8525 | Recall: 0.9123 | F1: 0.8814
    education: HS-grad, Count: 2,085
    Precision: 0.6518 | Recall: 0.4232 | F1: 0.5132
    education: Masters, Count: 369
    Precision: 0.8326 | Recall: 0.8647 | F1: 0.8483
    education: Preschool, Count: 10
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    education: Prof-school, Count: 116
    Precision: 0.8462 | Recall: 0.9167 | F1: 0.8800
    education: Some-college, Count: 1,485
    Precision: 0.7051 | Recall: 0.5523 | F1: 0.6194
    marital-status: Divorced, Count: 920
    Precision: 0.8085 | Recall: 0.3689 | F1: 0.5067
    marital-status: Married-AF-spouse, Count: 4
    Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
    marital-status: Married-civ-spouse, Count: 2,950
    Precision: 0.7331 | Recall: 0.6907 | F1: 0.7113
    marital-status: Married-spouse-absent, Count: 96
    Precision: 1.0000 | Recall: 0.2500 | F1: 0.4000
    marital-status: Never-married, Count: 2,126
    Precision: 0.8367 | Recall: 0.3981 | F1: 0.5395
    marital-status: Separated, Count: 209
    Precision: 1.0000 | Recall: 0.4211 | F1: 0.5926
    marital-status: Widowed, Count: 208
    Precision: 1.0000 | Recall: 0.1579 | F1: 0.2727
    occupation: ?, Count: 389
    Precision: 0.6667 | Recall: 0.4286 | F1: 0.5217
    occupation: Adm-clerical, Count: 726
    Precision: 0.6447 | Recall: 0.5104 | F1: 0.5698
    occupation: Armed-Forces, Count: 3
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    occupation: Craft-repair, Count: 821
    Precision: 0.6875 | Recall: 0.4862 | F1: 0.5696
    occupation: Exec-managerial, Count: 838
    Precision: 0.7962 | Recall: 0.7481 | F1: 0.7714
    occupation: Farming-fishing, Count: 193
    Precision: 0.5000 | Recall: 0.1786 | F1: 0.2632
    occupation: Handlers-cleaners, Count: 273
    Precision: 0.5714 | Recall: 0.3333 | F1: 0.4211
    occupation: Machine-op-inspct, Count: 378
    Precision: 0.5429 | Recall: 0.4043 | F1: 0.4634
    occupation: Other-service, Count: 667
    Precision: 0.5556 | Recall: 0.1923 | F1: 0.2857
    occupation: Priv-house-serv, Count: 26
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    occupation: Prof-specialty, Count: 828
    Precision: 0.7848 | Recall: 0.7628 | F1: 0.7736
    occupation: Protective-serv, Count: 136
    Precision: 0.7812 | Recall: 0.5952 | F1: 0.6757
    occupation: Sales, Count: 729
    Precision: 0.7247 | Recall: 0.6719 | F1: 0.6973
    occupation: Tech-support, Count: 189
    Precision: 0.7333 | Recall: 0.6471 | F1: 0.6875
    occupation: Transport-moving, Count: 317
    Precision: 0.6170 | Recall: 0.4531 | F1: 0.5225
    relationship: Husband, Count: 2,590
    Precision: 0.7345 | Recall: 0.6906 | F1: 0.7119
    relationship: Not-in-family, Count: 1,702
    Precision: 0.8222 | Recall: 0.3936 | F1: 0.5324
    relationship: Other-relative, Count: 178
    Precision: 1.0000 | Recall: 0.3750 | F1: 0.5455
    relationship: Own-child, Count: 1,019
    Precision: 1.0000 | Recall: 0.1765 | F1: 0.3000
    relationship: Unmarried, Count: 702
    Precision: 0.9286 | Recall: 0.2889 | F1: 0.4407
    relationship: Wife, Count: 322
    Precision: 0.7194 | Recall: 0.6993 | F1: 0.7092
    race: Amer-Indian-Eskimo, Count: 71
    Precision: 0.6250 | Recall: 0.5000 | F1: 0.5556
    race: Asian-Pac-Islander, Count: 193
    Precision: 0.7818 | Recall: 0.6935 | F1: 0.7350
    race: Black, Count: 599
    Precision: 0.7917 | Recall: 0.5846 | F1: 0.6726
    race: Other, Count: 55
    Precision: 0.8000 | Recall: 0.6667 | F1: 0.7273
    race: White, Count: 5,595
    Precision: 0.7388 | Recall: 0.6380 | F1: 0.6847
    sex: Female, Count: 2,126
    Precision: 0.7423 | Recall: 0.5193 | F1: 0.6111
    sex: Male, Count: 4,387
    Precision: 0.7420 | Recall: 0.6577 | F1: 0.6973
    native-country: ?, Count: 125
    Precision: 0.7143 | Recall: 0.6452 | F1: 0.6780
    native-country: Cambodia, Count: 3
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    native-country: Canada, Count: 22
    Precision: 0.6667 | Recall: 0.7500 | F1: 0.7059
    native-country: China, Count: 18
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    native-country: Columbia, Count: 6
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    native-country: Cuba, Count: 19
    Precision: 0.8000 | Recall: 0.8000 | F1: 0.8000
    native-country: Dominican-Republic, Count: 8
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    native-country: Ecuador, Count: 5
    Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
    native-country: El-Salvador, Count: 20
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    native-country: England, Count: 14
    Precision: 0.6667 | Recall: 0.5000 | F1: 0.5714
    native-country: France, Count: 5
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    native-country: Germany, Count: 32
    Precision: 0.8462 | Recall: 0.8462 | F1: 0.8462
    native-country: Greece, Count: 7
    Precision: 0.0000 | Recall: 0.0000 | F1: 0.0000
    native-country: Guatemala, Count: 13
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    native-country: Haiti, Count: 6
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    native-country: Honduras, Count: 4
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    native-country: Hong, Count: 8
    Precision: 0.5000 | Recall: 1.0000 | F1: 0.6667
    native-country: Hungary, Count: 3
    Precision: 1.0000 | Recall: 0.5000 | F1: 0.6667
    native-country: India, Count: 21
    Precision: 0.7500 | Recall: 0.7500 | F1: 0.7500
    native-country: Iran, Count: 12
    Precision: 0.3333 | Recall: 0.2000 | F1: 0.2500
    native-country: Ireland, Count: 5
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    native-country: Italy, Count: 14
    Precision: 0.7500 | Recall: 0.7500 | F1: 0.7500
    native-country: Jamaica, Count: 13
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    native-country: Japan, Count: 11
    Precision: 0.7500 | Recall: 0.7500 | F1: 0.7500
    native-country: Laos, Count: 4
    Precision: 1.0000 | Recall: 0.0000 | F1: 0.0000
    native-country: Mexico, Count: 114
    Precision: 1.0000 | Recall: 0.3333 | F1: 0.5000
    native-country: Nicaragua, Count: 7
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    native-country: Peru, Count: 5
    Precision: 0.0000 | Recall: 0.0000 | F1: 0.0000
    native-country: Philippines, Count: 35
    Precision: 1.0000 | Recall: 0.6875 | F1: 0.8148
    native-country: Poland, Count: 14
    Precision: 0.5000 | Recall: 1.0000 | F1: 0.6667
    native-country: Portugal, Count: 6
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    native-country: Puerto-Rico, Count: 22
    Precision: 0.8333 | Recall: 0.8333 | F1: 0.8333
    native-country: Scotland, Count: 3
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    native-country: South, Count: 13
    Precision: 0.3333 | Recall: 0.5000 | F1: 0.4000
    native-country: Taiwan, Count: 11
    Precision: 0.8000 | Recall: 1.0000 | F1: 0.8889
    native-country: Thailand, Count: 5
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    native-country: Trinadad&Tobago, Count: 3
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    native-country: United-States, Count: 5,870
    Precision: 0.7402 | Recall: 0.6314 | F1: 0.6815
    native-country: Vietnam, Count: 5
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000
    native-country: Yugoslavia, Count: 2
    Precision: 1.0000 | Recall: 1.0000 | F1: 1.0000


## Ethical Considerations
This model makes predictions based on demographic information. There is a risk of introducing human bias into the model. Users should consider the implications of using potentially biased models.

## Caveats and Recommendations
The model's accuracy may vary across demographic groups, as shown by performance metrics on data slices.
It is recommended to regularly update the model with new data to ensure its accuracy.
