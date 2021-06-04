from django.db import models
from django.forms import ModelForm


class JewelryChain(models.Model):
    name = models.CharField(max_length=100)
    pictures = models.ImageField(blank=True, null=True,
                                 upload_to="pictures/%Y/%m/$D/")
    desc = models.CharField(max_length=256)
    product = models.DecimalField(max_digits=6, decimal_places=0, null=True)
    good_type = models.TextChoices('type', 'Figaro Cuban Tri-color_Valentino')
    sTypes = models.CharField(blank=True, choices=good_type.choices, max_length=20)
    description = models.TextField()


class JewelryQuote(models.Model):
    name = models.CharField(max_length=64)
    phone = models.DecimalField(max_digits=10, decimal_places=0)
    email = models.CharField(max_length=64)
    type_choices = [
        ('FI', 'Figaro'),
        ('CU', 'Cuban'),
        ('TV', 'Tri-Color Valentino'),

    ]
    color_choices = [
        ('GD', 'Gold'),
        ('WG', 'White GOLD'),
        ('TC', 'Tri-Color Valentino'),

    ]
    length_choices = [
        ('14', '14'),
        ('16', '16'),
        ('18', '18'),
        ('20', '20'),
        ('22', '22'),
        ('24', '24'),
        ('26', '26'),
        ('28', '28'),
    ]
    Style = models.CharField(max_length=2, choices=type_choices)
    Color = models.CharField(max_length=2, choices=color_choices)
    Length = models.CharField(max_length=2, choices=length_choices)
    amount = models.DecimalField(max_digits=6, decimal_places=0)
    custom_order = models.TextField()


class JewelryQuoteForm(ModelForm):
    class Meta:
        model = JewelryQuote
        fields = ['name', 'phone', 'email', 'Style', 'Color', 'Length', 'amount',
                  'custom_order', ]
