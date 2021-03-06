# Generated by Django 3.1.2 on 2021-11-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('image', models.ImageField(blank=True, upload_to='products_images')),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField(default=0)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
    ]
