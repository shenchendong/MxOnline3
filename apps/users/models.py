from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class UserProfile(AbstractBaseUser):

    GENDER_CHOICES = (
        ("male",u"男"),
        ("female",u"女"),
    )

    # 昵称
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    # 生日，可以为空
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    # 性别 只能男或女，默认女
    gender = models.CharField(
        max_length=5,
        verbose_name=u"性别",
        choices=GENDER_CHOICES,
        default="female")
    # 地址
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    # 电话
    mobile = models.CharField(max_length=11, null=True, blank=True)
    # 头像 默认使用default.png
    image = models.ImageField(
        upload_to="image/%Y/%m",
        default=u"image/default.png",
        max_length=100
    )

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.username







