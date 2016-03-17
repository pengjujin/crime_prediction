import pandas as pd 
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing
from sklearn.metrics import log_loss
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression

train_data_path = ""
test_data_path = ""

date_parser = lambda date: pd.date.time.strptime(date, '%Y-%m-%d %H:%M:%S')
train = pd.read_csv(train_data_path, parse_dates = ['Dates'], date_parser = date_parser)
test = pd.read_csv(test_data_path, parse_dates=['Dates'], date_parser = date_parser)

crime_encoder = preprocessing.LabelEncoder()
crime = crime_encoder.fit_transform(train.Category)

#build the training data features
days = pd.get_dummies(train.DayOfWeek)
district = pd.get_dummies(train.PdDistrict)
hour = pd.get_dummies(train.Dates.dt.hour)

train_data = pd.concat([hour, days, district], axis = 1)
train_data['crime'] = crime