# Import authentication policies
# from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from authentication.authentication import BearerAuthentication
# Import permissions definition
from rest_framework.permissions import IsAuthenticated
# Import HTTP response module
from rest_framework.response import Response
# Import view module
from rest_framework.views import APIView


# Example view
class ExampleView(APIView):
    # Define authentication classes (types)
    authentication_classes = [BearerAuthentication]  # [SessionAuthentication, BasicAuthentication]
    # Define permission classes
    permission_classes = [IsAuthenticated]

    # Just return request fields
    # NOTE the main fields in a request generally are:
    # 1. request.user -> typically set to an instance of the contrib.auth package's User class;
    # 2. request.auth -> used for any additional authentication information (e.g. authentication token).
    def get(self, request, format=None):
        # Just return main request attributes+
        return Response({
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        })