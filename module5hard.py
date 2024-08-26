import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self, users = [], videos = [], current_user = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user # Текущий пользователь

    def add(self, *Videos):
        for new_video in Videos:
            video_exist = False
            for v in self.videos:
                if new_video.title == v.title:
                    video_exist = True
                    print("Такое видео уже есть")
            if not video_exist:
                self.videos.append(new_video)

    def get_videos(self, sub_titel):
        result = []
        for v in self.videos:
            if sub_titel.lower() in v.title.lower():
                result.append(v.title)
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return None

        for v in self.videos:
            if title == v.title:
                if v.adult_mode and self.current_user.age > 17:
                    for sec in range(v.duration):
                        print(sec, sep=" ", end="")
                        time.sleep(1)
                    print(" Конец видео")
                elif v.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    print(title, v.adult_mode)

    def log_in(self, nickname, password):
        for u in self.users:
            if u.nickname == nickname and u.password == password:
                self.current_user = u
                print("Юзер найден")

    def register(self, nickname, password, age):
        for u in self.users:
            if u.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return None
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')