# Generated by Django 3.2.18 on 2024-05-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='products/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('Tops', 'Tops'), ('Bottoms', 'Bottoms'), ('Outwear', 'Outwear'), ('Accessories', 'Accessories'), ('Suits', 'Suits'), ('Footwear', 'Footwear'), ('Undergarments', 'Undergarments')], max_length=100)),
            ],
        ),
    ]
