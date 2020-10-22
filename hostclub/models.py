import uuid
import pathlib
from django.db import models


class TaxRate(models.TextChoices):
    CURRENT = 10, '10%'
    REDUCED = 8, '8%（軽減税率）'
    TAX_EXEMPT = 0, '0%(非課税)'


class Host(models.Model):
    class Meta:
        verbose_name_plural = 'ホスト'

    name = models.CharField(verbose_name='ホスト名', max_length=100)

    def __repr__(self):
        return '<Host: %s %s>' % (self.id, self.name)


def get_image_path(self, filename):
    prefix = 'customer/'
    name = str(uuid.uuid4()).replace('-', '')
    ext = pathlib.Path(filename).suffix
    return prefix + name + ext

class Customer(models.Model):
    class Meta:
        verbose_name_plural = 'お客様'

    name = models.CharField(verbose_name='お客様名', max_length=100)
    # @ref https://qiita.com/okoppe8/items/86776b8df566a4513e96
    # add validators if required  [FileExtensionValidator(['jpg', 'png'...])]
    image = models.ImageField(verbose_name='画像', upload_to=get_image_path)
    memo = models.TextField(verbose_name='メモ', blank=True, default='')


    def __repr__(self):
        return '<Customer: %s %s>' % (self.id, self.name)

class Seat(models.Model):
    class Meta:
        verbose_name_plural = 'シート'

    name = models.CharField(verbose_name='シート名', max_length=100)

    def __repr__(self):
        return '<Seat: %s %s>' % (self.id, self.name)


class Menu(models.Model):
    class Meta:
        verbose_name_plural = 'メニュー'

    name = models.CharField(verbose_name='商品名', max_length=100)
    price = models.BigIntegerField(verbose_name='価格')
    tax_rate = models.FloatField(choices=TaxRate.choices, default=TaxRate.CURRENT)

    def __repr__(self):
        return '<Menu: %s %s yen, %s %>' % (self.name, self.price, self.tax_rate)

class Reserve(models.Model):
    class Meta:
        verbose_name_plural = '予約'

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='reserves')
    seat = models.ForeignKey(Seat, on_delete=models.PROTECT, related_name='reserves')
    host = models.ForeignKey(Host, on_delete=models.PROTECT, related_name='reserves')
    entered_at = models.DateTimeField(verbose_name='入店日時')
    left_at = models.DateTimeField(verbose_name='退店日時')

    def __repr__(self):
        return '<Reserve: cus:%s seat:%s host:%s>' % (self.customer, self.seat, self.host)
