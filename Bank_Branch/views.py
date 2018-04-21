from rest_framework.response import Response
from rest_framework.views import APIView
from Bank_Branch.models import bank_branch
from Bank_Branch.serializers import ifscbranchdetailsSerializers, citybranchdetailsSerializers
from django.http import HttpResponse
from django.shortcuts import render
import  csv


class Branch_details_of_ifsc(APIView):         # ProjectList view function
    def post(self, request):
        val = request.POST.get('ifsc_code')
        repo_obj = bank_branch.objects.filter(ifsc=val)
        serial = ifscbranchdetailsSerializers(repo_obj, many=True)
        print(serial)
        return Response(serial.data)

    def get(self, request):
        pass


class Branch_details_of_city(APIView):  # ProjectList view function
    def post(self, request):
        ct = request.POST.get('city_name')
        bnk = request.POST.get('bank_name')
        repo_obj = bank_branch.objects.filter(city=ct, bank_name=bnk)
        serial = citybranchdetailsSerializers(repo_obj, many=True)
        print(serial)
        return Response(serial.data)

    def get(self):
        pass



class home(APIView):
    def get(self, request):

        branch = bank_branch.objects.all()


        if(len(branch)==0):
            with open('/home/alok/Music/bank_branches.csv') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                count=0
                for row in readCSV:
                   bank_obj= bank_branch(ifsc=row[0], bank_id= row[1],branch=row[2], address=row[3], city=row[4], district=row[5], state=row[6], bank_name=row[7])
                   bank_obj.save()
                   if(count==1000):
                       break
                   count=count+1


            return render(request, 'home.html', {'data': "This is home page and Database is added now:"})

        else:

            return render(request, 'home.html', {'data': "This is home page and Database is already added:"})