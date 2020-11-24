from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from posts.models import Poss
from django.contrib.auth.models import User

# Register your models here.
@admin.register(Poss)
class PostAdmin(admin.ModelAdmin):
	list_display = ('pk','user','profile','title','photo')
	list_display_links = ('pk','user')
	list_editable = ('profile','title','photo')
	search_fields = (
		'user__email',
		'user__username'
		'user__first_name',
		'user_last_name',
		'phone_number')
	list_filter = (
		'created',
		'modified',
		'user__is_active',
		'user__is_staff'
		)
	fieldsets = (
		('Poss',{
			'fields': (('user','photo'),),
			}),
		('Extra info',{
			'fields': (
				('profile','title'),)
			}),
		('Metadata',{
			'fields':(('created','modified'))
			})
		)

	readonly_fields = ('created','modified')

class ProfileInLine(admin.StackedInline):
	model = Poss
	can_delete = False
	verbose_name_pural = 'Poss'

class UserAdmin(BaseUserAdmin):
	inlines = (ProfileInLine,)
	list_display =(
		'username',
		'email',
		'first_name',
		'last_name',
		'is_active',
		'is_staff')

admin.site.unregister(User)
admin.site.register(User,UserAdmin)