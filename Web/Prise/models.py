from django.db import models


class Led1(models.Model):
    led1 = models.BooleanField(default=False)
    
    def allumer(self):
        self.led1 = True
    
    
    def eteindre(self):
        self.led1 = False
      