from django.urls import path

from app.endpoints.club.create import CreateClubEndpoint
from app.endpoints.docs import DocsView
from app.endpoints.member.list import ListMembersEndpoint
from app.endpoints.user.create import CreateUserEndpoint
from app.endpoints.user.login import LoginEndpoint
from app.endpoints.user.logout import LogoutEndpoint

urlpatterns = [
    path('', DocsView.as_view(), name='docs'),
    path('login/', LoginEndpoint.as_view(), name='login endpoint'),
    path('logout/', LogoutEndpoint.as_view(), name='logout endpoint'),
    path('users/', CreateUserEndpoint.as_view(), name='create user endpoint')
]

# Club
urlpatterns += [
    path('club/', CreateClubEndpoint.as_view(), name='create new club'),
    path('club/<int:club_id>/members/', ListMembersEndpoint.as_view(), name='list club members')
]
