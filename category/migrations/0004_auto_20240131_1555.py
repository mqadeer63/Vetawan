# Generated by Django 3.1 on 2024-01-31 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='subcat_image',
            field=models.ImageField(blank=True, upload_to='images/subcategories'),
        ),
    ]