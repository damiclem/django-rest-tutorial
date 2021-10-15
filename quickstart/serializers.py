# Define authentication modules
from django.contrib.auth.models import User, Group
# Define rest framework modules
from rest_framework import serializers


# Define serializer for user
# NOTE HyperlinkedModelSerializer handles resources retrievable from an endpoint
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']