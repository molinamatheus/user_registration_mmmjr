import csv
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from project.quickstart.serializers import UserSerializer
from django.http import HttpResponse, JsonResponse
from project.quickstart.models import User
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def user_list(request):
    """
    List all code User, or create a new User.
    """
    if request.method == 'GET':
        format = request.GET.get("format")
        print(format)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        if format == "csv":
            response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="project_frexco.csv"'},
            )
            writer = csv.writer(response)
            writer.writerow(['username', 'email', 'password', 'birthday'])
            for item in users:
                writer.writerow([item.get('username'), item.get('email'), item.get('password'), item.get('birthday')])
            
            return csv

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        def password_random(username):
            new_password = ""
            for letra in username:
                if letra in 'Aa': new_password += '10'
                elif letra in 'Bb': new_password += '11'
                elif letra in 'Cc': new_password += '12'
                elif letra in 'Dd': new_password += '13'
                elif letra in 'Ee': new_password += '14'
                elif letra in 'Ff': new_password += '15'
                elif letra in 'Rr': new_password += '#'
                elif letra in 'Ss': new_password += '$'
                elif letra in 'Mm': new_password += '?'
                else: new_password += letra
            return(new_password)

        data = JSONParser().parse(request)
        username = data.get("username")
        password_test = ""
        password = data.get("password")

        if password == password_test or password is None:
            data["password"] = password_random(username)
      
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
