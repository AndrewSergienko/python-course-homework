import requests
import random


def request_json(url, params=None):
    response = requests.get(url, params)
    if response.status_code == 200:
        return response.json()


def get_user(user_id: int):
    user = request_json(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    return f"id: {user['id']}\nname: {user['name']}\nusername: {user['username']}\nemail: {user['email']}\nphone: {user['phone']}"


def get_users():
    users = request_json(f"https://jsonplaceholder.typicode.com/users")
    return "\n".join([f"id: {user['id']} name: {user['name']} username: {user['username']}" for user in users])


def get_post(post_id: int):
    post = request_json(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    return post


def get_post_comments(post_id: int):
    params = {"postId": post_id}
    return request_json(f"https://jsonplaceholder.typicode.com/comments", params)


def get_posts_by_user(user_id: int):
    params = {"userId": user_id}
    posts = request_json(f"https://jsonplaceholder.typicode.com/posts", params)
    res_str = ""
    for post in posts:
        res_str += f"post_id: {post['id']}; user_id: {post['userId']}; title: {post['title']}\n"
    return res_str


def get_info_about_post(post_id: int):
    post = get_post(post_id)
    comments = get_post_comments(post_id)
    comments_id = ", ".join([str(comment['id']) for comment in comments])[:-1]
    return f"id: {post['id']}\nTitle: {post['title']}\nBody: {post['body']}\nComments_num: {len(comments)}\nComments_id: {comments_id}"


def get_todo_list(user_id, completed):
    params = {'completed': completed, 'userId': user_id}
    todo_items = request_json(f"https://jsonplaceholder.typicode.com/todos", params)
    return "\n".join([f"id: {todo_item['id']}; user_id: {todo_item['userId']} title: {todo_item['title']}" for todo_item in todo_items])


def get_random_photo():
    photos = request_json("https://jsonplaceholder.typicode.com/photos")
    return random.choice(photos)["url"]
