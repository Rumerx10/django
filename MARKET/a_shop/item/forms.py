from django import forms
from .models import Item


INIPUT_CLASS = 'w-full py-4 px-6 rounded-xl border'
class NewItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description', 'price', 'image')

        widgets = {
            'category': forms.Select(attrs={
                'class': INIPUT_CLASS
            }),
            'name': forms.TextInput(attrs={
                'class': INIPUT_CLASS
            }),
            'description': forms.Textarea(attrs={
                'class': INIPUT_CLASS
            }),
            'price': forms.TextInput(attrs={
                'class': INIPUT_CLASS
            }),
            'image': forms.FileInput(attrs={
                'class': INIPUT_CLASS
            })
        }


class EditItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description', 'price', 'image', 'is_sold')

        widgets = {
            'category': forms.Select(attrs={
                'class': INIPUT_CLASS
            }),
            'name': forms.TextInput(attrs={
                'class': INIPUT_CLASS
            }),
            'description': forms.Textarea(attrs={
                'class': INIPUT_CLASS
            }),
            'price': forms.TextInput(attrs={
                'class': INIPUT_CLASS
            }),
            'image': forms.FileInput(attrs={
                'class': INIPUT_CLASS
            })
        }
