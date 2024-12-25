from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views import View
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
import numpy as np
from typing import Dict, Any

from .forms import BeforeDeliveryForm, AtDeliveryForm
from .services.ml_service import MLModelService

# Constants for model features
FEATURES_BEFORE_DELIVERY = [
    'placenta_previa',
    'indications_for_caesarean_1',
    'placenta_localization_3',
    'delivery_2_0',
    'age',
    'gestational_age',
    'fibrinogen'
]

FEATURES_AT_DELIVERY = [
    'bp_systolic',
    'heart_rate',
    'hemoglobin',
    'hematocrit',
    'thrombocytes',
    'prothrombin_index'
]

# Initialize ML service
ml_service = MLModelService()

class MainView(View):
    """View for rendering the main page with prediction forms."""
    
    template_name = 'classify_prk_app/main.html'
    
    def get(self, request: HttpRequest) -> HttpResponse:
        """Handle GET request and render main page with forms.
        
        Args:
            request: HTTP request object
        
        Returns:
            Rendered main page with prediction forms
        """
        context = {
            'before_delivery_form': BeforeDeliveryForm(),
            'at_delivery_form': AtDeliveryForm(),
        }
        return render(request, self.template_name, context)


class PRKPredictionBeforeDeliveryView(View):
    """View for handling PRK predictions before delivery."""

    @method_decorator(require_http_methods(["GET"]))
    def get(self, request: HttpRequest) -> JsonResponse:
        """Handle GET request for PRK prediction before delivery.
        
        Args:
            request: HTTP request object containing prediction parameters
            
        Returns:
            JsonResponse with prediction results or error message
        """
        try:
            form = BeforeDeliveryForm(request.GET)
            
            if not form.is_valid():
                return JsonResponse({'error': form.errors}, status=400)
                
            input_data = self._prepare_input_data(form.cleaned_data)
            prediction_result = ml_service.predict_before_delivery(input_data)
            
            print(f"Successfully made prediction for before delivery data: {input_data}")
            return JsonResponse(prediction_result)
            
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            return JsonResponse({'error': 'Internal server error'}, status=500)
    
    def _prepare_input_data(self, form_data: Dict[str, Any]) -> np.ndarray:
        """Prepare input data for model prediction.
        
        Args:
            form_data: Cleaned form data
            
        Returns:
            Numpy array with prepared input data
        """
        input_values = [float(form_data[feature]) for feature in FEATURES_BEFORE_DELIVERY]
        return np.array(input_values, dtype=float).reshape(1, -1)


class PRKPredictionAtDeliveryView(View):
    """View for handling PRK predictions at delivery."""

    @method_decorator(require_http_methods(["GET"]))
    def get(self, request: HttpRequest) -> JsonResponse:
        """Handle GET request for PRK prediction at delivery.
        
        Args:
            request: HTTP request object containing prediction parameters
            
        Returns:
            JsonResponse with prediction results or error message
        """
        try:
            form = AtDeliveryForm(request.GET)
            
            if not form.is_valid():
                return JsonResponse({'error': form.errors}, status=400)
                
            input_data = self._prepare_input_data(form.cleaned_data)
            prediction_result = ml_service.predict_at_delivery(input_data)
            
            print(f"Successfully made prediction for at delivery data: {input_data}")
            return JsonResponse(prediction_result)
            
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            return JsonResponse({'error': 'Internal server error'}, status=500)
    
    def _prepare_input_data(self, form_data: Dict[str, Any]) -> np.ndarray:
        """Prepare input data for model prediction.
        
        Args:
            form_data: Cleaned form data
            
        Returns:
            Numpy array with prepared input data
        """
        input_values = [float(form_data[feature]) for feature in FEATURES_AT_DELIVERY]
        return np.array(input_values, dtype=float).reshape(1, -1)
