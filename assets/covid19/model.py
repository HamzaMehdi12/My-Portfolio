import numpy as np
import pandas as pd
import time
import joblib

from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA

from dataset import DataSet

class Model_ARIMA:
    def __init__(self, X_train: pd.DataFrame, X_test: pd.DataFrame , y_train: pd.Series, y_test: pd.Series, freq: str = 'D'):
        """
        Initializing model Arima
        Parameters:
            - self.X_train, X_test: Train and Test set
            - self.y_train, y_test: train and test predicted set
            - self.stepwise: auto_arima: identifying most optimal parameters for the ARIMA model. Learns the values for p and q. Based on y_train and X_train. Here
                -- seasonal: For any seasonality in our datsaset. Although there is none so far so false
        Returns: 
            - stepwise p and q learned values
        """
        try:
            #Ensuring datetime with specified frequency
            for series in [X_train, X_test, y_train, y_test]:
                series.index = pd.DatetimeIndex(series.index)
            self.X_train = X_train
            self.X_test = X_test
            self.y_train = y_train
            self.y_test = y_test
            self.stepwise = auto_arima(
                self.y_train, 
                exogenous = self.X_train, 
                start_p = 0, 
                start_q = 0,
                d = None,
                seasonal = False,
                trace = True,
                error_action = 'ignore',
                suppress_warnings=True,
                stepwise = True) #learning p and q
        except Exception as e:
            print(f"Error received while model computations: {str(e)}")
            raise Exception(e)
        
        
    def model_pipeline(self):
        """
        Fits the model ARIMA for further training of the model
        Parameters: 
            - self.order: stepwise order values learned by stepwise auto_arima function.
            - self.model  ARIMA: Model
            - self.fitted: Model.fit for parameter fitting of the model
        Returns:
            - self.fitted
        """
        
        try:
            print("Starting model fit")
            time.sleep(3)
            print("Selected ARIMA order: ", self.stepwise.order)
            self.order = self.stepwise.order
            self.model = ARIMA(endog= self.y_train, exog = self.X_train, order = self.order)
            self.fitted = self.model.fit()
            print(self.fitted.summary())
            print("Model fitting completed: Starting training")
            self.save_model()
            time.sleep(3)
            return self.fitted
        except Exception as e:
            print(f"Error received during model selection: {str(e)}")
            raise Exception(e)
        
    def save_model(self, filename = "arimax_model.pkl"):
        """
        Saves model
        """
        joblib.dump(self.fitted, filename)       
        


#---------------------------------------------------------------This Ends the Model File-----------------------------------------------------------