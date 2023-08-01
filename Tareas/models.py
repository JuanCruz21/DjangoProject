from django.db import models
# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Tasks(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField(default=False)
    Projects = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return self.name