from django import forms

from userinfo.models import UserInfo


class UserInfoForm(forms.ModelForm):
    name     = forms.CharField(required=True, label='', 
                    widget=forms.TextInput(attrs={"placeholder": "Your name"}))   # required=True is default
    email    = forms.EmailField()
    comments = forms.CharField(
                    required=False, 
                    widget=forms.Textarea(
                            attrs={
                                "placeholder": "Your Comment.",
                                "class": "new-class-name two",
                                "id": "my-id-for-textareas",
                                "rows": 20,
                                "cols": 100,
                            }
                        )
                    )
    age      = forms.DecimalField(initial=1)
   
    class Meta:
        model = UserInfo
        fields = [
            'name',
            'age',
            # datetime is set to default=datetime.now -> no need to display 'date'
            #'date',
            'comments',
            'featured',
        ]
    # This function checks the input for a specific word
    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get("name")

        # This way its easy to put in multiple validations
        if not "Yoda" in name:
            raise forms.ValidationError("This is not a valid name")
        if not "Mest" in name:
            raise forms.ValidationError("This is not a valid name")
        return name

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")

        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email
            
"""
    Form Fields:
    https://docs.djangoproject.com/en/2.2/ref/forms/fields/

    Form Widgets:
    https://docs.djangoproject.com/en/2.2/ref/forms/widgets/
"""

class RawUserInfoForm(forms.Form): # Standard Django Form
    name     = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))   # required=True is default
    comments = forms.CharField(
                    required=False, 
                    widget=forms.Textarea(
                            attrs={
                                "placeholder": "Your Comment.",
                                "class": "new-class-name two",
                                "id": "my-id-for-textareas",
                                "rows": 20,
                                "cols": 100,
                            }
                        )
                    )
    age      = forms.DecimalField(initial=1)
