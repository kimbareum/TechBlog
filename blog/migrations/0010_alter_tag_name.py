# Generated by Django 4.2.3 on 2023-07-19 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, choices=[('Life', 'Life'), ('Style', 'Style'), ('Tech', 'Tech'), ('Sport', 'Sport'), ('Photo', 'Photo'), ('Develop', 'Develop'), ('Music', 'Music')], max_length=10, null=True),
        ),
    ]
