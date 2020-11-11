from django.urls import path

from app.endpoints.club.create import CreateClubEndpoint
from app.endpoints.member.accept import AcceptMembershipEndpoint
from app.endpoints.member.list import ListMembersEndpoint
from app.endpoints.member.put import PutMemberEndpoint
from app.endpoints.time.create import CreateTimeEndpoint
from app.endpoints.trainee.list import ListTraineesEndpoint
from app.endpoints.user.get import GetUserEndpoint
from app.endpoints.user.users import UsersEndpoint
from app.endpoints.user.login import LoginEndpoint
from app.endpoints.user.logout import LogoutEndpoint

urlpatterns = [
    path('login/', LoginEndpoint.as_view(), name='login endpoint'),
    path('logout/', LogoutEndpoint.as_view(), name='logout endpoint'),
    path('users/', UsersEndpoint.as_view(), name='create user endpoint'),
    path('user/', GetUserEndpoint.as_view(), name='create user endpoint'),
]

# Club
urlpatterns += [
    path('club/', CreateClubEndpoint.as_view(), name='create new club'),
    path('club/<int:club_id>/members/', ListMembersEndpoint.as_view(), name='list club members'),
    path('club/<int:club_id>/members/<int:user_id>/', PutMemberEndpoint.as_view(), name='put member to club')
]

# Members
urlpatterns += [
    path('members/<int:member_id>/accept/', AcceptMembershipEndpoint.as_view(), name='accepts a membership')
]

# Trainees
urlpatterns += [
    path('trainees/', ListTraineesEndpoint.as_view(), name='list trainees')
]

# Time
urlpatterns += [
    path('time/', CreateTimeEndpoint.as_view(), name='create new time')
]
