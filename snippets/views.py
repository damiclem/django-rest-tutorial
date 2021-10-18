# Define HTTP module
from django.http import HttpResponse, JsonResponse, Http404
# Define module for CSFR protection
from django.views.decorators.csrf import csrf_exempt
# Define module for Django decorators
from rest_framework.decorators import api_view
# Define JSON parser
from rest_framework.parsers import JSONParser
# Define response module
from rest_framework.response import Response
# Define permissions module
# NOTE it holds pre-defined classes useful for rescticting access to given views
from rest_framework import permissions
# Define response status handler
from rest_framework import status
# Define API View class
from rest_framework.views import APIView
# Define MIXINs for REST framework
from rest_framework import mixins
# Define generic objects for REST framework
from rest_framework import generics
# Deine module for User
from django.contrib.auth.models import User
# Define modules for snippets
from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer


# # # NOTE Here CSFR protection is disabled, i.e. token is not requested
# # @csrf_exempt
# # NOTE @api_view decorator over a function define methods allowed to access it
# @api_view(['GET', 'POST'])
# # NOTE optional format suffix can be set to URLs
# def snippet_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         # List all snippets
#         snippets = Snippet.objects.all()
#         # Define snippet serializer 
#         serializer = SnippetSerializer(snippets, many=True)
#         # Return JSON-formatted snippet
#         # return JsonResponse(serializer.data, safe=False)
#         # NOTE request.data can handle request both in JSON or other formats!
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         # Define JSON-formatted request body
#         data = JSONParser().parse(request)
#         # Define serializer for snippet
#         serializer = SnippetSerializer(data=data)
#         # Continue only if serialized values are valid
#         if serializer.is_valid():
#             # Save serialized data
#             serializer.save()
#             # Return updated data, as JSON document
#             # return JsonResponse(serializer.data, status=201)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # Otherwise, return error
#         # return JsonResponse(serializer.errors, status=400)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # NOTE Class-based views allows for better separation between different (GET, POST, PUT, etc.) methods
# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


# # NOTE Mixins implement pieces of common behaviour
# class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     # NOTE what's happening there?
#     # We are building the view using GenericAPIView, then adding MIXINs
#     # The base class provides core functionality
#     # MIXINs provide .list(...) and .create(...) methods
#     # Then, those methods are explicitly bound to RESTful request
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# NOTE REST framework provides a lot of already MIXED-in generic views!
class SnippetList(generics.ListCreateAPIView):
    # Define query
    queryset = Snippet.objects.all()
    # Define serializer
    serializer_class = SnippetSerializer
    # Define permissions
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    # NOTE Overriding this method allows to define how the instance save is managed
    def perform_create(self, serializer):
        # NOTE Owner gets passed to save method
        serializer.save(owner=self.request.user)


# # @csrf_exempt
# @api_view
# def snippet_detail(request, pk, formta=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         # return HttpResponse(status=404)
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         # return JsonResponse(serializer.data)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         # data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=request.data)  # data=data)
#         if serializer.is_valid():
#             serializer.save()
#             # return JsonResponse(serializer.data)
#             return Response(serializer.data)
#         # return JsonResponse(serializer.errors, status=400)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         # return HttpResponse(status=204)
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    # Define query
    queryset = Snippet.objects.all()
    # Define serializer
    serializer_class = SnippetSerializer
    # Define permissions
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# List users
class UserList(generics.ListAPIView):
    # Define query
    queryset = User.objects.all()
    # Define serializer
    serializer_class = UserSerializer


# Get details of an user
class UserDetail(generics.RetrieveAPIView):
    # Define query
    queryset = User.objects.all()
    # Define serializer
    serializer_class = UserSerializer
