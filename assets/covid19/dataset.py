#Dataset file
# Would process dataset based on covid-19 cases
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import time



from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split 


class DataSet:
        def __init__(self, df):
            """
            Dunder method to define class and OOP based computations.
            Parameters: 
                - df : DataFrame to be processed
                - self : OOP based implementation
            """
            print("Initializing the process for data preprocessing")
            time.sleep(3)
            self.df = df
            self.run_pipeline()

        def run_pipeline(self):
            """
            To run the pipeline once the object is created. An automated approach
            """
            print("Starting the process and preprocessing: ")
            time.sleep(3)
            self.df, self.df_t = self.preprocess()
            print("Now visualizing the result: ")
            time.sleep(3)
            self.visualize()

        def visualize(self):
            """
            Visualizing the dataset.
            Parameters:
                - self.df_t: The processed dataset before imputation.
                - date_range: complete range of our dataset
                - mdates: Locates the month to view cases on the plot.

            """
            try:
                if self.df_t is None: 
                    raise ValueError('Data not processed')
                print(f"Data Loaded Successfully! First five rows: \n", self.df_t.head())
                print(f"Printing the info with datatypes: \n")
                self.df_t.info()

                #plotting results of dataset before PCA
                date_range = pd.date_range(start = '2020-01-22', end = '2020-07-27', freq = 'D')
                np.random.seed(20)
                plt.figure(figsize =(12,6))
                # Plotting cases based data over the timeline
                plt.plot(self.df_t.index, self.df_t['Confirmed'], label = 'Confirmed cases', linewidth = 2, color = 'red')
                plt.plot(self.df_t.index, self.df_t['Deaths'], label = 'Deaths', linewidth = 2, color = 'blue')
                plt.plot(self.df_t.index, self.df_t['Recovered'], label = 'Recovered', linewidth = 2, color = 'purple')
                plt.plot(self.df.index, self.df_t['New cases'], label = 'New Cases', linewidth = 4, color = 'red')
                plt.plot(self.df_t.index, self.df_t['New deaths'], label = 'New deaths', linewidth = 4, color = 'blue')
                plt.plot(self.df_t.index, self.df_t['New recovered'], label = 'New recovered', linewidth = 4, color = 'purple')

                plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
                plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

                plt.xlabel('Date')
                plt.ylabel('Number of cases')
                plt.title('Daily Old, New, Deaths, Recovered And Total Cases')
                plt.legend()
                plt.xticks(rotation = 45)
                plt.tight_layout()
                plt.show()
            except Exception as e:
                print(f"Encountered error using {str(e)}")



        def preprocess(self):
            """
            Preprocesses the data for machine learning and model training.
            Parmeters: 
                - self.df: DataFrame
                - daily_country_counts: Converting the country occurances to a single int value
                - indexing: Indexing on daily, weekly and biweekly. Can do upto monthly and yearly but do not want to increase complexity on edge-devices
                - Imputer: Simple Imputer on numeric values only
                - Scaler: RobustScaler based on previous processed results
            Returns:
                - self.df: DataFrame

            """
            try:
                print("Starting Preprocessing of DataSet:\n ")
                #Indexing and parsing date
                self.df['Date'] = pd.to_datetime(self.df['Date'])
                self.df = self.df.sort_values('Date').set_index('Date')
                self.df.drop(columns = ['WHO Region'], inplace = True)

                self.df['daysofweek'] = self.df.index.dayofweek
                self.df['month'] = self.df.index.month
                #Generating daily cases
                daily = self.df.resample('D').size().to_frame('Total Cases')
                daily['t_cases'] = (daily['Total Cases'] > 0).astype(int)
                
                #Aggregating Daily Features
                agg = self.df.resample('D').agg({
                    'Confirmed' : 'sum',
                    'Deaths' : 'sum',
                    'Recovered' : 'sum',
                    'Active' : 'sum',
                    'New cases' : 'sum',
                    'New deaths' : 'sum',
                    'New recovered' : 'sum'
                    }).fillna(0)

                self.df_f = daily.join(agg)
                #creating lag features
                for lag in [1, 7, 14]:
                    self.df_f[f'lag_{lag}_case'] = self.df_f['t_cases'].shift(lag)
                self.df_f.dropna(inplace = True)
                
                #Adding country wise cases for optimal coding
                self.df_f['country_vals'] = self.df['Country/Region'].value_counts().to_dict()
                self.df_t = self.df_f
                self.target_name = ['New cases', 'New deaths', 'New recovered']
                #Creating datasplits
                X = self.df_f.drop(columns = self.target_name)
                y = self.df_f[self.target_name]
                print(f"Sample Size: X = {X.shape}, y = {y.shape}")

                num_cols = X.select_dtypes(include=[np.number]).columns.tolist()

                #working on imputers for numerical values only
                num_imp = SimpleImputer(strategy='mean')

                num_trans = Pipeline(steps = [
                    ('imputer', num_imp),
                    ('scaler', RobustScaler())
                    ])
                transformers = [('num', num_trans, num_cols)]
                print(f"After imputing: {X.head()}")
                self.preprocessor = ColumnTransformer(transformers)
                X_proc = self.preprocessor.fit_transform(X)
                #Buiding processed dataframe
                self.df = pd.DataFrame(X_proc, index = X.index)
                self.df[self.target_name] = y.loc[self.df.index]

                # View processed dataset
                print(f"Processed Dataset: \n{self.df.head()}")
                return self.df, self.df_t
            except Exception as e:
                print(f"Error received during preprocessing{str(e)}")
                raise Exception(e)

        def split(self, test_size = 0.2):
            """
            Splits the dataset into train and test datasets.
            Parameters:
                - X = self.df.drop(): Dataframe without the target column. The rest remains the same
                - y = self.df.dtop[target]: Only the target column

               - X_train, y_train: Splitted training dataset of X and y
               - X_test, y_test: Splitted training dataset of X and y

                - train_test_split(X,y,test_size, random_state: Sciket learn splitting function. Here;
                   -- Test_size: size of test to be used
                    -- random_state: shuffling and random rows.
                    -- stratify: To help imbalances in class

            Return:
                - X_train, y_train
                - X_test, y_test
            """
            try:
                target_cols = ['New cases']
                X = self.df.drop(columns = target_cols)
                y = self.df[target_cols]
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state = 20)
                
                return X_train, X_test, y_train, y_test
            except Exception as e:
                print(f"Error recceived during splitting: {str(e)}")
                raise Exception(e)




#------------------------------------------------------------This ends the Dataset File------------------------------------------------------------