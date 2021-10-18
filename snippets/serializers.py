# Import serializers library
from rest_framework import serializers
# Import snippet module
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
# Import user module
from django.contrib.auth.models import User


# class SnippetSerializer(serializers.Serializer):
class SnippetSerializer(serializers.ModelSerializer):
    # # ID of the snippet
    # id = serializers.IntegerField(read_only=True)
    # # Title of the snippet
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # # Code contained in the snippet
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # # Other snippet parameter
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    # NOTE This allows to read owner's username
    # The untyped ReadOnlyField is always read-only, and will be used for serialized representations,
    # but will not be used for updating model instances when they are deserialized
    owner = serializers.ReadOnlyField(source='owner.username')

    # Define meta-class
    # NOTE modelserializer is just a shurtcut for predefined fields (by model) and default create() and update() methods
    class Meta:
        # Define referenced model
        model = Snippet
        # Define fields in referenced model
        fields = [ 'id', 'title', 'code', 'linenos', 'language', 'style', 'owner', ]

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Snippet.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance


# Define serialize for User
class UserSerializer(serializers.ModelSerializer):
    # Define snippets
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())


    # Define metadata
    class Meta:
        # Define related model
        model = User
        # Define fields to serialize
        fields = ['id', 'username', 'snippets']