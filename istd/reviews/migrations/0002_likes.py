# Generated by Django 2.2.2 on 2019-06-08 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20190608_1928'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0003_auto_20190608_1746'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_of_target', models.IntegerField(db_index=True, verbose_name='id таргетированной модели')),
                ('isCompany', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='companies.Company')),
                ('isCourse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='courses.Course')),
                ('isLesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='courses.Lesson')),
                ('isPackage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='courses.Package')),
                ('isUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Лайк',
                'verbose_name_plural': 'Лайки',
            },
        ),
    ]