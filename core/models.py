from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 40)
    email = models.EmailField(max_length = 40)
    current_credit = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def str(self):
        return self.name+ ' | Credit: ' +str(self.current_credit)