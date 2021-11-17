from django.shortcuts import render
from rest_framework import views, status, parsers
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from .models import Course
from .forms import CourseForm
from django.http import JsonResponse, HttpResponse
from .serializers import CourseSerializers


@csrf_exempt
def courses_list(request):
    """
    List all courses or create a new course
    """
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializers(instance=courses, many=True)
        return JsonResponse(data=serializer.data, status=status.HTTP_200_OK, safe=False)
    elif request.method == 'POST':
        data = parsers.JSONParser().parse(request)
        serializer = CourseSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoezNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = CourseSerializers(instance=course)
        return JsonResponse(data=serializer.data, status=200)

    elif request.method in {"PUT", "PATCH"}:
        data = parsers.JSONParser().parse(request)
        serializer = CourseSerializers(instance=course, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.errors, status=400)

    elif request.method == "DELETE":
        course.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class CourseApiView(views.APIView):
    pass


class CourseView(generic.CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course.html'
    success_url = '/courses/'

