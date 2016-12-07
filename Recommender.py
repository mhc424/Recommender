'''
Created on Dec 6, 2016

@author: Monica
'''

import operator
import BookReader
import MovieReader

def averages(items, ratings):
    avg = []
    for i, item in enumerate(items):
        all_ratings = [rating[i] for rating in ratings.values() if rating[i] != 0]
        rating_avg = sum(all_ratings)/float(len(all_ratings))
        avg.append((item, rating_avg))
    return sorted(avg, key=operator.itemgetter(1), reverse = True)
    
def similarities(name, ratings):
    similarity = []
    user_rating = ratings[name]
    print user_rating
    for key, value in ratings.items():
        if key != name: 
            sim_rate = sum([user_rating[j] * value[j] for j in range(len(value))])
            similarity.append((key, sim_rate))        
    return sorted(similarity, key = operator.itemgetter(1), reverse = True)
    

def recommended(items, ratings, n, cur_user):
    recommendations = []
    usable_users = similarities(cur_user, ratings)[0:n]
    for i, val in enumerate(items):
        if ratings[cur_user][i] == 0:
            title = val
            weighted_rating = sum([ratings[user][i]*sim_score for (user, sim_score) in usable_users])
            recommendations.append((title, weighted_rating))
        
    return sorted(recommendations, key = operator.itemgetter(1), reverse = True) 

items, ratings = MovieReader.get_data("movieratings.txt")
print recommended(items, ratings, 10, "student1246")
    