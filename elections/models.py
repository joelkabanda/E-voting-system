from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('voter', 'Voter'),
        ('election_commissioner', 'Election Commissioner')
    ]
# Create your models here.
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='voter')
    registration_number = models.CharField(max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username
    
class Post(models.Model):
    post_name =models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Candidate(models.Model):

    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='candidate_profile'
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='candidates'
    )

   
    def __str__(self):
        return f"{self.user.username} - {self.post.name}"
    
class Vote(models.Model):

    voter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='votes'
    )

    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name='votes_received'
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='votes'
    )

    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('voter', 'post')    
