#Excercise 1 
def triple(a):
    x=a*3
    return x
result=triple(4)
print(result)
#Exercise 2
def subtract(a,b):
    x=b-a
    return x
result=subtract(3,6)
print(result)

#Exercise 3
list_tuple=[('cat',3),('dog',5.1)]
def dictionary_maker(list_tuple):
    dictionary={}
    for key, value in list_tuple:
        dictionary[key]=value
    return dictionary
result=dictionary_maker(list_tuple)
print(result)  

#Exercise 4
# Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}
# e.g. [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]
# we will refer to this as a "CV".

def has_experience_as(list_cv,job_title):
    result=[]
    for x in list_cv:
        if job_title in x['jobs']:
            result.append(x['user'])
    return result

cv= [{'user': 'john', 'jobs': ['analyst', 'engineer']},
      {'user': 'jane', 'jobs': ['finance', 'software']},
      {'user':'jessica', 'jobs':['finance','analyst']}]
finance_people=has_experience_as(cv, 'finance')
print(finance_people)


#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.
def job_counts(cv_data: list[dict]) -> dict:
    result = {}
    for cv in cv_data:
        for job in cv["jobs"]:
            if job in result:
                result[job] += 1
            else:
                result[job] = 1
    
    return result

print(job_counts(cv_data=[{'user': 'john', 'jobs': ['analyst', 'engineer']}, 
                          {'user': 'jane', 'jobs': ['finance', 'software']},
                          {'user': '1', 'jobs': ["cowbreeder"]},
                          {'user': '2', 'jobs': ['finance',]},
                          {'user': '3', 'jobs': ['software']}]))



#
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.
def most_popular_job(cv_data: list[dict]):
    counts = job_counts(cv_data=cv_data)

    return max(counts.items(), key=lambda i: i[1])

print(most_popular_job(cv_data=[{'user': 'john', 'jobs': ['analyst', 'engineer']}, 
                          {'user': 'jane', 'jobs': ['finance', 'software']},
                          {'user': '1', 'jobs': ["cowbreeder"]},
                          {'user': '2', 'jobs': ['finance',]},
                          {'user': '3', 'jobs': ['finance']}]))

# 7)
def total_registered_cases(covid_cases,country):
    for key, value in covid_cases.items():
        if country == key:
            return sum(value)
    else:
        return 'No such country registered'

covid={'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
       'Italy': [6, 8, 1, 7]}
cases=total_registered_cases(covid,'Spain')
print(cases)


##############

# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus
# the length of the lists can differ)


# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country

# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#

def total_registered_cases_per_country(data: dict):
    return {k: sum(v) for k, v in data.items()}

# print(total_registered_cases_per_country(data={'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}))


# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases

def country_with_most_cases(data: dict):
    return max(data, key=lambda i: sum(data[i]))

# print(country_with_most_cases(data={'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6], 'Italy': [6, 8, 1, 7]}))



###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #