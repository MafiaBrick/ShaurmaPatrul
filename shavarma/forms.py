from django.forms import ModelForm
from .models import comment

class commentForm(ModelForm):
    class Meta:
        model = comment
        fields = ['com','tasty','struct','orig']
