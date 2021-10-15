# Define django models
from django.db import models
# Get lexicon handlers from pygments
from pygments.lexers import get_all_lexers
# Get styles from pygments
from pygments.styles import get_all_styles


# Define available parameters for lexicon
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# Define a class for handilng a snippet (i.e. a small piece of code)
class Snippet(models.Model):
    # Defines when the snippet has been created
    created = models.DateTimeField(auto_now_add=True)
    # Defines title of the snippet
    title = models.CharField(max_length=100, blank=True, default='')
    # Define code content
    code = models.TextField()
    # Other attributes for snippet
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    
    class Meta:
        ordering = ['created']
