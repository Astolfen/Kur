from main import *

class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.controller.title("Страница администратора")

        self.toolbar = tk.Frame(self)
        self.toolbar.pack(side="top", fill="x")

        button_creat_actor = tk.Button(self.toolbar, text="Создать Актера", command=self.button_cr_ac_clicked)
        button_creat_actor.pack(side="left")

        button_creat_genres = tk.Button(self.toolbar, text="Создать Жанр", command=self.button_cr_ge_clicked)
        button_creat_genres.pack(side="left")

        button_creat_movie = tk.Button(self.toolbar, text="Создать Фильм", command=self.button_cr_mv_clicked)
        button_creat_movie.pack(side="left")

        button_exit = tk.Button(self.toolbar, text="Выход", command=self.button_exit)
        button_exit.pack(side="left")

        self.form_panel = tk.Frame(self)  # Панель для формы (пока скрыта)
        self.actor_form_panel = tk.Frame(self.form_panel)  # Панель для формы создания актера
        self.genres_form_panel = tk.Frame(self.form_panel)  # Панель для формы создания жанров
        self.movie_form_panel = tk.Frame(self.form_panel)  # Панель для формы создания фильма

        self.create_actor_form()
        self.create_genres_form()
        self.create_movie_form()

        self.form_panel.pack()

    def create_actor_form(self):
        # Элементы формы для создания актера
        self.actor_name_label = tk.Label(self.actor_form_panel, text="Имя актера:")
        self.actor_name_label.pack()
        self.actor_name_entry = tk.Entry(self.actor_form_panel)
        self.actor_name_entry.pack()

        self.actor_age_label = tk.Label(self.actor_form_panel, text="Возраст актера:")
        self.actor_age_label.pack()
        self.actor_age_entry = tk.Entry(self.actor_form_panel)
        self.actor_age_entry.pack()

        self.save_actor_button = tk.Button(self.actor_form_panel, text="Создать актера", command=self.save_actor)
        self.save_actor_button.pack()

    def create_genres_form(self):
        self.genres_name_label = tk.Label(self.genres_form_panel, text="Название жанра:")
        self.genres_name_label.pack()
        self.genres_name_entry = tk.Entry(self.genres_form_panel)
        self.genres_name_entry.pack()

        self.save_genres_button = tk.Button(self.genres_form_panel, text="Создать жанр", command=self.save_genres)
        self.save_genres_button.pack()

    def create_movie_form(self):
        # Элементы формы для создания фильма
        self.movie_name_label = tk.Label(self.movie_form_panel, text="Название фильма:")
        self.movie_name_label.pack()
        self.movie_name_entry = tk.Entry(self.movie_form_panel)
        self.movie_name_entry.pack()

        self.movie_year_label = tk.Label(self.movie_form_panel, text="Год выпуска:")
        self.movie_year_label.pack()
        self.movie_year_entry = tk.Entry(self.movie_form_panel)
        self.movie_year_entry.pack()

        self.movie_description_label = tk.Label(self.movie_form_panel, text="Описание:")
        self.movie_description_label.pack()
        self.movie_description_entry = tk.Text(self.movie_form_panel, width=100, height=10)
        self.movie_description_entry.pack(fill=tk.BOTH, expand=True)
        # self.movie_description_entry = tk.Entry(self.movie_form_panel,width=100)
        # self.movie_description_entry.pack()

        self.actor_list_label = tk.Label(self.movie_form_panel, text="Выберите актеров:")
        self.actor_list_label.pack()

        # Создаем список для выбора актеров
        self.actor_listbox = tk.Listbox(self.movie_form_panel, selectmode=tk.MULTIPLE, width=80, exportselection=0)
        self.actor_listbox.pack()

        # Заполняем список для выбора актеров
        self.fill_actor_listbox()

        self.genres_list_label = tk.Label(self.movie_form_panel, text="Выберите жанры:")
        self.genres_list_label.pack()

        # Создаем список для выбора актеров
        self.genres_listbox = tk.Listbox(self.movie_form_panel, selectmode=tk.MULTIPLE, width=80, exportselection=0)
        self.genres_listbox.pack()

        # Заполняем список для выбора актеров
        self.fill_genres_listbox()

        self.save_movie_button = tk.Button(self.movie_form_panel, text="Создать фильм", command=self.save_movie)
        self.save_movie_button.pack()

    def save_actor(self):
        # Получаем данные из полей ввода
        actor_name = self.actor_name_entry.get()
        actor_age = self.actor_age_entry.get()

        if actor_name == "":
            messagebox.showerror("Ошибка", "Имя не введено")
            return
        if actor_age == "":
            messagebox.showerror("Ошибка", "Пароль не введен")
            return

        try:
            Actor.create(name=actor_name, age=int(actor_age))
            messagebox.showinfo("Успешно", "Успешно сохранен")
        except pw.IntegrityError:
            messagebox.showerror("Ошибка", "Такой актер уже есть")

    def save_genres(self):
        # Получаем данные из полей ввода
        genres_name = self.genres_name_entry.get()

        if genres_name == "":
            messagebox.showerror("Ошибка", "Имя не введено")
            return

        try:
            Genres.create(name=genres_name)
            messagebox.showinfo("Успешно", "Успешно сохранен")
        except pw.IntegrityError:
            messagebox.showerror("Ошибка", "Такой жанр уже создан")

    def save_movie(self):
        # Получаем данные из полей ввода

        movie_name = self.movie_name_entry.get()
        movie_year = self.movie_year_entry.get()
        movie_description = self.movie_description_entry.get("1.0", tk.END)
        index_selected_actors = [self.actor_listbox.get(idx)[1] for idx in self.actor_listbox.curselection()]
        index_selected_genres = [self.genres_listbox.get(idx)[1] for idx in self.genres_listbox.curselection()]

        if movie_name == "":
            messagebox.showerror("Ошибка", "Имя не введено")
            return

        if movie_year == "":
            messagebox.showerror("Ошибка", "Год не введено")
            return

        if movie_description == "":
            messagebox.showerror("Ошибка", "Описание не введено")
            return

        try:
            Movie.create(name=movie_name, releaseYear=int(movie_year), description=movie_description)

            try:
                id = Movie.get(Movie.name == movie_name, Movie.releaseYear == movie_year)
                for i in index_selected_genres:
                    GenresMovie.create(movie_id=id.id, genres_id=i)
                for i in index_selected_actors:
                    PlayMovie.create(movie_id=id.id, actor_id=i)
            except pw.IntegrityError:
                messagebox.showerror("Ошибка", "Проблема с созданием")

            messagebox.showinfo("Успешно", "Успешно сохранен")
        except pw.IntegrityError:
            messagebox.showerror("Ошибка", "Такой фильм уже есть")

    def fill_actor_listbox(self):
        self.actor_listbox.delete(0, tk.END)
        actors = Actor.select()
        for actor in actors:
            self.actor_listbox.insert(tk.END, (actor.name, actor))

    def fill_genres_listbox(self):
        self.genres_listbox.delete(0, tk.END)
        genres = Genres.select()
        for genr in genres:
            self.genres_listbox.insert(tk.END, (genr.name, genr))

    def button_exit(self):
        self.controller.geometry("400x200")
        self.controller.show_frame(LoginPage)

    def button_cr_ac_clicked(self):
        self.actor_form_panel.pack()
        self.genres_form_panel.pack_forget()
        self.movie_form_panel.pack_forget()

    def button_cr_ge_clicked(self):
        self.genres_form_panel.pack()
        self.actor_form_panel.pack_forget()
        self.movie_form_panel.pack_forget()

    def button_cr_mv_clicked(self):
        self.fill_actor_listbox()
        self.fill_genres_listbox()
        self.movie_form_panel.pack()
        self.actor_form_panel.pack_forget()
        self.genres_form_panel.pack_forget()
