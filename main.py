import csv
from movies import movies
    
def cvsfilereader(filename):
    # opening the CSV file
  moviesList = []
  with open(filename, mode ='r')as file:
     
    # reading the CSV file
    csvFile = csv.reader(file)
    
    # displaying the contents of the CSV file
    for lines in csvFile:
      #print(lines[1]) 
      movie = movies(lines[0],lines[1],lines[3],lines[5])
      print(movie.name)
      moviesList.append(movie)

  return movies

if __name__ == '__main__':
    movies = cvsfilereader("movies.csv")