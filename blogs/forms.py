from django import forms
from blogs.models import CommentModel


class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        exclude = ['blog', 'created_at']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Name"}),
            'email': forms.EmailInput(attrs={'placeholder': "Email"}),
            'phone': forms.TextInput(attrs={'placeholder': "Phone"}),
            'comment': forms.Textarea(attrs={'placeholder': "Comment"}),
        }
