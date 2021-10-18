# Define URLs module
from django.urls import path
# Import views library
from snippets import views
# Define suffix patterns
from rest_framework.urlpatterns import format_suffix_patterns


# Define URL patterns
urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]


# Append a set of available format suffix patterns
urlpatterns = format_suffix_patterns(urlpatterns)
