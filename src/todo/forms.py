from django import forms
from .models import Todo


class TodoAddForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title',)


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'completed')
        # exclude = ('created_date')
