from django.http import JsonResponse, HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, parsers, views, response

from .forms import StudentForm
from .models import Student
from .serializers import StudentSerializers


@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializers(instance=students, many=True)
        return JsonResponse(data=serializer.data, status=status.HTTP_200_OK, safe=False)
    elif request.method == 'POST':
        data = parsers.JSONParser().parse(request)
        serializer = StudentSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializers(instance=student)
        return JsonResponse(data=serializer.data, status=200)

    elif request.method in {"PUT", "PATCH"}:
        data = parsers.JSONParser().parse(request)
        serializer = StudentSerializers(instance=student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.errors, status=400)

    elif request.method == "DELETE":
        student.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class StudentView(generic.CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student.html'
    success_url = '/students/'


class StudentAPIVIew(views.APIView):

    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentSerializers(instance=students, many=True)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)


class StudentDetailAPIView(views.APIView):

    def get_object(self, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk):
        student = self.get_object(pk=pk)
        serializer = StudentSerializers(instance=student)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        student = self.get_object(pk=pk)
        data = parsers.JSONParser().parse(request)
        serializer = StudentSerializers(instance=student, data=data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)
        return response.Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
