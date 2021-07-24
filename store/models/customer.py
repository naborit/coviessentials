from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50,null=False )
    last_name = models.CharField(max_length=50,null=False)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    confirm_password=models.CharField(max_length=500,default=1)

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


    def register(self):
        self.save()

    def isExits(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
