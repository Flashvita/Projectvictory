from django.urls import path
from customers.views import CustomeCreateView, CustomersListView


urlpatterns = [
    path('customers/create/', CustomeCreateView.as_view()),
    path('customers/list/', CustomersListView.as_view()),
]
