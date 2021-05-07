from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.base import BaseEstimator
import pandas as pd
from sklearn.metrics import classification_report
import numpy as np

class BaseModel: 
    def __init__(self, estimator:BaseEstimator=RandomForestClassifier()):
        """
        Initialize the objetct. 
        
        parameters
        ----------
        estimator: BaseEstimator 
            A scickit-learn estimator 

        Returns
        -------
            None 
        """
        self.estimator = estimator
       
    def fit(self, X:pd.DataFrame, y:pd.Series) -> None: 
        """
        Fits the underlying estimator. 
        
        parameters
        ----------
        X: pd.DataFrame 
            features
        y: pd.Series
            labels

        Returns
        -------
           None 
        """
        self.estimator.fit(X, y)
        
    def predict(self, X:pd.DataFrame) -> np.array:
        """
        generates a prediction based on the underlying fitted model. 
        
        parameters
        ----------
        X: pd.DataFrame 
            features

        Returns
        -------
        y_pred: pd.Series
            labels 
        """
        y_pred = self.estimator.predict(X)
        return y_pred

    def validate(self, X_test:pd.DataFrame, y_test:pd.Series) -> str :
        """
        validates the  model using test data.
        
        parameters
        ----------
        X_test: pd.DataFrame 
            features
        y_test: pd.Series
            labels   

        Returns
        -------
        classification_report: str
            report with the main classification metrics.
        """
        y_pred = self.predict(X_test)
        report = classification_report(y_test, y_pred)
        return report

    def save(self, file_path:str) -> None:
        """
        save the model to a serialized pickle file

        parameters
        ----------
        file_path: str 
            path to output file.

        Returns
        -------
            None.
        """
        with open(file_path, 'wb') as handle:
            pickle.dump(self, handle)

        
