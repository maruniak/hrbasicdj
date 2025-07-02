from django.urls import path
from .views import employee_card_pdf

urlpatterns = [
    # ... ваши другие пути
    path('employee/<int:pk>/card/', employee_card_pdf, name='employee_card_pdf'),
]
