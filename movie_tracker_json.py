import os
import json

FILENAME="movies.json"

def load_movies():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME,'r',encoding='utf-8') as f:
        return json.load(f)

def save_movies(movies):
    with open(FILENAME,'w',encoding="utf-8") as f:
        json.dump(movies,f,indent=3)

def add_movies(movies):
    title=input("Enter the movie name: ").strip().lower()
    if any(movie['title'].lower()==title for movie in movies):
        print('Movie already existed')
        return
    genre=input('Genre: ').strip().lower()
    try:
        rating=float(input('Rating(0-10): '))
        if not (0<=rating<=10):
            return   
        movies.append({'title':title,'genre':genre,'rating':rating})
        save_movies(movies)
        print('Movie added successfully✅')
    except ValueError as e:
        print('Invalid Rating')

def search_movies(movies):
    term=input('Enter the title or genre: ').strip().lower()
    found=False
    for movie in movies:
        if term in movie['title'].lower() or term in movie['genre'].lower():
            print(f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}")
            found=True
    if not found:
        print("No movies found.")
        return
    
def view_movies(movies):
    for movie in movies:
        print(f"Title: {movie['title']}, Genre: {movie['genre']}, Rating: {movie['rating']}")

def run_movie_db():
    movies=load_movies()
    while True:
        print("\nMovie Tracker Menu:")
        print("1. Add Movie")
        print("2. Search Movies")
        print("3. View All Movies")
        print("4. Exit")
        choice=input("Enter your choice: ").strip()
        if choice=='1':
            add_movies(movies)
        elif choice=='2':
            search_movies(movies)
        elif choice=='3':
            view_movies(movies)
        elif choice=='4':
            print("Exiting the Movie Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    run_movie_db()