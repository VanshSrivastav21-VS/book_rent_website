# Generated by Django 5.1 on 2024-08-14 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_file_book_file_name_alter_book_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='file',
        ),
        migrations.RemoveField(
            model_name='book',
            name='file_name',
        ),
    ]
