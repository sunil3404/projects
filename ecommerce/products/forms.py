from django import forms
from products.models import Brand
from django.core.exceptions import ValidationError


class ProductForm(forms.Form):
    product_name = forms.CharField(label="Product Name", 
            widget=forms.TextInput(attrs={"class" : "form-control", "cols" : "2"}), max_length=100)
    product_description = forms.CharField(label="Description",
            widget = forms.Textarea(attrs={"class" : "form-control", "cols": "4", "rows" : "8"}))
    product_price = forms.IntegerField(label="Price", 
            widget=forms.NumberInput(attrs={"class" : "form-control"}))
    product_image = forms.ImageField(label="Image",
            widget = forms.FileInput(attrs={"class" : "form-control", "required" : "false"}))
    brand_id = forms.ModelChoiceField(queryset = Brand.objects.all(), widget=forms.Select(attrs={"class" : "form-control"}))


    def clean_product_image(self):
        img_ext = self.cleaned_data['product_image']
        if "jpeg" not in img_ext.name:
            raise ValidationError("Image must be jpeg")
        return img_ext
