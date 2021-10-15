# Define HTTP module
from django.http import HttpResponse, JsonResponse
# Define module for CSFR protection
from django.views.decorators.csrf import csrf_exempt
# Define JSON parser
from rest_framework.parsers import JSONParser
# Define module for JSON parser
from snippets.models import Snippet
# Define serializer for JSON parser
from snippets.serializers import SnippetSerializer


# NOTE Here CSFR protection is disabled, i.e. token is not requested
@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        # List all snippets
        snippets = Snippet.objects.all()
        # Define snippet serializer 
        serializer = SnippetSerializer(snippets, many=True)
        # Return JSON-formatted snippet
        return JsonResponse(serializer.data, safe=False)

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
            return JsonResponse(serializer.data, status=201)
        # Otherwise, return error
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)