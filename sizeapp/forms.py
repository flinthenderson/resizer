from django import forms
from sizeapp.models import Images

class ImagesForm(forms.ModelForm):
	class Meta:
		model = Images
		fields = "__all__"