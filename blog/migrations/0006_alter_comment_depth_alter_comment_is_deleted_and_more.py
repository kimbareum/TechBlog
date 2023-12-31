# Generated by Django 4.2.3 on 2023-07-18 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_options_remove_comment_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='depth',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_fixed',
            field=models.BooleanField(default=False),
        ),
    ]
