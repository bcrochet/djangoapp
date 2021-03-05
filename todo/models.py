from django.db import models

# Create your models here.
class Todo(models.Model):
    def __str__(self):
        return self.todo_text

    todo_text = models.CharField(max_length=200)
    todo_done = models.BooleanField(default=False)
    add_date = models.DateTimeField(auto_now_add=True)
