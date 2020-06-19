from rest_framework import serializers
from sizeapp.models import Images

class ImagesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Images
		fields = ['name', 'image']