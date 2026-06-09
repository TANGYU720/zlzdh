from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.hashers import make_password
from django import forms
from .models import Kehu

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("两次密码输入不一致")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

class CustomGroupAdmin(GroupAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('permissions',)

class CustomAdminSite(AdminSite):
    site_header = '企业官网管理后台'
    site_title = '智联自动化'
    index_title = '管理首页'
    
    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        
        for app in app_list:
            if app['app_label'] == 'auth':
                app['name'] = '管理员设置'
                
                for model in app['models']:
                    if model['object_name'] == 'User':
                        model['name'] = '管理员账号'
                    elif model['object_name'] == 'Group':
                        model['name'] = '权限组'
            elif app['app_label'] == 'homepage':
                app['name'] = '咨询客户'
        
        return app_list

admin_site = CustomAdminSite(name='custom_admin')

admin_site.register(User, CustomUserAdmin)
admin_site.register(Group, CustomGroupAdmin)