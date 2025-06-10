import os
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import json

from sklearn.metrics import mean_absolute_error, mean_squared_error, classification_report, roc_auc_score, average_precision_score, confusion_matrix

class Eval:
    def __init__(self, X_train: pd.DataFrame, X_test: pd.DataFrame, y_train: pd.Series, y_test:pd.Series, fitted_model, n_test: int, freq: str = 'D'):
        """
        Initializing the dataset
        """
        self.X_train = X_train.copy()
        self.X_test = X_test.copy()
        self.y_train = y_train.squeeze() if hasattr(y_train, 'squeeze') else pd.Series(y_train)
        self.y_test = y_test.squeeze() if hasattr(y_test, 'squeeze') else pd.Series(y_test)
        for s in (X_train, X_test, y_train, y_test):
            s.index = pd.DatetimeIndex(s.index)
            inferred_freq = pd.infer_freq(s.index)
            if inferred_freq != freq:
                print(f"Warning: Inferred Frequency is '{inferred_freq}' (expected '{freq}'). Proceeding without forcing frequncy")
                s.index = pd.DatetimeIndex(s.index)
            else:
                s.index = pd.DatetimeIndex(s.index, freq = freq)
        self.fitted = fitted_model
        self.n_test = n_test

    def Evaluate(self):
        """
        Function to evaluate error, report, AUC and ROC
        """
        try:
            fc = self.fitted.get_forecast(steps=self.n_test, exog=self.X_test)
            y_pred = fc.predicted_mean
            ci = fc.conf_int()
            # align to test index
            y_pred.index = self.y_test.index
            ci.index     = self.y_test.index

            # 2) Metrics
            mse = mean_squared_error(self.y_test, y_pred)
            mae = mean_absolute_error(self.y_test, y_pred)
            print(f"Test MSE: {mse:.4f}, MAE: {mae:.4f}")

            # 3) Build results DataFrame
            df = pd.DataFrame({
                'actual':       self.y_test,
                'predicted':    y_pred,
                'lower_ci':     ci.iloc[:, 0],
                'upper_ci':     ci.iloc[:, 1]
            })
            print("\n === Forecast Result Sample ===")
            print(df.head())

            # 4) Plot
            plt.figure(figsize=(12,5))
            plt.plot(self.y_train.index, self.y_train, label='Train (actual)')
            plt.plot(self.y_train.index, self.fitted.fittedvalues, '--', label = 'Train Fit')
            plt.plot(self.y_test.index, y_pred, '--', label = 'Test Forecast')
            plt.plot(self.y_test.index, self.y_test, label = 'Test Actual')
            plt.fill_between(ci.index,
                             ci.iloc[:,0],
                             ci.iloc[:,1],
                             color='gray', alpha=0.3, label='95% CI')
            plt.legend()
            plt.title("ARIM\AX: Train vs Test Forecast")
            plt.show()

            return df, {'MSE': mse, 'MAE': mae}
        except Exception as e:
            print("Error during evaluation")
            raise Exception(e)

#---------------------------------------------------------This ends the Evaluate File--------------------------------------------------------------

