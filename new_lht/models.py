from django.db import models

# Create your models here.
class lht_main(models.Model):
    lht_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):

        return self.lht_text
