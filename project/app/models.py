from django.db import models

from django.contrib.auth.hashers import make_password
from django.utils import timezone
import hashlib

# Create your models here.

class User(models.Model):
    def __str__(self):
        return str(self.name)

    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=255, blank=True, null=True)
    is_studio = models.BooleanField(default=0)

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'user'

    def save(self, *args, **kwargs):
        self.password = make_password(self.password) #パスワード暗号化
        super().save(*args, **kwargs)


class LoginToken(models.Model):
    def __str__(self):
        # メールアドレスとアクセス日時、トークンが見えるようにする
        dt = timezone.localtime(self.access_datetime).strftime("%Y/%m/%d %H:%M:%S")
        return self.user.email + '(' + dt + ') - ' + self.token

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=40) #トークン
    access_datetime = models.DateTimeField() #アクセス日時

    class Meta:
        db_table = 'tokens'
        verbose_name_plural = 'token'

    @staticmethod
    def create(user: User):
        # ユーザの既存のトークンを取得
        if LoginToken.objects.filter(user=user).exists():
            # トークンが既に存在している場合は削除する
            LoginToken.objects.get(user=user).delete()

        # トークン生成（メールアドレス + パスワード + システム日付のハッシュ値とする）
        dt = timezone.now()
        str = user.email + user.password + dt.strftime('%Y%m%d%H%M%S%f')
        hash = hashlib.sha1(str.encode('utf-8')).hexdigest()    # utf-8でエンコードしないとエラーになる

        # トークンをデータベースに追加
        token = LoginToken.objects.create(
            user = user,
            token = hash,
            access_datetime = dt)

        return token


class Group(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = 'groups'
        verbose_name_plural = 'group'

class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = 'group_users'
        verbose_name_plural = 'group_user'

class Studio(models.Model):
    def __str__(self):
        return str(self.name)

    name = models.CharField(max_length=255)
    prefecture = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    gps = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = 'studios'
        verbose_name_plural = 'studio'

class Room(models.Model):
    def __str__(self):
        return str(self.name)

    name = models.CharField(max_length=255)
    wide = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    studio = models.ForeignKey(Studio, on_delete=models.PROTECT)

    class Meta:
        db_table = 'rooms'
        verbose_name_plural = 'room'

class Current(models.Model):
    member_no = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    studio = models.ForeignKey(Studio, on_delete=models.PROTECT)

    class Meta:
        db_table = 'currents'
        verbose_name_plural = 'current'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        db_table = 'bookings'
        verbose_name_plural = 'booking'

class EquipmentKind(models.Model):
    def __str__(self):
        return str(self.name)

    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'equipment_kinds'
        verbose_name_plural = 'equipment_kind'

class Equipment(models.Model):
    def __str__(self):
        return str(self.name)

    name = models.CharField(max_length=255)
    kind = models.ForeignKey(EquipmentKind, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)

    class Meta:
        db_table = 'equipments'
        verbose_name_plural = 'equipment'
