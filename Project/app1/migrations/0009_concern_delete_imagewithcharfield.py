# Generated by Django 4.2.6 on 2023-10-08 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_imagewithcharfield_delete_concern'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('context', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='ImageWithCharField',
        ),
    ]
