# Generated by Django 5.0.3 on 2024-03-18 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0004_comments_subscribers_delete_forms_posts_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='services',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
