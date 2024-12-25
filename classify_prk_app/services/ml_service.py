import os
import xgboost as xgb
import numpy as np
from typing import Dict, Any

class MLModelService:
    """Service for handling machine learning model operations."""

    def __init__(self):
        """Initialize the ML service with pre-trained models."""
        self.model_before_delivery = None
        self.model_at_delivery = None
        self._load_models()

    def _load_models(self) -> None:
        """Load the XGBoost models from files."""
        try:
            base_dir = os.path.dirname(os.path.dirname(__file__))

            # Load before delivery model
            model_before_path = os.path.join(base_dir, 'ml_models/xgboost_model_before_delivery.json')
            self.model_before_delivery = xgb.XGBClassifier()
            self.model_before_delivery.load_model(model_before_path)

            # Load at delivery model
            model_at_path = os.path.join(base_dir, 'ml_models/xgboost_model_at_delivery.json')
            self.model_at_delivery = xgb.XGBClassifier()
            self.model_at_delivery.load_model(model_at_path)

            print("Successfully loaded ML models")
        except Exception as e:
            print(f"Error loading ML models: {str(e)}")
            raise RuntimeError("Failed to load ML models")

    def predict_before_delivery(self, input_data: np.ndarray) -> Dict[str, Any]:
        """Make prediction using the before delivery model.
        
        Args:
            input_data: Numpy array of shape (1, n_features) containing the input features
            
        Returns:
            Dictionary containing prediction and probability scores
        """
        prediction = self.model_before_delivery.predict(input_data)
        probabilities = self.model_before_delivery.predict_proba(input_data)
        
        return {
            'prediction': int(prediction[0]),
            'probability': probabilities.tolist()
        }

    def predict_at_delivery(self, input_data: np.ndarray) -> Dict[str, Any]:
        """Make prediction using the at delivery model.
        
        Args:
            input_data: Numpy array of shape (1, n_features) containing the input features
            
        Returns:
            Dictionary containing prediction and probability scores
        """
        prediction = self.model_at_delivery.predict(input_data)
        probabilities = self.model_at_delivery.predict_proba(input_data)
        
        return {
            'prediction': int(prediction[0]),
            'probability': probabilities.tolist()
        }
