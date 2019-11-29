from django.db import models

from wagtail.core.models import Page

# Imports required for tools
from modelcluster.fields import ParentalKey
from wagtail.core.models import Orderable
from wagtail.admin.edit_handlers import InlinePanel, FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


from tools.models import Dreamer, Seo


class HomePage(Page, Dreamer, Seo):
    parent_page_types = ['wagtailcore.page', 'home.HomePage']
    subpage_types = ['tools.Index', 'home.HomePage']


    content_panels = Page.content_panels + Dreamer.panels + [
        InlinePanel('carousel_items', label="Carousel images"),
    ] 
     
    promote_panels = Page.promote_panels + Seo.panels


    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


class Carousel(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='carousel_items')
    title = models.CharField(blank=True, max_length=250)
    caption = models.CharField(blank=True, max_length=250)
    image = models.ForeignKey('wagtailimages.Image',  null=True, blank=True, on_delete=models.CASCADE, related_name='+')

    panels = [
        FieldPanel('title'),
        FieldPanel('caption'),
        ImageChooserPanel('image'),
    ]