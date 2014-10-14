# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 21:40:32 2014

This program will taken in a Facebook user's username, determine the userid
associated with the user, and use that to download a hardcoded number of
posts from the user's wall. Based on the total number of likes and comments,
these posts will be sorted for "popularity". The hardcoded number of most
popular posts will have its words analyzed for polarity and subjectivity.

@author: elena
"""

from pattern.web import URL, strip_between, Facebook, NEWS, COMMENTS, LIKES
from pattern.en import sentiment

# Based on username input, go find out the id number facebook has
# assigned to this user.
def find_id():
    idlink = URL('http://graph.facebook.com/' + userid).download()
    #idlink = URL('http://graph.facebook.com/lilian.xie?fref=ts').download()
    idlink = idlink[7:]
    idnum = strip_between('"', '}', idlink)     
    return idnum

# Based on username input, identify the user's Facebook name by eliminating
# all other information.
def find_name():
    idlink = URL('http://graph.facebook.com/' + userid).download()    
    #idlink = URL('http://graph.facebook.com/lilian.xie?fref=ts').download()
    name = strip_between('{', '"name":"', idlink)     
    name = strip_between('","user', '}', name)
    return name
   
# Go download "pullnum"-number of posts from the user's wall and for all posts
# that are not about the user's activities (changed cover photo, went 
# to an event etc.), calculate its popularity and store the score with
# the corresponding post content.
def find_news():
    fb = Facebook(license='CAAEuAis8fUgBAAZB8tJX5T9qPXpFolTmCpFQNMZBHoHuGpwuhjHYUwyIHR2Xm9lENwbewkSwM0NS3sZBXJGFcOUeiwUYBKxWqtbDnfxMzmAOfI0s48bjXjKKYZB2eSvnZBMLA0iz1HeZCMHPFNxgaqhEufsZAzQuwT4bqQ77YFz426lH1YEZCJcJ', throttle=1.0, language='en')
    person = fb.profile(id=find_id())
    postkey=()    
    posts=[]    
    
    for post in fb.search(person['id'], type=NEWS, count=pullnum):
        if find_name() not in post.text: 
            popularity = post.comments + post.likes             
            postkey = (popularity, post.text)
            posts.append(postkey)
    return posts

 
#---------------progam starts here-----------------#

# Insert the number of posts to be downloaded as well as the cut off 
# of the popularity score          
pullnum = 50    #enter integer value 5-200
popscore = 20   #enter integer value 5- 30
score = []
userid = raw_input('Enter username:') 

#store ranked scores and posts as tuples
sort = sorted(find_news(), reverse=True)


# For all sorted posts, determine if its popularity score is high enough,
# if they are, run a polarity-subjectivity text analysis on the post 
# content and print the results. If symbols in the post create a 
# problem for the text analysis function, tell me it went wrong and 
# print the post.
for i in sort:
    if i[0]>popscore:    
        try:
            score = sentiment(str(i))
            polarity = round(score[0],3) #round the score to 3 decimals max.
            subjectivity = round(score[1],3)
            print '\n'
            print 'Score:' , i[0]
            print str(i[1])
            print 'Polarity: ', polarity
            print 'Subjectivity: ', subjectivity
        except:
            print 'ERROR!!'+ str(i)
    


