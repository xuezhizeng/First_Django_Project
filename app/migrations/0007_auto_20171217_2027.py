# Generated by Django 2.0 on 2017-12-17 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20171217_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.StoreHouse', verbose_name='所属仓库名称:'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='job',
            field=models.CharField(choices=[('记帐员', '记帐员'), ('仓库主管', '仓库主管'), ('普通员工', '普通员工'), ('统计员', '统计员'), ('保管员', '保管员')], default='普通员工', max_length=10, verbose_name='职位:'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='sex',
            field=models.CharField(choices=[('female', '女'), ('male', '男')], default='女', max_length=10, verbose_name='性别:'),
        ),
    ]
