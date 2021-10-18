# Import URLs module
from django.urls import path, include
# Import views library
from authentication import views
# Define suffix patterns
from rest_framework.urlpatterns import format_suffix_patterns


# Define URL patterns
urlpatterns = [
    path('token/', views.ExampleView.as_view(), name='token-exchange'),
]


# Append a set of available format suffix patterns
urlpatterns = format_suffix_patterns(urlpatterns)


# # Authentication view
# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
# ]