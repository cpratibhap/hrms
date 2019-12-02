from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def name_validators(value):
    if not value.isalpha():
        raise ValidationError("Not a valid name")
    else:
        return value


def email_validators(value):
    if not '@indexial.com' in value:
        raise ValidationError("Not a valid email ID")
    else:
        return value


#mobile_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Invalid Mobile Number')
mobile_regex = RegexValidator(regex='(0|91|\+91)[6-9]\d{9}|([6-9]\d{9})', message='Invalid Mobile Number')

def validate_image_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')



