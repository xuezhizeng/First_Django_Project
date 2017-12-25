# Generated by Django 2.0 on 2017-12-19 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20171219_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_sup',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Supplier', verbose_name='供应商名称'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_mens',
            field=models.CharField(choices=[('千克', '千克'), ('袋', '袋'), ('台', '台'), ('斤', '斤'), ('箱', '箱'), ('颗', '颗')], default='请输入计量单位', max_length=20, verbose_name='计量单位:'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='job',
            field=models.CharField(choices=[('保管员', '保管员'), ('记帐员', '记帐员'), ('普通员工', '普通员工'), ('仓库主管', '仓库主管'), ('统计员', '统计员')], default='普通员工', max_length=10, verbose_name='职位:'),
        ),
    ]
