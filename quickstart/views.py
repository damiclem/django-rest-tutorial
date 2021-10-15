# Import authentication modules
from django.contrib.auth.models import User, Group
# Import modules for views
from rest_framework import viewsets
# Import modules for permissions
from rest_framework import permissions
# Import custom serializer
from quickstart.serializers import UserSerializer, GroupSerializer


# NOTE probably methosd called hereby set objects' properties (using self)
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # Retrieve all users, order by joining time (descending)
    queryset = User.objects.all().order_by('-date_joined')
    # Define serializer class
    serializer_class = UserSerializer
    # Define permissions
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    # Select all group objects
    queryset = Group.objects.all()
    # Define serializer
    serializer_class = GroupSerializer
    # Define permissions
    permission_classes = [permissions.IsAuthenticated]
