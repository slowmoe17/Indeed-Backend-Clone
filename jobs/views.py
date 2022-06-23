from django import http
from django.shortcuts import render
from rest_framework import generics, status, permissions 
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Job, Application
from .serializers import JobSerializer, JobApplicationSerializer
from users.permissions import IsEmployer, IsEmployee, ReadOnly
from users.models import User , EmployeeProfile , EmployerProfile

class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsEmployer | ReadOnly,)

    def get_job_title(self):
        print (self.request.user.EmployeeProfile.job_title)

    def get_queryset(self):
        queryset = Job.objects.all()
        job_title = self.request.query_params.get('job_title', None)

        if job_title is not None:
            queryset = queryset.filter(job_title__contains=job_title,)

        else : 
            job_title=EmployeeProfile.objects.get(user=self.request.user).job_title
            queryset = queryset.filter(job_title=job_title)

            print(Job.objects.filter(
                job_title__contains=job_title
            )) 
        return queryset
    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)

class JobDelete(generics.DestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsEmployer | ReadOnly,)


    def get_object(self):
        queryset1 = Job.objects.filter(recruiter=self.request.user)
        job_id = self.request.query_params.get('id', None)
        if job_id is not None:
            queryset = queryset1.filter(id=job_id)
        return queryset
        
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return Response({"message": "Job deleted successfully"}, status=status.HTTP_200_OK)

    
    
        
    


        
        


            
        

        


    




class ApplicationListCreate(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = (permissions.AllowAny,)
    def get_queryset(self):
        queryset = Application.objects.all()
        # filter by query params : job title and job recruiter
        job_title = self.request.query_params.get('job_title', None)
        if job_title is not None:
            queryset = queryset.filter(job__job_title__contains=job_title)
        job_recruiter = self.request.query_params.get('recruiter', None)
        if job_recruiter is not None:
            queryset = queryset.filter(job__job_recruiter__contains=job_recruiter)
        return queryset
