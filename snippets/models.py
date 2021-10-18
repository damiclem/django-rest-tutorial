# Define django models
from django.db import models
# Define HTML formatter
from pygments.formatters.html import HtmlFormatter
# Get lexicon handlers from pygments
from pygments.lexers import get_all_lexers, get_lexer_by_name
# Get styles from pygments
from pygments.styles import get_all_styles
# Define highlights
from pygments import highlight


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
    # Define snippet owner
    # NOTE Owner is the foreign key to an actual User
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    # Define highlighted text
    highlighted = models.TextField()


    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        # Define lexer
        lexer = get_lexer_by_name(self.language)
        # Define attributes for snippet
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        # Set highlighted code
        self.highlighted = highlight(self.code, lexer, formatter)
        # Save snippet
        super(Snippet, self).save(*args, **kwargs)


    class Meta:
        ordering = ['created']
