import requests
import random
import os, json
from testtask.models import Post
from django.contrib.auth.models import User
from django.http import JsonResponse

dir_path = os.path.dirname(os.path.realpath(__file__))


def start_bots(request):

    with open(dir_path+'/bot_config.json', 'r') as f:
        config = json.load(f)

    def bot_signups_user():
        signup_url = 'http://127.0.0.1:8000/api/users/signup/'
        token_url = 'http://127.0.0.1:8000/api/users/token/'
        username = 'bot-{}'.format(''.join(['{}'\
            .format(random.randrange(0, 101, 1)) for _ in range(5)]))
        password = ''\
            .join(['{}'.format(random.randrange(0, 101, 1)) for _ in range(8)])
        signup_data = {
            "username": username,
            "password": password,
            "password2": password,
        }
        usr = requests.post(signup_url, data=signup_data)

        login_data = {
            "username": username,
            "password": password,
        }
        token = requests.post(token_url, data=login_data)
        token_json = token.json()
        print('SignUp status:', usr)
        return token_json['access']

    def bot_creates_post(headers):
        url = 'http://127.0.0.1:8000/api/post/new/'
        postdata = {
            "title": "Whatever {}".format(headers['Authorization']),
            "text": "Whatever",
        }
        r = requests.post(url, headers=headers, data=postdata)
        print('PostCreate status:', r)

    def bot_likes_post(headers):
        all_posts = Post.objects.all()
        rndm_post_id = random.choice([i.id for i in all_posts])
        url_like = 'http://127.0.0.1:8000/api/post/{}/like/'\
                                                .format(rndm_post_id)
        l = requests.put(url_like, headers=headers)
        print('LikePost status:', l)

    for _ in range(config['num_of_users']):
        token = bot_signups_user()
        print(token)
        headers = {'Authorization': 'Bearer {}'.format(token)}
        max_posts_per_user = config['max_posts_per_user']
        max_likes_per_user = config['max_likes_per_user']
        for _ in range(random.randint(0, max_posts_per_user)):
            bot_creates_post(headers)
        for _ in range(random.randint(0, max_likes_per_user)):
            bot_likes_post(headers)


    return JsonResponse(config, safe=True)

# Make bots work cocurrently
# def job_function():
#     with concurrent.futures.ThreadPoolExecutor(max_workers=config['num_of_users'])\
#                                                                 as executor:
#         for _ in range(config['num_of_users']):
#             executor.submit(start_bot)
    # return JsonResponse(config, safe=True)
