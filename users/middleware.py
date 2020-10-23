# from django.utils import timezone
# from django.conf import settings
# from django.utils.deprecation import MiddlewareMixin
# from datetime import datetime as dt
# from django.contrib.auth.models import User
# from .models import Profile
#
# class UpdateLastActivityMiddleware(object):
#
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#
#         if request.user.is_authenticated:
#             profile = Profile.objects.get(user__id=request.user.id)
#             profile.last_activity = dt.now
#             profile.save()
#
#         return self.get_response(request)
