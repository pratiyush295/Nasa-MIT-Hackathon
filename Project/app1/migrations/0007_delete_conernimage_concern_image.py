# Generated by Django 4.2.6 on 2023-10-08 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_concern_context'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ConernImage',
        ),
        migrations.AddField(
            model_name='concern',
            name='image',
            field=models.ImageField(default='img', upload_to='images/'),
            preserve_default=False,
        ),
    ]