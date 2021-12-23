import request_tools as rt


def menu(choice, user_id, subpoint=None):
    if subpoint is None:
        if choice == "1":
            print(rt.get_user(user_id))
            return True
        if choice == "2":
            menu_subitems = "1. Перелік постів користувача\n" \
            "2. інформація про конкретний пост"
            print(menu_subitems)
            menu(input("Ваш вибір: "), user_id, '2')
            return True
        if choice == "3":
            menu_subitems = "1. Список невиконаних задач\n" \
            "2. Список виконаних задач"
            print(menu_subitems)
            menu(input("Ваш вибір: "), user_id, '3')
            return True
        if choice == "4":
            print(rt.get_random_photo())
            return True
    if subpoint == "2":
        if choice == "1":
            print(rt.get_posts_by_user(user_id))
            return True
        if choice == "2":
            post_id = int(input("Введіть ід поста: "))
            print(rt.get_info_about_post(post_id))
            return True
    if subpoint == "3":
        if choice == "1":
            completed = "true"
        if choice == "2":
            completed = "false"
        print(rt.get_todo_list(user_id, completed))
        return True


def start():
    print(rt.get_users())
    user_id = int(input("Введіть ІД юзера: "))
    result = True
    while result:
        print("""
        1. Повна інформація по користувачу
        2. Меню постів
        3. TODO меню
        4. URL рандомної картинки
        """)
        point = input("Виберіть пункт: ")
        result = menu(point, user_id)


start()