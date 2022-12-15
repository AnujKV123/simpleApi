# Generated by Django 3.1.2 on 2022-12-15 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productMainModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('Description', models.CharField(blank=True, max_length=500, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('unique_code', models.TextField(unique=True)),
                ('Size', models.IntegerField(choices=[(10, '1'), (20, '2'), (30, '3')])),
                ('Quality', models.CharField(choices=[('high', 'h'), ('low', 'l'), ('medium', 'm')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='productImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, null=True, upload_to='')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.productmainmodel')),
            ],
        ),
        migrations.CreateModel(
            name='productColourModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Colour', models.CharField(choices=[('red', 'r'), ('blue', 'b'), ('green', 'g'), ('black', 'b')], max_length=50)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.productmainmodel')),
            ],
        ),
    ]