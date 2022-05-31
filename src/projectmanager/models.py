from django.db import models
from django.contrib.auth.models import User
# Create your models here.

TECH_STACK_OPTIONS = [
    (0, 'Vue'),
    (1, 'React'),
    (2, 'Angular'),
]


class Project(models.Model):
    name = models.CharField(max_length=128, null=False,
                            verbose_name='Project Name')
    description = models.TextField(null=True, verbose_name='Description')
    tech_stack = models.IntegerField(
        choices=TECH_STACK_OPTIONS, null=True, verbose_name='Tech Stack')

    created_by = models.ForeignKey(
        User, verbose_name='Creator', on_delete=models.SET_NULL, null=True)
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name='Create Time')

    def __str__(self):
        return self.name
