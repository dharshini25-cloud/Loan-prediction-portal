from django.db import models
from django.utils import timezone


class LoanPrediction(models.Model):
    gender = models.CharField(max_length=10)
    married = models.CharField(max_length=10)
    dependents = models.CharField(max_length=10)
    education = models.CharField(max_length=20)
    self_employed = models.CharField(max_length=10)

    applicant_income = models.FloatField()
    coapplicant_income = models.FloatField()
    loan_amount = models.FloatField()
    loan_term = models.FloatField()
    credit_history = models.FloatField()
    property_area = models.CharField(max_length=20)

    result = models.CharField(max_length=20)

    
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.result