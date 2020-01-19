from django.db import models
from translations.models import Translatable
from optimized_image.fields import OptimizedImageField
from django.utils.translation import gettext_lazy as _


class Logo(models.Model):
    logo = OptimizedImageField(
        upload_to='logo',
        default='defaults/logo.png',
        verbose_name=_('Logo'))
    favicon = OptimizedImageField(
        upload_to='logo',
        default='default_imgs/logo.png',
        verbose_name=_('Favicon 16x16'))

    class Meta:
        verbose_name = _('Logo')
        verbose_name_plural = _('Logo')

    def __str__(self):
        return 'Logo & Favicon'


# Create your models here.
class Home(Translatable):
    header = models.ImageField(
        upload_to='home',
        default='defaults/placeholder.png',
        verbose_name=_('Section-1 Background Image'))
    header_title_line1 = models.CharField(
        max_length=255,
        verbose_name=_('Section-1 Text Line-1'))
    header_title_line2 = models.CharField(
        max_length=255,
        verbose_name=_('Section-1 Text Line-2'))
    section2 = OptimizedImageField(
        upload_to='home',
        null=True,
        blank=True,
        verbose_name=_('Section-2 Background Image'))
    section2_story = OptimizedImageField(
        upload_to='home',
        null=True,
        blank=True,
        verbose_name=_('Section-2 Center-Box Background Image'))
    section2_image_left = OptimizedImageField(
        upload_to='home',
        null=True,
        blank=True,
        verbose_name=_('Section-2 Left Image'))
    section2_image_right = OptimizedImageField(
        upload_to='home',
        null=True,
        blank=True,
        verbose_name=_('Section-2 Right Image'))
    section2_title_line1 = models.CharField(
        max_length=255,
        verbose_name=_('Section-2 Text Line-1'))
    section2_title_line2 = models.CharField(
        max_length=255,
        verbose_name=_('Section-2 Text Line-2'))
    section3 = OptimizedImageField(
        upload_to='home',
        default='defaults/placeholder.png',
        verbose_name=_('Section-3 Background Image'))
    section3_msg_line1 = models.CharField(
        max_length=255,
        verbose_name=_('Section-3 Text Line-1'))
    section3_msg_line2 = models.CharField(
        max_length=255,
        verbose_name=_('Section-3 Text Line-2'))
    section4_img1 = OptimizedImageField(
        upload_to='home',
        default='defaults/placeholder.png',
        verbose_name=_('Section-4 Box-1 Image'))
    section4_img2 = OptimizedImageField(
        upload_to='home',
        default='defaults/placeholder.png',
        verbose_name=_('Section-4 Box-2 Image'))
    section4_img3 = OptimizedImageField(
        upload_to='home',
        default='defaults/placeholder.png',
        verbose_name=_('Section-4 Box-3 Image'))
    section4_img4 = OptimizedImageField(
        upload_to='home',
        default='defaults/placeholder.png',
        verbose_name=_('Section-4 Box-4 Image'))
    section5 = OptimizedImageField(
        upload_to='home',
        default='defaults/placeholder.png',
        verbose_name=_('Section-5 Background Image'))
    section5_msg_line1 = models.CharField(
        max_length=255,
        verbose_name=_('Section-5 Text Line-1'))
    section5_msg_line2 = models.CharField(
        max_length=255,
        verbose_name=_('Section-5 Text Line-2'))
    section6_img1 = OptimizedImageField(
        upload_to='home',
        default='defaults/placeholder.png',
        verbose_name=_('Section-6 Image-1'))
    section6_img1_text_line1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Section-6 Image-1 Text Line 1'))
    section6_img1_text_line2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Section-6 Image-1 Text Line 2'))
    section6_img2 = OptimizedImageField(
        upload_to='home',
        default='defaults/placeholder.png',
        verbose_name=_('Section-6 Image-2'))
    section6_img2_text_line1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Section-6 Image-2 Text Line 1'))
    section6_img2_text_line2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Section-6 Image-2 Text Line 2'))
    section6_img3 = OptimizedImageField(
        upload_to='home',
        default='defaults/placeholder.png',
        verbose_name=_('Section-6 Image-3'))
    section6_img3_text_line1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Section-6 Image-3 Text Line 1'))
    section6_img3_text_line2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Section-6 Image-3 Text Line 3'))

    def __str__(self):
        return 'Home'

    class Meta:
        verbose_name = _('Home Page')
        verbose_name_plural = _('Home Page')


class MenuPage(Translatable):
    sec1_img = OptimizedImageField(
        upload_to='about',
        blank=True,
        null=True,
        verbose_name=_('Section-1 Image'))
    sec1_l1 = models.CharField(
        max_length=255,
        verbose_name=_('Section-1 Text Line-1'))
    sec1_l2 = models.CharField(
        max_length=255,
        verbose_name=_('Section-1 Text Line-2'))

    class Meta:
        verbose_name = _('Menu Page')
        verbose_name_plural = _('Menu Page')


class Ingredient(Translatable):
    ingredient_name = models.CharField(
        max_length=64,
        verbose_name=_('Ingredients'),
        help_text='eg. Chicken, Tomato, Egg')

    def __str__(self):
        return self.ingredient_name

    class Meta:
        verbose_name = _('Ingredients')
        verbose_name_plural = _('Ingredients')


class Menu(Translatable):
    food_name = models.CharField(
        max_length=64,
        verbose_name=_('Food Name'),
        help_text='eg. Adana Kebab. FIELD/ALAN: food_name')
    image = OptimizedImageField(
        upload_to='menu',
        default='defaults/noImage.jpg',
        blank=True,
        null=True,
        verbose_name=_('Food Picture'))
    ingredients = models.ManyToManyField(
        Ingredient,
        blank=True,
        related_name='ingredients',
        verbose_name=_('Ingredients In This Dish'))
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Price'))
    feature = models.BooleanField(
        default=False,
        verbose_name=_("Feature On Home Page"))

    def __str__(self):
        return self.food_name

    class Meta:
        verbose_name = _('Menu')
        verbose_name_plural = _('Menu')


class Category(Translatable):
    category_name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name=_('Category Name'),
        help_text=_('eg. Lunch, Dessert, Drinks. FIELD/ALAN: category_name'))
    phrase_above_name = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        verbose_name=_('Phrase Above Category Name'),
        help_text=_('eg. For Start, Tasty, More Concrete, Healthy, Refreshing etc. FIELD/ALAN: phrase_above_name'))
    menu_items = models.ManyToManyField('Menu', related_name='category')

    DISPLAY_ORDER = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    )
    display_order = models.IntegerField(choices=DISPLAY_ORDER, unique=True)

    def __str__(self):
        return f"{self.display_order}. {self.category_name}, {self.phrase_above_name}"

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class ContactPage(Translatable):
    sec1_img = OptimizedImageField(
        upload_to='contact',
        blank=True,
        null=True,
        verbose_name=_('Section-1 Background Image'))
    sec1_l1 = models.CharField(
        max_length=255,
        verbose_name=_('Section-1 Text Line-1'))
    sec1_l2 = models.CharField(
        max_length=255,
        verbose_name=_('Section-1 Text Line-2'))
    sec3_img = OptimizedImageField(
        upload_to='about',
        blank=True,
        null=True,
        verbose_name=_('Section-3 Background Image'))
    sec3_l1 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Section-3 Text Line-1'))
    sec3_l2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Section-3 Text Line-2'))

    def __str__(self):
        return 'Contact Page'

    class Meta:
        verbose_name = _('Contact Page')
        verbose_name_plural = _('Contact Page')


class Contact(models.Model):
    phone = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name=_('Phone Number'),
        help_text=_('+90 (000) 000 00 00'))
    email = models.EmailField(
        max_length=128,
        null=True,
        blank=True,
        verbose_name=_('Email'),
        help_text=_('example@email.com'))

    def __str__(self):
        return f'{self.phone}, {self.email}'

    class Meta:
        verbose_name = _('Contact Info')
        verbose_name_plural = _('Contact Info')


class Address(models.Model):
    company_name = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        verbose_name=_("Company Name"))
    street = models.CharField(
        max_length=64,
        verbose_name=_("Street"))
    city = models.CharField(
        max_length=64,
        verbose_name=_("City"))
    state = models.CharField(
        max_length=25,
        verbose_name=_("State"))
    postal = models.CharField(
        max_length=6,
        verbose_name=_("Postal Code"))
    country = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        verbose_name=_("Country"))
    address_map_link = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Google Maps link for the address'))

    def __str__(self):
        return f'{self.company_name}, {self.street}, {self.city} {self.postal}, {self.state}, {self.country}'

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Address')


class OpenHours(models.Model):
    WEEKDAY_CHOICE = (
        ('1', _('Monday')),
        ('2', _('Tuesday')),
        ('3', _('Wednesday')),
        ('4', _('Thursday')),
        ('5', _('Friday')),
        ('6', _('Saturday')),
        ('7', _('Sunday')),
    )

    weekday_from = models.CharField(
        choices=WEEKDAY_CHOICE,
        null=True,
        blank=True,
        max_length=12,
        verbose_name=_('From Day'))
    weekday_to = models.CharField(
        choices=WEEKDAY_CHOICE,
        null=True,
        blank=True,
        max_length=12,
        verbose_name=_('To Day'))
    open_hr_from = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name=_('Open Hours From'))
    open_hr_to = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name=_('Open Hours To'))

    def __str__(self):
        return f'Open {self.get_weekday_from_display()} - {self.get_weekday_to_display()} from {self.open_hr_from} - {self.open_hr_to}'

    class Meta:
        verbose_name = _('Open Hours')
        verbose_name_plural = _('Open Hours')


class About(Translatable):
    sec1_img = OptimizedImageField(
        upload_to='about',
        blank=True,
        null=True,
        verbose_name=_('Section-1 Image'))
    sec1_l1 = models.CharField(
        max_length=255,
        verbose_name=_('Section-1 Text Line-1'))
    sec1_l2 = models.CharField(
        max_length=255,
        verbose_name=_('Section-1 Text Line-2'))
    sec2_img = OptimizedImageField(
        upload_to='about',
        blank=True,
        null=True,
        verbose_name=_('Section-2 Image'))
    about_l1 = models.CharField(
        max_length=255,
        default='About',
        verbose_name=_('About Title'))
    about_l2 = models.CharField(
        max_length=255,
        verbose_name=_('About Subtitle'))
    about = models.TextField()
    sec3_img = OptimizedImageField(
        upload_to='about',
        blank=True,
        null=True,
        verbose_name=_('Section-3 Image'))
    sec3_l1 = models.CharField(
        max_length=255,
        verbose_name=_('Section-3 Title'))
    sec3_l2 = models.CharField(
        max_length=255,
        verbose_name=_('Section-3 Subtitle'))
    sec3_paragraph = models.TextField()
    sec4_img = OptimizedImageField(
        upload_to='about',
        blank=True,
        null=True,
        verbose_name=_('Section-4 Image'))
    sec4_l1 = models.CharField(
        max_length=255,
        verbose_name=_('Section-4 Text Line-1'))
    sec4_l2 = models.CharField(
        max_length=255,
        verbose_name=_('Section-4 Text Line-2'))

    def __str__(self):
        return 'Our Story'

    class Meta:
        verbose_name = _('About Page')
        verbose_name_plural = _('About Page')


class SocialMedia(models.Model):
    facebook = models.TextField(null=True, blank=True)
    instagram = models.TextField(null=True, blank=True)
    tripadvisor = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'Facebook, Instagram, TripAdvisor'

    class Meta:
        verbose_name = _('Social Media Link')
        verbose_name_plural = _('Social Media Links')
