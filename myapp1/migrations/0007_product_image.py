# Generated by Django 5.1.1 on 2024-10-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0006_remove_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='product_images/default_image.jpg', upload_to='product_images/'),
        ),
    ]
