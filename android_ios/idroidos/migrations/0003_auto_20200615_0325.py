# Generated by Django 3.0.3 on 2020-06-15 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idroidos', '0002_auto_20200613_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comparisoninfo',
            name='battery',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comparisoninfo',
            name='camera',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comparisoninfo',
            name='conclusion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comparisoninfo',
            name='design',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comparisoninfo',
            name='display',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comparisoninfo',
            name='extras',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comparisoninfo',
            name='intro',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comparisoninfo',
            name='overview',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comparisoninfo',
            name='performance',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comparisoninfo',
            name='software',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comparisoninfo',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='conclusion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='heading',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='para1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='para2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='para3',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='newscomment',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='smartphonecomment',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='smartphonesinfo',
            name='battery',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='smartphonesinfo',
            name='camera',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='smartphonesinfo',
            name='conclusion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='smartphonesinfo',
            name='design',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='smartphonesinfo',
            name='display',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='smartphonesinfo',
            name='extras',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='smartphonesinfo',
            name='intro',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='smartphonesinfo',
            name='overview',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='smartphonesinfo',
            name='performance',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='smartphonesinfo',
            name='smartphone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='smartphonesinfo',
            name='software',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='smartphonesinfo',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
