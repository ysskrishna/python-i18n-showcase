import i18n
from datetime import datetime


i18n.load_path.append('translations')
i18n.set('filename_format', '{locale}.{format}')
i18n.set('skip_locale_root_data', True) 


def test_translations(locale):
    i18n.set('locale', locale)
    print(f"\n=== Testing {locale} translations ===")
    print(i18n.t('GREETING'))
    print(i18n.t('MESSAGES.WELCOME'))
    print(i18n.t('MESSAGES.FAREWELL'))
    
    # Test plurals
    print(i18n.t('MESSAGES.ITEMS_COUNT', count=0))
    print(i18n.t('MESSAGES.ITEMS_COUNT', count=1))
    print(i18n.t('MESSAGES.ITEMS_COUNT', count=5))
    
    # Test interpolations
    print(i18n.t('MESSAGES.WELCOME_USER', name='John'))
    print(i18n.t('MESSAGES.FILE_INFO', filename='document.txt', date=datetime.now().strftime('%Y-%m-%d')))

# Test in different languages
test_translations('en')
test_translations('es')
test_translations('zh')