from distutils.log import error
from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#   user_name = forms.CharField(label="Your Name", required=False, max_length=100, error_messages={
#      "required": "Your Name Must Not Be Empty",
#     "max_length": "Please Enter a Shorter Name"
# })
#review_text = forms.CharField(label="Your Feedback ", widget=forms.Textarea, max_length=200)
#rating=forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ['owner_comment']
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }

        error_messages = {
            "user_name": {
                "required": "Your Name Must Not Be Empty",
                "max_length": "Please Enter a Shorter Name"
            }
        }
