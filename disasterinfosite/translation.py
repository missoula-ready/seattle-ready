from modeltranslation.translator import register, translator, TranslationOptions
from .models import SiteSettings

@register(SiteSettings)
class SiteSettingsTranslationOptions(TranslationOptions):
    fields = ('about_text', 'site_title', 'site_description', 'intro_text', 'who_made_this')
