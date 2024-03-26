from django.urls import path
from apiminerva import views

app_name = 'apiminerva'

urlpatterns = [
    path('criarlistarpessoa/', views.PessoaListAndCreate.as_view(), name='PessoaListAndCreate'),
    path('modificarpessoa/<int:pk>/', views.PessoaDetailAndChangeAndDelete.as_view(), name='PessoaDetailAndChangeAndDelete'),
    path('criarlistaraviso/', views.AvisoListAndCreate.as_view(), name='AvisoListAndCreate'),
    path('modificaraviso/<int:pk>/', views.AvisoDetailAndChangeAndDelete.as_view(), name='AvisoDetailAndChangeAndDelete'),

]