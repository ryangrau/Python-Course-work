 
epic_programmer_dict = {'tim berners-lee' : ['tbl@gmail.com', 111],
                        'guido van rossum' : ['gvr@gmail.com', 222],
                        'linus torvalds' : ['lt@gmail.com', 333],
                        'sergey brin' : ['sb@gmail.com', 444],
                        'larry page' : ['lp@gmail.com', 555]
                        }


def searchPeople(personsName):
        try:
            personsInfo = epic_programmer_dict[personsName]
            print 'Name: ' + personsName.title()
            print 'Email: ' + personsInfo[0]
            print 'Number: ' + str(personsInfo[1])
        except:
            print 'No information found for that name'


userWantsMore = True
while userWantsMore == True:
        personsName = raw_input('please enter a name: ').lower()
        userWantsMore = False

searchAgain = raw_input('Search again? (y/n) ')
if searchAgain == 'y':
    userWantsMore = True
elif searchAgain == 'n':
    userWantsMore = False
else:
    print "I don't understand what you mean, quitting"
    userWantsMore = False
    
