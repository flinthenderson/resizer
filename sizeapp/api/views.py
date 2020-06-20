from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from PIL import Image
from sizeapp.pillowsizer.resize import edit_and_save
from . serializers import ImagesSerializer
from sizeapp.models import Images
import os

class ImageUploadView(APIView):
	parser_class = (FileUploadParser)

	def post(self, request, *args, **kwargs):
		try:
			width = int(request.data['width'])
			height = int(request.data['height'])
			file_serializer = ImagesSerializer(data=request.data)

			if file_serializer.is_valid():
				file_serializer.save()
				print(file_serializer.data)

				filename = os.path.split(file_serializer.data['image'])[-1]
				BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
				im_path = os.path.join(BASE_DIR, 'media', 'uploads', filename)

				im = Image.open(im_path)
				im = im.resize((width, height))
				im.save(im_path)

				return Response(file_serializer.data, status=status.HTTP_201_CREATED)
			else:
				return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		except:
			return Response(status=status.HTTP_400_BAD_REQUEST)


class ListView(APIView):
	def get(self, request, format=None):
		images = Images.objects.all()
		serializer = ImagesSerializer(images, many=True)
		return Response({'images': serializer.data}, status=status.HTTP_200_OK)

class DetailView(APIView):
	def get(self, request, id):
		try:
			image = Images.objects.get(pk=id)
			serializer = ImagesSerializer(image)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)