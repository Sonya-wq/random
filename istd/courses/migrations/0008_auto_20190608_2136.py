# Generated by Django 2.2.2 on 2019-06-08 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20190608_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='courses.CourseCategory'),
            preserve_default=False,
        ),
    ]