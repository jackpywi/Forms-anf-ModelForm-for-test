from django.db import models


class Snippet(models.Model):

    """ filds for forms """

    name = models.CharField(max_length=100)
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.name
