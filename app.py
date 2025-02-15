import i18n
from datetime import datetime
import locale
from babel.dates import format_datetime
from babel.numbers import format_number, format_currency

i18n.load_path.append('translations')
i18n.set('filename_format', '{locale}.{format}')
i18n.set('skip_locale_root_data', True)
i18n.set('fallback', 'en')  # Set English as fallback language

def format_date_for_locale(date, locale_str):
    """Format date according to locale conventions"""
    try:
        return format_datetime(date, locale=locale_str)
    except:
        return date.strftime('%Y-%m-%d')  # Fallback format

def format_number_for_locale(number, locale_str):
    """Format number according to locale conventions"""
    try:
        return format_number(number, locale=locale_str)
    except:
        return str(number)  # Fallback format

def test_translations(locale):
    i18n.set('locale', locale)
    print(f"\n=== Testing {locale} translations ===")
    
    # Basic translations
    print("\n-- Basic Translations --")
    print(i18n.t('GREETING'))
    print(i18n.t('MESSAGES.WELCOME'))
    print(i18n.t('MESSAGES.FAREWELL'))
    
    # Pluralization
    print("\n-- Pluralization --")
    print(i18n.t('MESSAGES.ITEMS_COUNT', count=0))
    print(i18n.t('MESSAGES.ITEMS_COUNT', count=1))
    print(i18n.t('MESSAGES.ITEMS_COUNT', count=5))
    
    # Interpolation with variables
    print("\n-- Variable Interpolation --")
    print(i18n.t('MESSAGES.WELCOME_USER', name='John'))
    
    # Date formatting
    current_date = datetime.now()
    formatted_date = format_date_for_locale(current_date, locale)
    print("\n-- Date Formatting --")
    print(i18n.t('MESSAGES.FILE_INFO', filename='document.txt', date=formatted_date))
    
    # Number formatting
    print("\n-- Number Formatting --")
    number = 1234567.89
    formatted_number = format_number_for_locale(number, locale)
    print(i18n.t('MESSAGES.NUMBER_DISPLAY', number=formatted_number))
    
    # Currency formatting
    print("\n-- Currency Formatting --")
    amount = 1234.56
    try:
        formatted_amount = format_currency(amount, 'USD', locale=locale)
        print(i18n.t('MESSAGES.PRICE_DISPLAY', price=formatted_amount))
    except:
        print(f"Currency formatting not supported for locale: {locale}")
    
    # Error handling for missing translations
    print("\n-- Error Handling --")
    print(i18n.t('MESSAGES.NON_EXISTENT', default='Translation not found'))

# Test in different languages
test_translations('en')
test_translations('es')
test_translations('zh')