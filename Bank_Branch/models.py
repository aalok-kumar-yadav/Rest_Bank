from django.db import models


class bank_branch(models.Model):

    ifsc = models.CharField(max_length=100)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=400)
    district = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=400)

    def __str__(self):
        return self.bank_name
