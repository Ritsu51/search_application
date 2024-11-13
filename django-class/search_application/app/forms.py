from django import forms
from .models import Product

class SearchForm(forms.Form):
    query = forms.CharField(
        label='検索キーワード',
        max_length=100,  # CharField で max_length が有効です
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '検索したいキーワ ードを入力'}),
        # favorite = forms.BooleanField(label="check",required = False)
    )

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'max_damage', 'category']