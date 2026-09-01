from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
import json
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import StudentSerializer

@csrf_exempt
def create_students(request):
    if request.method == "POST":
        body= json.loads(request.body)
        student= Student.objects.create(
            name=body.get["name"],
            email=body.get["email"],
            department=body.get["department"],
            cgpa=body.get["cgpa"]
        )

        return JsonResponse(
            {"message": f"Student {student.name} created successfully."},
            status=201
        )
    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)

class StudentCreate(APIView):
    def post(self,request):
        data=request.data
        serializer=StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(f"Successfully created student {serializer.data['name']}",status=201)
        return Response(serializer.errors,status=400)

@csrf_exempt
def update_students(request):
    body=json.loads(request.body)
    if request.method=="PUT":
        try:
            student=Student.objects.get(id=body.get("id"))
            student.name=body.get("name",student.name)
            student.email=body.get("email",student.email)
            student.department=body.get("department",student.department)
            student.cgpa=body.get("cgpa",student.cgpa)
            student.save()
            return JsonResponse({"message": f"Student {student.name} updated successfully."})
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found."}, status=404)

class StudentUpdate(APIView):
    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@csrf_exempt
def delete_students(request):
    if request.method=="DELETE":
        body=json.loads(request.body)
        try:
            student=Student.objects.get(id=body.get("id"))
            student.delete()
            return JsonResponse({"message": f"Student {student.name} deleted successfully."})
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found."}, status=404)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found."}, status=404)

class StudentDelete(APIView):       
    def delete(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=404)
        student.delete()
        return Response({"message": "Deleted"})

def students(request):
    data=[]
    for student in Student.objects.all():
        data.append({
            "id":student.id,
            "name":student.name,
            "email":student.email,  
            "department":student.department,
            "cgpa":student.cgpa,
        })
    return JsonResponse(data,safe=False)

class Studentlist(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer=StudentSerializer(students,many=True)

        return Response(serializer.data)

def student_detail(request, idd):
    try:
        student = Student.objects.get(id=idd)
        return JsonResponse({
            "id":student.id,
            "name":student.name,
            "email":student.email,          
            "department":student.department,
            "cgpa":student.cgpa
        })
    except Student.DoesNotExist:
        return JsonResponse({"error": "Student not found"},status=404)

class StudentDetail(APIView):
    def get(self,request,id):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student)

        return Response(serializer.data)


def student_details(request, idd, name):
    return HttpResponse(f"student {idd} with name {name}")

def debug_view(request):
    print("method:", request.method)
    print("path:", request.path)
    print("headers:", request.headers)
    print("browser info:",request.headers.get('User-Agent'))
    return HttpResponse("Debug information printed to console.")

def home(request):
    department = request.GET.get('department')
    return HttpResponse(f"depp: {department}")

# Create your views here.