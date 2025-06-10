import pandas as pd
import numpy as np
import time

from dataset import DataSet
from model import Model_ARIMA
from evaluate import Eval

class Train_Model:
    def __init__(self, X_train, X_test, y_train, y_test, fit_):
        """
        Initializes values.
        Parameters:
            - X_train, X_test: training set
            - y_train, y_test: pred test
            - fit_: fitted model
        """
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        fit_ = fit_

    def train(self):
        """
        Trains the model parmeters on forecast, test and train values
        Parameters:
            - Forecast tests: Forecasting model test, with steps usng y_test steps and X_test
            - ci_test: CI/CD testing
            - self.y_pred_test: Predicts mean vales in forecast test
        Returns:
            - self.y_train
            - ci_test
            - self.y_pred_test
            - forecast_test
            - self.n_test
        """
        try:
            print("Starting training model")
            time.sleep(3)
            fc = fit_.get_forecast(steps = len(self.X_test), exog = self.X_test)
            self.y_pred = fc.predicted_mean
            self.y_prob = np.full_like(self.y_test, np.nan, dtype = np.float64)
            print("Forecasting on test set")
            self.n_test = len(self.y_test)
            forecast_test = fit_.get_forecast(steps = self.n_test, exog = self.X_test)
            self.y_pred_test = forecast_test.predicted_mean
            ci_test = forecast_test.conf_int() 
            self.y_pred_test.index = self.y_test.index
            ci_test.index = self.y_test.index
            print("Starting evaluation mode")
            return self.y_pred, ci_test, self.y_pred_test, forecast_test, self.n_test, self.y_prob
        except Exception as e:
            print(f"Error received during training: {str(e)}")
            raise Exception(e)
if __name__ == "__main__":
    try:
        df = pd.read_csv(r"full_grouped.csv")
        print("Lets start the working flow\n")
        time.sleep(3)
        print(f"Visualizing the dataset: \n{df.head()}")
        D = DataSet(df)
        print("Preprocessing completed. Now going for dataset splitting using TrainTestSplit \n")
        time.sleep(3)
        X_train, X_test, y_train, y_test = D.split(test_size = 0.2)
        print(f"Shape of training dataset: X_train: {X_train.shape}, y_train: {y_train.shape}\n")
        print(f"Shape of testing dataset: X_test: {X_test.shape}, y_test: {y_test.shape}\n")
        print("Running model fit")

        D1 = Model_ARIMA(X_train, X_test, y_train, y_test)
        fit_ = D1.model_pipeline()
        D2 = Train_Model(X_train, X_test, y_train, y_test, fit_)
        y_pred, ci_test, y_pred_test, forecast_test, n_test, y_prob = D2.train()
        D3 = Eval(X_train, X_test, y_train, y_test, fit_, n_test)
        D3.Evaluate()
        print("Completed all steps:\n")
        print("Shutting down...")
        time.sleep(3)
    except Exception as e:
        print(f"Error received during computation training: {str(e)}")
        raise Exception(e)
#-------------------------------------------------------------This ends the Training File----------------------------------------------------------