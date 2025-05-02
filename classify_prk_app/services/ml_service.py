import os
import xgboost as xgb
import numpy as np
import pandas as pd
import joblib
from typing import Dict, Any
from sklearn.preprocessing import StandardScaler

class MLModelService:
    """Service for handling machine learning model operations."""

    def __init__(self):
        """Initialize the ML service with pre-trained models."""
        self.model_wlab = None
        self.model_wolab = None
        self.scaler_wlab = None
        self.scaler_wolab = None
        self.num_features_wlab = None
        self.num_features_wolab = None
        self._load_models()
        self._load_scalers()

    def _load_models(self) -> None:
        """Load the XGBoost models from files."""
        try:
            base_dir = os.path.dirname(os.path.dirname(__file__))

            # Load before delivery model with labs parametres
            model_wlab_path = os.path.join(base_dir, 'ml_models/xgboost_model_before_delivery_wlab_010525.json')
            self.model_wlab = xgb.XGBClassifier()
            self.model_wlab.load_model(model_wlab_path)

            # Load before delivery model without labs parametres
            model_wolab_path = os.path.join(base_dir, 'ml_models/xgboost_model_before_delivery_wolab_010525.json')
            self.model_wolab = xgb.XGBClassifier()
            self.model_wolab.load_model(model_wolab_path)

            print("Successfully loaded ML models")
        except Exception as e:
            print(f"Error loading ML models: {str(e)}")
            raise RuntimeError("Failed to load ML models")


    def _load_scalers(self) -> None:
        """Load the scalers from files."""
        try:
            base_dir = os.path.dirname(os.path.dirname(__file__))

            # Load before delivery scaler with labs parametres 
            scaler_wlab_path = os.path.join(base_dir, 'scalers/scalers_before_delivery_wlab_010525.pkl')
            self.scaler_wlab = joblib.load(scaler_wlab_path)
            self.num_features_wlab = self.scaler_wlab.feature_names_in_

            # Load before delivery scaler without labs parametres
            scaler_wolab_path = os.path.join(base_dir, 'scalers/scalers_before_delivery_wolab_010525.pkl')
            self.scaler_wolab = joblib.load(scaler_wolab_path)
            self.num_features_wolab = self.scaler_wolab.feature_names_in_
            
            print("Successfully loaded scalers")
        except Exception as e:
            print(f"Error loading scalers: {str(e)}")
            raise RuntimeError("Failed to load scalers")


    def predict_wlab(self, input_data: np.ndarray) -> Dict[str, Any]:
        """Make prediction using the before delivery with labs parameters model.
        
        Args:
            input_data: Numpy array of shape (1, n_features) containing the input features
            
        Returns:
            Dictionary containing prediction and probability scores
        """
        input_data_scaled = input_data.copy()
        input_data_scaled[self.num_features_wlab] = self.scaler_wlab.transform(input_data[self.num_features_wlab])
        input_data_scaled = pd.DataFrame(input_data_scaled, columns=input_data.columns)

        prediction = self.model_wlab.predict(input_data_scaled)
        probabilities = self.model_wlab.predict_proba(input_data_scaled)
        
        return {
            'prediction': int(prediction[0]),
            'probability': probabilities.tolist()
        }

    def predict_wolab(self, input_data: pd.DataFrame) -> Dict[str, Any]:
        """Make prediction using the before delivery model without labs parameters.
        
        Args:
            input_data: Numpy array of shape (1, n_features) containing the input features
            
        Returns:
            Dictionary containing prediction and probability scores
        """
        input_data_scaled = input_data.copy()
        input_data_scaled[self.num_features_wolab] = self.scaler_wolab.transform(input_data[self.num_features_wolab])
        input_data_scaled = pd.DataFrame(input_data_scaled, columns=input_data.columns)

        prediction = self.model_wolab.predict(input_data_scaled)
        probabilities = self.model_wolab.predict_proba(input_data_scaled)
        
        return {
            'prediction': int(prediction[0]),
            'probability': probabilities.tolist()
        }
