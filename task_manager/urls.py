from django.urls import path
from django.urls import path
from .views import (
    ClientListCreateView,
    ClientDetailView,
    ClientDeleteView,
    ProjectCreateView,
)


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import ClientListCreateView, ClientRetrieveUpdateDestroyView

urlpatterns = [
    path("clients/", ClientListCreateView.as_view(), name="client-list-create"),
    path(
        "clients/<int:pk>",
        ClientRetrieveUpdateDestroyView.as_view(),
        name="client-detail",
    ),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="client-detail"),
    path(
        "clients/<int:pk>/projects/", ProjectCreateView.as_view(), name="project-create"
    ),
    path("clients/<int:pk>/delete/", ClientDeleteView.as_view(), name="client-delete"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("clients/<int:pk>", ClientDeleteView.as_view(), name="client-delete"),
]
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM1NDA2MDIxLCJpYXQiOjE3MzQ1NDIwMjEsImp0aSI6ImViNTdjZjA0NDgxMjQ1YjVhMjA4ZWZmNmU2OGE1NzdlIiwidXNlcl9pZCI6MX0.8rLXsKiYUuTtQ_4xBs70_Njelq4d-AT8j7pnzsMRics
