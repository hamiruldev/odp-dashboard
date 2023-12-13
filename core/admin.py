
from django.contrib import admin

class CustomAdminSite(admin.AdminSite):
    
    site_header = 'One Dream Property | Listing System'
    site_title = 'Administration'
    site_url = 'http://onedreamproperty.com.my/'
    index_title = 'Dashboard'
    
    
    

    
    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        
        # permission = self
        
        

        # print("permission", permission)
        print("super().get_app_list(request)", super().get_app_list(request))
        # Define the custom order of app labels
        custom_order = ['blog', 'branchs', 'inventory', 'profiles', 'teams', 'users']

        # Sort the app list based on the custom order
        app_list.sort(key=lambda x: custom_order.index(x['app_label']))
        
        print("admin.AdminSite.each_context--->", app_list)
        

        return app_list

 
admin_site = CustomAdminSite(name="myadmin")
