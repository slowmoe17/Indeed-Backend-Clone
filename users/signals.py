from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User,EmployeeProfile,EmployerProfile

User = get_user_model()




@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.account_type == 'employee':
            EmployeeProfile.objects.create(user=instance)
        elif instance.account_type == 'employer':
            EmployerProfile.objects.create(user=instance)




        


    
