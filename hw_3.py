import re

def normalize_phone(phone_number):
    phone_number = "123123123"

    cleaned_number = re.sub(r'[^0-9+]', '', phone_number)
    if not cleaned_number.startswith('+'):
        if cleaned_number.startswith('380'):
            cleaned_number = '+' + cleaned_number
        else:
            cleaned_number = "+38" + cleaned_number
            
    return cleaned_number