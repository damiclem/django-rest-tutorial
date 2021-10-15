# Define URLs module
from django.urls import path
# Import views library
from snippets import views


# Define URL patterns
urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]