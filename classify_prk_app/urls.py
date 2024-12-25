from django.urls import path
from . import views

app_name = 'classify_prk_app'

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('classify_prk_before_delivery/', views.PRKPredictionBeforeDeliveryView.as_view(), name='classify_prk_before_delivery'),
    path('classify_prk_at_delivery/', views.PRKPredictionAtDeliveryView.as_view(), name='classify_prk_at_delivery'),
]
