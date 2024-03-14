from django.db import models

# Create your models here.


class Invoice(models.Model):
    """ Model representing an invoice. """

    number = models.CharField(max_length=36)
    amount = models.DecimalField("Total Invoice Amount",
                                 decimal_places=2,
                                 max_digits=20,
                                 blank=True, null=True, default=0)
    supplier_reference = models.CharField(max_length=36)
    supplier_company_name = models.CharField(max_length=40)
    supplier_govt_id = models.IntegerField()
    bar_code = models.IntegerField()
    issuer_name = models.CharField(max_length=20)
    
    #date_posted = models.DateField()
    #date_posted = timezone.now()
    #DateField(default=django.utils.timezone.now)


    def __str__(self) -> str:
        return self.number