from django.urls import path
from .views import category_signs_list, signs_road_list, delete, create, update_put, update_patch


urlpatterns = [
        path('category-list/', category_signs_list, name='category-list'),
        path('signs-road-list/', signs_road_list, name='signs-road-list'),
        path('signs-delete/<int:pk>', delete, name='signs-delete'),
        path('signs-create/', create, name='signs-create'),
        path('signs-update-put/<int:pk>', update_put, name='signs-update-put'),
        path('signs-update-patch/<int:pk>', update_patch, name='signs-update-patch'),
]