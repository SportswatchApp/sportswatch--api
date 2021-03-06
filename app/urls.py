from django.urls import path

from app.endpoints.category.create import CreateCategoryEndPoint
from app.endpoints.club.apply import ApplyMembershipView
from app.endpoints.club.create import CreateClubEndpoint
from app.endpoints.club.list import ListClubsEndpoints
from app.endpoints.member.accept import AcceptMembershipEndpoint
from app.endpoints.member.list import ListMembersEndpoint
from app.endpoints.member.put import PutMemberEndpoint
from app.endpoints.time.create import CreateTimeEndpoint
from app.endpoints.trainee.list import ListTraineesEndpoint
from app.endpoints.trainee.times import ListTraineeTimesEndpoint
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
    path('club/<int:club_id>/members/<int:user_id>/', PutMemberEndpoint.as_view(), name='put member to club'),
    path('clubs/', ListClubsEndpoints.as_view(), name='list clubs endpoint'),
    path('club/<int:club_id>/apply/', ApplyMembershipView.as_view(), name='apply membership for club'),
]

# Members
urlpatterns += [
    path('members/<int:member_id>/accept/', AcceptMembershipEndpoint.as_view(), name='accepts a membership')
]

# Trainees
urlpatterns += [
    path('trainees/', ListTraineesEndpoint.as_view(), name='list trainees'),
    path('trainees/<int:trainee_id>/times/', ListTraineeTimesEndpoint.as_view(), name='get times for trainee')
]

# Time
urlpatterns += [
    path('time/', CreateTimeEndpoint.as_view(), name='create new time')
]

# Categories
urlpatterns += [
    path('category/', CreateCategoryEndPoint.as_view(), name='create new category')
]
