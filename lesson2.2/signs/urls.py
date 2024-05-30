from django.urls import path
from .views import ( SignsRoadDetailDeleteUpdate,
    # CreateListSignsView,
    #CreateSignsRoadAPIView,
    #ListCategoryAPIView, ListRoadSingAPIView,
                    # SingsRoadDelete, SingsRoadDetail,
                    # SingsRoadPut, SingsRoadPatch
                    )

urlpatterns = [
    # path('create/', CreateListSignsView.as_view(), name='create'),
    # path('create/', CreateSignsRoadAPIView.as_view(), name='create'),
    # path('category-list/', ListCategoryAPIView.as_view(), name='category-list'),
    # path('signs-road-list/', ListRoadSingAPIView.as_view(), name='signs-road-list'),
    path('signs-road/<int:pk>', SignsRoadDetailDeleteUpdate.as_view(), name='signs-road'),
    # path('sings-road-detail/<int:pk>', SingsRoadDetail.as_view(), name='sings-road-detail'),
    # path('sings-road-delete/<int:pk>', SingsRoadDelete.as_view(), name='sings-road-delete'),
    # path('sings-road-put/<int:pk>', SingsRoadPut.as_view(), name='sings-road-put'),
    # path('sings-road-patch/<int:pk>', SingsRoadPatch.as_view(), name='sings-road-patch'),
]