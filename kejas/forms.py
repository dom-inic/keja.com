from . models import MyKeja
from django import forms
from django.forms import ModelForm


class NewKeja(ModelForm):
    class Meta:
        model = MyKeja
        fields = ("property_name","property_image", "description", "location", "phone_no", "email_address", 
        "more_property_images", "property_specs", "category")
        widgets = {
            "property_name": forms.TextInput(
                attrs={
                    "required": True,
                    "placeholder": "type the name of your property here ....",
                    "class": "form-control",
                }
            ),
            # "property_image": forms.ImageField(
            
            # ),
            "description": forms.Textarea(
                attrs={
                    'cols': 80,
                    "required": True,
                    "placeholder":"brief description of the property...",
                    "class": "form-control",

                }
            ),
            "location": forms.TextInput(
                attrs={
                    "required": True,
                    "class":"form-control",
                }
            ),
            # "phone_no": forms.IntegerField(
        
            # ),
            # "email_address":forms.EmailField(
            #     widget=forms.TextInput(
            #         attrs={
            #             "class": "form-control",
            #             "required": True,
            #         }
            #     )
                

            # ),
            # "more_property_images":forms.ImageField(

            # ),
            "property_specs":forms.Textarea(
                attrs={
                    "class":"form-control",
                }
            ),
            "category":forms.TextInput(
                attrs={
                    "required":True,
                    "class":"form-control",
                }
            )
        }
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
    