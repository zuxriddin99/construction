# Generated by Django 3.1.7 on 2021-03-06 04:34

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_bizningishlarimiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Korxona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Korxona nomi')),
                ('main_image', models.ImageField(upload_to='korxona-haqida', verbose_name='Surat')),
                ('little_image', models.ImageField(upload_to='korxona-haqida', verbose_name='Surat')),
                ('short_info', ckeditor_uploader.fields.RichTextUploadingField(verbose_name="Qisqacha ma'lumot")),
                ('full_info', ckeditor_uploader.fields.RichTextUploadingField(verbose_name="To'liq ma'lumot")),
                ('quote_index_page', models.TextField(verbose_name='Iqtibos')),
                ('quote_name', models.CharField(max_length=250, verbose_name='Iqtibos vakili')),
                ('quote_job', models.CharField(max_length=250, verbose_name='Iqtibos vakilining kasbi')),
                ('quote_image', models.ImageField(upload_to='bizning-ishlar', verbose_name='Surat')),
            ],
            options={
                'verbose_name': 'Korxona',
                'verbose_name_plural': 'Korxona',
                'db_table': 'korxona',
            },
        ),
        migrations.AlterModelOptions(
            name='bizningishlarimiz',
            options={'verbose_name': 'Bizning Ish', 'verbose_name_plural': 'Bizning Ishlarimiz'},
        ),
    ]