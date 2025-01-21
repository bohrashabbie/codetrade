import requests
import ast

# Make a request to the API
response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=aaa7de53dcab3a19afed86880f364e54&language=en-US&page=1')

# Parse the response as a string into a Python dictionary using ast.literal_eval()
response_text = response.text
response_dict = ast.parse(response_text)

# Initialize lists to store the data
id = []
title = []
overview = []
release_date = []
popularity = []
vote_average = []
vote_count = []

# Loop through the results and extract the required data
for i in response_dict['results']:
    id.append(i['id'])
    title.append(i['title'])
    overview.append(i['overview'])
    release_date.append(i['release_date'])
    popularity.append(i['popularity'])
    vote_average.append(i['vote_average'])
    vote_count.append(i['vote_count'])

# Create a dictionary with the extracted data
dictionary = {'title': title,'id': id,'overview': overview,'release_date': release_date,'popularity': popularity,'vote_average': vote_average,'vote_count': vote_count
}

# Print the dictionary
print(dictionary)
