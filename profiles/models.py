from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    
    # New fields
    phone_number = models.CharField(max_length=15, blank=True)
    facebook_url = models.URLField(max_length=200, blank=True)
    twitter_url = models.URLField(max_length=200, blank=True)
    linkedin_url = models.URLField(max_length=200, blank=True)
    skills = models.TextField(blank=True)
    education = models.TextField(blank=True)
    work_experience = models.TextField(blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    profile_views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def update_last_login(self):
        self.last_login = timezone.now()
        self.save()
    
    def get_completion_percentage(self):
        fields = [self.bio, self.location, self.birth_date, self.avatar,
                 self.phone_number, self.facebook_url, self.twitter_url,
                 self.linkedin_url, self.skills, self.education, self.work_experience]
        filled_fields = sum(1 for field in fields if field)
        return int((filled_fields / len(fields)) * 100)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
