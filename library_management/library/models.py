from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    total_copies = models.IntegerField(default=1)
    borrowed_copies = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15, blank=True)
    reading_preferences = models.JSONField(default=dict)  # JSON field to store genres they prefer

    def __str__(self):
        return self.user.username

class Transaction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student} borrowed {self.book}'
