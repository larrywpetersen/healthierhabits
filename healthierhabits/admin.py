from django.contrib import admin

from .models import Groups, Rewards, Customers, Orders

admin.site.register( Groups)
admin.site.register( Rewards)
admin.site.register( Customers)
admin.site.register( Orders)

