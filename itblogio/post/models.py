from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
