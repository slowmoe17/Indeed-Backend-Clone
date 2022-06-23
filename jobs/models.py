from django.db import models
from users.models import User



class Job(models.Model):
    class attendance(models.TextChoices):
        remote = "remote"
        onsite = "on-site"
        hybrid = "hybrid"
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    job_title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.IntegerField()
    type = models.CharField(choices=attendance.choices,max_length=10)
    




    def __str__(self):
        return f' {self.recruiter.username} is hiring {self.job_title} for {self.salary}'



class Application(models.Model):
    applicant = models.ForeignKey(User,on_delete=models.CASCADE)
    Full_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    resume = models.FileField(upload_to='resumes/')


    
