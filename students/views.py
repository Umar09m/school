from rest_framework import viewsets

from .models import Student
from .serializers import StudentSerializers


#
# class StudentListMixinView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#
# class StudentDetailMixinView(
#     mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView
# ):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
#
#     def get(self, request, pk, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)
#
#
# @csrf_exempt
# def student_list(request):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = StudentSerializers(instance=students, many=True)
#         return JsonResponse(data=serializer.data, status=status.HTTP_200_OK, safe=False)
#     elif request.method == 'POST':
#         data = parsers.JSONParser().parse(request)
#         serializer = StudentSerializers(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @csrf_exempt
# def student_detail(request, pk):
#     try:
#         student = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = StudentSerializers(instance=student)
#         return JsonResponse(data=serializer.data, status=200)
#
#     elif request.method in {"PUT", "PATCH"}:
#         data = parsers.JSONParser().parse(request)
#         serializer = StudentSerializers(instance=student, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data=serializer.data, status=200)
#         return JsonResponse(data=serializer.errors, status=400)
#
#     elif request.method == "DELETE":
#         student.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
#
#
# class StudentView(generic.CreateView):
#     model = Student
#     form_class = StudentForm
#     template_name = 'student.html'
#     success_url = '/students/'
#
#
# class StudentAPIVIew(views.APIView):
#
#     def get(self, request, *args, **kwargs):
#         students = Student.objects.all()
#         serializer = StudentSerializers(instance=students, many=True)
#         return response.Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, *args, **kwargs):
#         serializer = StudentSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
#
#
# class StudentDetailAPIView(views.APIView):
#
#     def get_object(self, pk):
#         try:
#             student = Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             return HttpResponse(status=404)
#
#     def get(self, request, pk):
#         student = self.get_object(pk=pk)
#         serializer = StudentSerializers(instance=student)
#         return response.Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def patch(self, request, pk, *args, **kwargs):
#         student = self.get_object(pk=pk)
#         data = parsers.JSONParser().parse(request)
#         serializer = StudentSerializers(instance=student, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(data=serializer.data, status=status.HTTP_200_OK)
#         return response.Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
#
#
# class StudentListCreateView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
#
#
# class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
#
#
# class StudentViewSet(viewsets.ViewSet):
#     """
#     A viewset for listing or retrieving students
#
#     """
#     def list(self, request):
#         queryset = Student.objects.all()
#         serializer = StudentSerializers(instance=queryset, many=True)
#         return response.Response(data=serializer.data)
#
#     def create(self, request):
#         serializer = StudentSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return response.Response(data=serializer.data)
#
#     def partial_update(self,request, pk=None):
#         queryset = Student.objects.all()
#         student = get_object_or_404(queryset, pk=pk)
#         serializer = StudentSerializers(instance=student, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return response.Response(data=serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Student.objects.all()
#         student = get_object_or_404(queryset, pk=pk)
#         serializer = StudentSerializers(instance=student)
#         return response.Response(data=serializer.data)
#
#     def destroy(self, request, pk=None):
#         queryset = Student.objects.all()
#         student = get_object_or_404(queryset, pk=pk)
#         student.delete()
#         return response.Response(status=status.HTTP_204_NO_CONTENT)


class StudentViewSet2(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers