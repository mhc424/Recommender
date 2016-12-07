'''
Created on Dec 6, 2016

@author: Monica
'''

def get_data(movieratings):
    
    movies = []
    d = {}
    
    f = open(movieratings)
    for row in f:
        info = row.split()
        user = info[0]
        movie = info[1]
        rating = info[2]
        if movie not in movies: 
            movies.append(movie)
    f.close()
    f2 = open(movieratings)
    for row in f2:
        info = row.split()
        user = info[0]
        movie = info[1]
        rating =int(info[2])
        
        if user not in d:
            d[user] = [0]*len(movies)
        d[user][movies.index(movie)] = rating
    f2.close()   
    return movies, d