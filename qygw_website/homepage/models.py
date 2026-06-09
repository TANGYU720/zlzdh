from django.db import models

class Kehu(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    phone = models.CharField(max_length=20, verbose_name='电话')
    email = models.EmailField(max_length=100, verbose_name='邮箱')
    company = models.CharField(max_length=200, verbose_name='公司名称')
    inquiry_type = models.CharField(max_length=50, verbose_name='咨询类型')
    message = models.TextField(verbose_name='留言内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='提交时间')

    class Meta:
        db_table = 'kehu'
        verbose_name = '客户信息'
        verbose_name_plural = '客户信息'

    def __str__(self):
        return f'{self.name} - {self.company}'
