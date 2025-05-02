from django.urls import path
from . import views

app_name = 'classify_prk_app'

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('classify_prk_wlab/', views.PRKPredictionWlabView.as_view(), name='classify_prk_wlab'),
    path('classify_prk_wolab/', views.PRKPredictionWolabView.as_view(), name='classify_prk_wolab'),
]
