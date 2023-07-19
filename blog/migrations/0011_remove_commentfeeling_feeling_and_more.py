# Generated by Django 4.2.3 on 2023-07-19 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_tag_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentfeeling',
            name='feeling',
        ),
        migrations.RemoveField(
            model_name='postfeeling',
            name='feeling',
        ),
        migrations.AddField(
            model_name='commentfeeling',
            name='like',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='postfeeling',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]