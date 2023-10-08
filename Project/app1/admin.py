from django.contrib import admin
from app1.models import Authenticator,Contact,ImageWithCharField
# Register your models here.

admin.site.register(Authenticator)
admin.site.register(Contact)
admin.site.register(ImageWithCharField)


