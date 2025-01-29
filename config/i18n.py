from aiogram.utils.i18n import I18n, FSMI18nMiddleware

I18N_DOMAIN = 'messages'
I18N_LOCALES_DIR = "locales"
I18N_DEFAULT_LOCALE = 'en'


i18n = I18n(
    path=I18N_LOCALES_DIR,
    default_locale=I18N_DEFAULT_LOCALE,
    domain=I18N_DOMAIN
)


i18n_middleware = FSMI18nMiddleware(i18n=i18n)