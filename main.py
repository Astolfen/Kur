# from workBD import BD
import os
import tkinter as tk
from tkinter import messagebox
from admin_page import *
from tkinter.simpledialog import Dialog
import yadisk
from models import *


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        username_label = tk.Label(self, text="Логин:")
        username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        password_label = tk.Label(self, text="Пароль:")
        password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        login_button = tk.Button(self, text="Войти", command=self.login)
        login_button.pack()

        register_button = tk.Button(self, text="Зарегистрироваться", command=self.register)
        register_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # формирует запрос на поиск в бд аккаунта
        try:
            user = User.get(User.name == username)
            if user.password == password:
                if user.role.name == 'user':
                    self.controller.geometry("1280x800")
                    self.controller.show_frame(UserPage)
                else:
                    self.controller.geometry("1280x800")
                    self.controller.show_frame(AdminPage)
            else:
                messagebox.showerror("Ошибка", "Неверный пароль")
        except User.DoesNotExist:
            messagebox.showerror("Ошибка", "Пользователь не найден")

    def register(self):
        self.controller.show_frame(RegisterPage)


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        username_label = tk.Label(self, text="Новый логин:")
        username_label.pack()
        self.new_username_entry = tk.Entry(self)
        self.new_username_entry.pack()

        password_label = tk.Label(self, text="Новый пароль:")
        password_label.pack()
        self.new_password_entry = tk.Entry(self, show="*")
        self.new_password_entry.pack()

        confirm_password_label = tk.Label(self, text="Подтвердите пароль:")
        confirm_password_label.pack()
        self.confirm_password_entry = tk.Entry(self, show="*")
        self.confirm_password_entry.pack()

        register_button = tk.Button(self, text="Зарегистрироваться", command=self.do_register)
        register_button.pack()

    def do_register(self):
        new_username = self.new_username_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if new_username == "":
            messagebox.showerror("Ошибка", "Имя не введено")
            return
        if new_password == "":
            messagebox.showerror("Ошибка", "Пароль не введен")
            return

        if new_password == confirm_password:
            try:
                User.create(name=new_username, password=confirm_password, role=2)
                messagebox.showinfo("Успешно", "Регистрация завершена")
                self.controller.show_frame(LoginPage)
            except pw.IntegrityError:
                messagebox.showerror("Ошибка", "Пользователь с даным именем сущесвует")
        else:
            messagebox.showerror("Ошибка", "Пароли не совпадают")


class UserPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.toolbar = tk.Frame(self)
        self.toolbar.pack(side="top", fill="x")

        button_search_movie = tk.Button(self.toolbar, text="Поиск фильма", command=self.button_sh_mv_clicked)
        button_search_movie.pack(side="left")

        button_search_actor = tk.Button(self.toolbar, text="Поиск актера", command=self.button_sh_ac_clicked)
        button_search_actor.pack(side="left")

        films = Movie.select()
        for film in films:
            film_label = tk.Label(self, text=film.name, fg="blue", cursor="hand2")
            film_label.pack(anchor="w", padx=10, pady=5)
            film_label.bind("<Button-1>", lambda event, filmm=film: self.show_movie_page(filmm))

    def show_movie_page(self, film):
        self.controller.show_frame(MoviePage)
        self.controller.frames[MoviePage].set_movie_info(film)

    def show_actor_page(self, actor):
        self.controller.show_frame(ActorPage)
        self.controller.frames[ActorPage].set_actor_info(actor)

    def button_sh_mv_clicked(self):
        # Создаем диалоговое окно для ввода названия фильма
        movie_name = tk.simpledialog.askstring("Поиск фильма", "Введите название фильма:")
        if movie_name:
            # Выполняем поиск фильмов по введенному названию
            found_movies = Movie.select().where(Movie.name == movie_name)
            if found_movies:
                # Отображаем найденные фильмы в новом окне
                self.show_search_results_movies(found_movies)
            else:
                messagebox.showinfo("Результаты поиска", "Фильм с таким названием не найден")

    def show_search_results_movies(self, movies):
        # Создаем новое окно для отображения результатов поиска
        search_results_window = tk.Toplevel(self)
        search_results_window.title("Результаты поиска")

        if movies:
            for movie in movies:
                text = f"{movie.name} : {movie.releaseYear}"
                movie_label = tk.Label(search_results_window, text=text, fg="blue", cursor="hand2")
                movie_label.pack()
                movie_label.bind("<Button-1>", lambda event, film=movie: self.show_movie_page(film))
        else:
            no_results_label = tk.Label(search_results_window, text="Фильмы с таким названием не найдены")
            no_results_label.pack()

    def button_sh_ac_clicked(self):
        actor_name = tk.simpledialog.askstring("Поиск фильма", "Введите название фильма:")
        if actor_name:
            found_actors = Actor.select().where(Actor.name == actor_name)
            if found_actors:
                self.show_search_results_actors(found_actors)
            else:
                messagebox.showinfo("Результаты поиска", "Фильм с таким названием не найден")

    def show_search_results_actors(self, actors):
        search_results_window = tk.Toplevel(self)
        search_results_window.title("Результаты поиска")

        if actors:
            for actor in actors:
                text = f"{actor.name} : {actor.age}"
                movie_label = tk.Label(search_results_window, text=text, fg="blue", cursor="hand2")
                movie_label.pack()
                movie_label.bind("<Button-1>", lambda event, film=actor: self.show_actor_page(film))
        else:
            no_results_label = tk.Label(search_results_window, text="Фильмы с таким названием не найдены")
            no_results_label.pack()


class MoviePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Это страница фильма")
        label.pack()

        user_label = tk.Label(self, text="Перейти к странице пользователя", fg="blue", cursor="hand2")
        user_label.pack()
        user_label.bind("<Button-1>", lambda event: controller.show_frame(UserPage))

        self.movie_name_label = tk.Label(self, text="Название:")
        self.movie_name_label.pack(anchor="w", padx=10, pady=5)

        self.movie_release_label = tk.Label(self, text="Год выпуска:")
        self.movie_release_label.pack(anchor="w", padx=10, pady=5)

        self.movie_description_label = tk.Label(self, text="Описание:", wraplength=600, justify="left")
        self.movie_description_label.pack(anchor="w", padx=10, pady=5)

        self.movie_actors_label = tk.Label(self, text="Актёры:", wraplength=500, justify="left")
        self.movie_actors_label.pack(anchor="w", padx=10, pady=5)

        self.actor_labels = []

    def show_actor_page(self, actor):
        self.controller.show_frame(ActorPage)
        self.controller.frames[ActorPage].set_actor_info(actor)

    def set_movie_info(self, film):
        self.movie_name_label.config(text=f"Название: {film.name}")
        self.movie_release_label.config(text=f"Год выпуска: {film.releaseYear}")
        self.movie_description_label.config(text=f"Описание: {film.description}")

        for label in self.actor_labels:
            label.destroy()
        self.actor_labels = []

        actors = PlayMovie.select().where(PlayMovie.movie_id == film.id)
        for i in actors:
            actor = Actor.get(Actor.id == i.actor_id)
            actor_label = tk.Label(self, text=actor.name, fg="blue", cursor="hand2")
            actor_label.pack(anchor="w", padx=10, pady=5)
            actor_label.bind("<Button-1>", lambda event, actorr=actor: self.show_actor_page(actorr))
            self.actor_labels.append(actor_label)


class ActorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Это страница фильма")
        label.pack()

        user_label = tk.Label(self, text="Перейти к странице пользователя", fg="blue", cursor="hand2")
        user_label.pack()
        user_label.bind("<Button-1>", lambda event: controller.show_frame(UserPage))

        self.actor_name_label = tk.Label(self, text="Имя:")
        self.actor_name_label.pack(anchor="w", padx=10, pady=5)

        self.actor_age_label = tk.Label(self, text="Возраст:")
        self.actor_age_label.pack(anchor="w", padx=10, pady=5)

        self.actor_movies_label = tk.Label(self, text="Фильмы:", wraplength=500, justify="left")
        self.actor_movies_label.pack(anchor="w", padx=10, pady=5)

        self.film_labels = []

    def show_movie_page(self, film):
        self.controller.show_frame(MoviePage)
        self.controller.frames[MoviePage].set_movie_info(film)

    def set_actor_info(self, actor):
        self.actor_name_label.config(text=f"Имя: {actor.name}")
        self.actor_age_label.config(text=f"Возраст: {actor.age}")

        for label in self.film_labels:
            label.destroy()
        self.film_labels = []

        films = Movie.select()
        for film in films:
            film_label = tk.Label(self, text=film.name, fg="blue", cursor="hand2")
            film_label.pack(anchor="w", padx=10, pady=5)
            film_label.bind("<Button-1>", lambda event, filmm=film: self.show_movie_page(filmm))
            self.film_labels.append(film_label)


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, RegisterPage, UserPage, AdminPage, MoviePage, ActorPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == '__main__':
    app = SampleApp()
    app.geometry("400x200")
    app.mainloop()

    # Создаем соединение с Yandex Disk
    y = yadisk.YaDisk(token="y0_AgAAAAAec8HBAAtofAAAAAD9T9PqAAA2TRPIZnFKmoZoeYu08EvoIR6w-A")
    print(y.check_token())

    host = 'localhost'  # Замените на хост вашей базы данных
    port = '5432'  # Замените на порт вашей базы данных
    user = 'postgres'  # Замените на имя пользователя вашей базы данных
    password = '1111'  # Замените на пароль вашей базы данных
    database = 'cursach'  # Замените на имя вашей базы данных

    # Путь для сохранения резервной копии базы данных
    backup_file = 'O:/backup.sql'  # Замените на имя файла, куда будет сохранена резервная копия

    # Формируем команду для создания резервной копии базы данных
    dump_command = f'pg_dump -h {host} -p {port} -U {user} -d {database} --schema=public -F c -b -v -f {backup_file}'
    os.system(dump_command)

    print("Резервная копия базы данных создана успешно.")

    # Загружаем резервную копию на Yandex Disk
    y.upload("O:/backup.sql", 'backup.sql')
