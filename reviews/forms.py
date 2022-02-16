from distutils.log import error
from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", required=False, max_length=100, error_messages={
        "required": "Your Name Must Not Be Empty",
        "max_length": "Please Enter a Shorter Name"
    })
