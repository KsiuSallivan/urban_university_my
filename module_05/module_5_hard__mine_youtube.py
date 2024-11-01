import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        if self.nickname == other.nickname and self.password == other.password:
            return True
        else:
            return False

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration  # sec
        self.time_now = time_now  # секунда остановки (изначально 0)
        self.adult_mode = adult_mode

    def __eq__(self, other):
        if self.title == other.title:
            return True
        else:
            return False

    def __repr__(self):
        return f'"{self.title}"'


class UrTube:
    def __init__(self, users: list[User] = None, videos: list[Video] = None, current_user: User = None):
        if users is not None:
            self.users = users
        else:
            self.users = [] # список объектов User
        if videos is not None:
            self.videos = videos # список объектов Video
        else:
            self.videos = []
        self.current_user = current_user # текущий пользователь, User

    def log_in(self, nickname: str, password: str):
        """
        Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем.
        Если такой пользователь существует, то current_user меняется на найденного.
        Помните, что password передаётся в виде строки, а сравнивается по хэшу
        """
        logging_user = User(nickname, password, 0)
        for user in self.users:
            if logging_user == user:
                self.current_user = user

    def register(self, nickname, password, age):
        """
        Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
        Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        После регистрации, вход выполняется автоматически.
        """
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        self.users.append(User(nickname,password,age))
        self.log_in(nickname,password)

    def log_out(self):
        """
         Метод log_out для сброса текущего пользователя на None.
         """
        self.current_user = None
        return self.current_user

    def add(self, *attrs: Video):
        """
        Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
        если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
        """
        for video in attrs:
            if video not in self.videos:
                self.videos.append(video)
            else:
                pass

    def get_videos(self, search_word):
        """
        Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово.
        Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
        """
        video_list: list[Video] = []
        for video in self.videos:
            if video.title.lower().__contains__(search_word.lower()):
                video_list.append(video)
        return video_list

    def watch_video(self, title):
        """
        Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
        то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
        После текущее время просмотра данного видео сбрасывается.
        Для метода watch_video так же учитывайте следующие особенности:
        Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
        Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
        Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
        После воспроизведения нужно выводить: "Конец видео"
        """
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        video_list = self.get_videos(title)
        for video in video_list:
            if video.title == title:
                if video.adult_mode is True and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                for i in range(1, video.duration+1):
                    time.sleep(1)
                    video.time_now = i
                    print(i, end=' ')
                print('Конец видео')


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