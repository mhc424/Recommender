'''
Created on Dec 7, 2016

@author: Monica
'''

import BookReader
import MovieReader
import Recommender

def main_model():
    recommendations = []
    user = str(raw_input("Enter the user that you would like recommendations for: "))
    num_comp = input("Enter the number of users that you would like to use for comparison: ")
    
    rating_type = input("Is this for books or movies? 1 = books, 2 = movies ")

#     while rating_type !=  1 or rating_type !=2:
#         print "Invalid input. Please try again"
#         rating_type = int(raw_input("Is this for books or movies? 1 = books, 2 = movies "))
#         
    get_avg = input("Would you like the average rating of the items as well? 0 = no, 1 = yes")
#     while get_avg != 0 or get_avg !=1:
#         print "Invalid input. Please try again"
#         get_avg = int(raw_input("Would you like the average rating of the items as well? 0 = no, 1 = yes"))
#     
    items = []
    ratings = {}  
    if rating_type == 1:
        items, info, ratings = BookReader.get_data("books.txt", "bookratings.txt")
    
        
    elif rating_type == 2:
        items, ratings = MovieReader.get_data("movieratings.txt")
    recommendations = Recommender.recommended(items, ratings, num_comp, user.strip())
    
    if get_avg == 1:
        print Recommender.averages(items, ratings)
    else:
        pass
    
    return recommendations

main_model()