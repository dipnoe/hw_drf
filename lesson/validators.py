from rest_framework.serializers import ValidationError


class VideoLinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)

        if not str(tmp_val).startswith('https://www.youtube.com/'):
            raise ValidationError('Недопустимый источник ссылки')
