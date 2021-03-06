from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.

class Yangilik(models.Model):
    title = models.CharField('Mavzu', max_length=250)
    short_info = models.TextField('Qisqacha ma\'lumot')
    image = models.ImageField('Surat', upload_to='news')
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    full_info = RichTextUploadingField('To\'lik ma\'lumot')

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'
        db_table = 'news'

    def __str__(self):
        return self.title


class Xodim(models.Model):
    name = models.CharField('Ism', max_length=100, blank=True)
    surname = models.CharField('Familiya', max_length=100, blank=True)
    speciality = models.CharField('Mutaxasisligi', max_length=200, blank=True)
    info = models.TextField('Ma\'lumot', blank=True)
    image = models.ImageField('Surat', upload_to='xodimlar')
    facebook = models.CharField('Facebook', max_length=250, blank=True)
    telegram = models.CharField('Telegram', max_length=250, blank=True)
    insta = models.CharField('Instagram', max_length=250, blank=True)

    class Meta:
        verbose_name = 'Xodim'
        verbose_name_plural = 'Xodimlar'
        db_table = 'xodimlar'

    def __str__(self):
        return self.name


class BizningIshlarimiz(models.Model):
    title = models.CharField('Mavzu', max_length=250)
    short_info = models.TextField('Qisqacha ma\'lumot')
    image = models.ImageField('Surat', upload_to='bizning-ishlar')
    created_dt = models.DateTimeField(auto_now_add=True)
    full_info = RichTextUploadingField('To\'lik ma\'lumot')

    class Meta:
        verbose_name = 'Bizning Ish'
        verbose_name_plural = 'Bizning Ishlarimiz'
        db_table = 'bizning_ishlar'

    def __str__(self):
        return self.title


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Korxona(SingletonModel):
    name = models.CharField('Korxona nomi', max_length=250)
    telegram = models.CharField('Korxona egasining telegram ID si', max_length=100)
    main_image = models.ImageField('Bosh saxifa uchun surat', upload_to='korxona-haqida')
    short_info = RichTextUploadingField('Qisqacha ma\'lumot')
    full_info = RichTextUploadingField('To\'liq ma\'lumot')
    quote_index_page = models.TextField('Iqtibos')
    quote_name = models.CharField('Iqtibos vakili', max_length=250)
    quote_job = models.CharField('Iqtibos vakilining kasbi', max_length=250)
    quote_image = models.ImageField('Iqtibos surat', upload_to='bizning-ishlar')

    class Meta:
        verbose_name = 'Korxona'
        verbose_name_plural = 'Korxona'
        db_table = 'korxona'

    def __str__(self):
        return self.name


class Xabar(models.Model):
    name = models.CharField('Mijozning ismi', max_length=250)
    phone = models.CharField('Mijozning raqami', max_length=15)
    message = models.TextField('Xabar')

    class Meta:
        verbose_name = 'Xabar'
        verbose_name_plural = 'Xabarlar'
        db_table = 'xabar'

    def __str__(self):
        return self.name
