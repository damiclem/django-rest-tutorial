# Define HTTP module
from django.http import HttpResponse, JsonResponse
# Define module for CSFR protection
from django.views.decorators.csrf import csrf_exempt
# Define module for Django decorators
from rest_framework.decorators import api_view
# Define JSON parser
from rest_framework.parsers import JSONParser
# Define response module
from rest_framework.response import Response
# Define response status handler
from rest_framework import status
# Define module for JSON parser
from snippets.models import Snippet
# Define serializer for JSON parser
from snippets.serializers import SnippetSerializer


# # NOTE Here CSFR protection is disabled, i.e. token is not requested
# @csrf_exempt
# NOTE @api_view decorator over a function define methods allowed to access it
@api_view(['GET', 'POST'])
# NOTE optional format suffix can be set to URLs
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        # List all snippets
        snippets = Snippet.objects.all()
        # Define snippet serializer 
        serializer = SnippetSerializer(snippets, many=True)
        # Return JSON-formatted snippet
        # return JsonResponse(serializer.data, safe=False)
        # NOTE request.data can handle request both in JSON or other formats!
        return Response(serializer.data)

    elif request.method == 'POST':
        # Define JSON-formatted request body
        data = JSONParser().parse(request)
        # Define serializer for snippet
        serializer = SnippetSerializer(data=data)
        # Continue only if serialized values are valid
        if serializer.is_valid():
            # Save serialized data
            serializer.save()
            # Return updated data, as JSON document
            # return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Otherwise, return error
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
@api_view
def snippet_detail(request, pk, formta=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        # return HttpResponse(status=404)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        # return JsonResponse(serializer.data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=request.data)  # data=data)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data)
            return Response(serializer.data)
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        # return HttpResponse(status=204)
        return Response(status=status.HTTP_204_NO_CONTENT)