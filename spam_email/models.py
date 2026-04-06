from django.db import models

# Create your models here.
class Email(models.Model):
    email = models.TextField()
    is_spam=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email[:50] 
