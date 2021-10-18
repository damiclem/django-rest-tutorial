# Define URLs module
from django.urls import path, include
# Import views library
from snippets import views
# Import viewsets library
from snippets.views import SnippetViewSet, UserViewSet, api_root
# Define router
from rest_framework.routers import DefaultRouter
# Define suffix patterns
from rest_framework.urlpatterns import format_suffix_patterns


# # NOTE when using ViewSet instead of View,
# # URLs must be explicitly bounded!
# snippet_list = SnippetView.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# })
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })


# NOTE using ViewSet instead of View, we can use a router
# instead of manually binding routes
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


# Define URL patterns
# NOTE in order to use hyperlinked documents, it is necessary to name endpoints
urlpatterns = [
    # # Root path
    # # path('', views.api_root),
    # path('', api_root),
    # # NOTE with class-based views, instances expose (POST, GET, etc.) methods
    # # path('snippets/', views.SnippetList.as_view(), name='snippet-list'),  # path('snippets/', views.snippet_list),
    # path('snippets/', snippet_list, name='snippet-list'),
    # # path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),  # path('snippets/<int:pk>/', views.snippet_detail),
    # path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    # # path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    # path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    # #  path('users/', views.UserList.as_view(), name='user-list'),
    # path('users/', user_list, name='user-list'),
    # # path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    # path('users/<int:pk>/', user_detail, name='user-detail'),
    # NOTE router binds routes automatically
    path('', include(router.urls)),
]


# # Append a set of available format suffix patterns
# urlpatterns = format_suffix_patterns(urlpatterns)


# Authentication view
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]