from rest_framework import views, response, status

from auth_app.serializers import UserSerializer


class UserRegisterAPIView(views.APIView):

	def post(self, request, *args, **kwargs):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return response.Response(serializer.data, status=status.HTTP_201_CREATED)
		return response.Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)