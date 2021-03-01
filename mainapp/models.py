from django.db import models


# Create your models here.

class Yangilik(models.Model):
    title = models.CharField('Mavzu', max_length=250)
    full_info = models.TextField('To\'lik ma\'lumot')
    short_info = models.TextField('Qisqacha ma\'lumot')
    image = models.ImageField('Surat', upload_to='news')
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'
        db_table = 'news'

    def __str__(self):
        return self.title
