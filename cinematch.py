import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def __repr__(self):
        return f"{self.title} (Genre: {self.genre}, Rating: {self.rating})"


class CineMatch:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, genre, rating):
        movie = Movie(title, genre, rating)
        self.movies.append(movie)

    def search_movies_by_title(self, title):
        return [movie for movie in self.movies if title.lower() in movie.title.lower()]

    def search_movies_by_genre(self, genre):
        return [movie for movie in self.movies if genre.lower() in movie.genre.lower()]

    def recommend_top_n_movies(self, n):
        if n > len(self.movies):
            n = len(self.movies)
        return sorted(self.movies, key=lambda movie: movie.rating, reverse=True)[:n]

    def delete_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                self.movies.remove(movie)
                return True
        return False


class CineMatchApp:
    def __init__(self, root):
        self.cine_match = CineMatch()
        self.root = root
        self.root.title("CineMatch - Movie Recommendation System")
        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg='#121212')

        # Header
        header_frame = tk.Frame(self.root, bg='#1f1f1f', pady=10)
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")
        header_label = tk.Label(header_frame, text="CineMatch", font=("Helvetica", 24, "bold"), fg='#ffffff',
                                bg='#1f1f1f')
        header_label.pack()

        # Add Movie Section
        add_frame = tk.LabelFrame(self.root, text="Add Movie", font=("Helvetica", 14), fg='#ffffff', bg='#1f1f1f', bd=0,
                                  padx=20, pady=10)
        add_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        tk.Label(add_frame, text="Title:", fg='#ffffff', bg='#1f1f1f', font=("Helvetica", 12)).grid(row=0, column=0,
                                                                                                    sticky="w")
        self.title_entry = tk.Entry(add_frame, font=("Helvetica", 12))
        self.title_entry.grid(row=0, column=1, pady=5, sticky="ew")

        tk.Label(add_frame, text="Genre:", fg='#ffffff', bg='#1f1f1f', font=("Helvetica", 12)).grid(row=1, column=0,
                                                                                                    sticky="w")
        self.genre_entry = tk.Entry(add_frame, font=("Helvetica", 12))
        self.genre_entry.grid(row=1, column=1, pady=5, sticky="ew")

        tk.Label(add_frame, text="Rating:", fg='#ffffff', bg='#1f1f1f', font=("Helvetica", 12)).grid(row=2, column=0,
                                                                                                     sticky="w")
        self.rating_entry = tk.Entry(add_frame, font=("Helvetica", 12))
        self.rating_entry.grid(row=2, column=1, pady=5, sticky="ew")

        self.add_button = tk.Button(add_frame, text="Add Movie", font=("Helvetica", 12), command=self.add_movie,
                                    bg='#4caf50', fg='#ffffff', bd=0, padx=10, pady=5)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Search and Recommend Section
        search_frame = tk.LabelFrame(self.root, text="Search & Recommend Movies", font=("Helvetica", 14), fg='#ffffff',
                                     bg='#1f1f1f', bd=0, padx=20, pady=10)
        search_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        tk.Label(search_frame, text="Search by Title:", fg='#ffffff', bg='#1f1f1f', font=("Helvetica", 12)).grid(row=0,
                                                                                                                 column=0,
                                                                                                                 sticky="w")
        self.search_title_entry = tk.Entry(search_frame, font=("Helvetica", 12))
        self.search_title_entry.grid(row=0, column=1, pady=5, sticky="ew")

        tk.Label(search_frame, text="Search by Genre:", fg='#ffffff', bg='#1f1f1f', font=("Helvetica", 12)).grid(row=1,
                                                                                                                 column=0,
                                                                                                                 sticky="w")
        self.search_genre_entry = tk.Entry(search_frame, font=("Helvetica", 12))
        self.search_genre_entry.grid(row=1, column=1, pady=5, sticky="ew")

        self.search_button = tk.Button(search_frame, text="Search Movies", font=("Helvetica", 12),
                                       command=self.search_movies, bg='#2196f3', fg='#ffffff', bd=0, padx=10, pady=5)
        self.search_button.grid(row=2, column=0, columnspan=2, pady=10)

        tk.Label(search_frame, text="Top N Movies:", fg='#ffffff', bg='#1f1f1f', font=("Helvetica", 12)).grid(row=3,
                                                                                                              column=0,
                                                                                                              sticky="w")
        self.top_n_entry = tk.Entry(search_frame, font=("Helvetica", 12))
        self.top_n_entry.grid(row=3, column=1, pady=5, sticky="ew")

        self.recommend_button = tk.Button(search_frame, text="Recommend Movies", font=("Helvetica", 12),
                                          command=self.recommend_movies, bg='#f57c00', fg='#ffffff', bd=0, padx=10,
                                          pady=5)
        self.recommend_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Delete Movie Section
        delete_frame = tk.LabelFrame(self.root, text="Delete Movie", font=("Helvetica", 14), fg='#ffffff', bg='#1f1f1f',
                                     bd=0, padx=20, pady=10)
        delete_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        tk.Label(delete_frame, text="Delete by Title:", fg='#ffffff', bg='#1f1f1f', font=("Helvetica", 12)).grid(row=0,
                                                                                                                 column=0,
                                                                                                                 sticky="w")
        self.delete_title_entry = tk.Entry(delete_frame, font=("Helvetica", 12))
        self.delete_title_entry.grid(row=0, column=1, pady=5, sticky="ew")

        self.delete_button = tk.Button(delete_frame, text="Delete Movie", font=("Helvetica", 12),
                                       command=self.delete_movie, bg='#f44336', fg='#ffffff', bd=0, padx=10, pady=5)
        self.delete_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Results Section
        results_frame = tk.LabelFrame(self.root, text="Results", font=("Helvetica", 14), fg='#ffffff', bg='#1f1f1f',
                                      bd=0, padx=20, pady=10)
        results_frame.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

        self.result_listbox = tk.Listbox(results_frame, height=15, font=("Helvetica", 12), fg='#000000', bg='#ffffff',
                                         selectbackground='#1f1f1f', selectforeground='#ffffff')
        self.result_listbox.pack(fill="both", expand=True, pady=10)

        self.clear_button = tk.Button(results_frame, text="Clear Fields", font=("Helvetica", 12),
                                      command=self.clear_fields, bg='#9e9e9e', fg='#ffffff', bd=0, padx=10, pady=5)
        self.clear_button.pack(pady=10)

    def add_movie(self):
        title = self.title_entry.get()
        genre = self.genre_entry.get()
        try:
            rating = float(self.rating_entry.get())
            if title and genre:
                self.cine_match.add_movie(title, genre, rating)
                messagebox.showinfo("Success", f"Movie '{title}' added successfully.")
                self.clear_fields()
            else:
                messagebox.showerror("Error", "Title and genre cannot be empty.")
        except ValueError:
            messagebox.showerror("Error", "Invalid rating. Please enter a number.")

    def search_movies(self):
        title = self.search_title_entry.get()
        genre = self.search_genre_entry.get()
        if title:
            result = self.cine_match.search_movies_by_title(title)
        elif genre:
            result = self.cine_match.search_movies_by_genre(genre)
        else:
            result = []

        self.display_results(result)

    def recommend_movies(self):
        try:
            n = int(self.top_n_entry.get())
            result = self.cine_match.recommend_top_n_movies(n)
            self.display_results(result)
        except ValueError:
            messagebox.showerror("Error", "Invalid number. Please enter an integer.")

    def delete_movie(self):
        title = self.delete_title_entry.get()
        if self.cine_match.delete_movie(title):
            messagebox.showinfo("Success", f"Movie '{title}' deleted successfully.")
            self.clear_fields()
        else:
            messagebox.showerror("Error", f"Movie '{title}' not found.")

    def display_results(self, result):
        self.result_listbox.delete(0, tk.END)
        if result:
            for movie in result:
                self.result_listbox.insert(tk.END, movie)
        else:
            self.result_listbox.insert(tk.END, "No results found.")

    def clear_fields(self):
        self.title_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)
        self.search_title_entry.delete(0, tk.END)
        self.search_genre_entry.delete(0, tk.END)
        self.top_n_entry.delete(0, tk.END)
        self.delete_title_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = CineMatchApp(root)
    root.mainloop()
