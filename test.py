import requests
from bs4 import BeautifulSoup
import webbrowser

def perform_google_search(query):
    # Create a Google search URL with the provided query
    search_url = f"https://www.google.com/search?q={query}"

    try:
        # Send an HTTP GET request to the search URL
        response = requests.get(search_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the search results page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract and print the titles and links of the search results
            search_results = soup.find_all('h3', class_='t')
            for i, result in enumerate(search_results, start=1):
                title = result.text
                url = result.a['href']
                print(f"{i}. {title}\n{url}\n")

            # Open the first search result in the default web browser
            if search_results:
                first_result_url = search_results[0].a['href']
                webbrowser.open("https://www.google.com" + first_result_url)
        else:
            print(f"Failed to retrieve search results. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Get a user-provided query
user_query = input("Enter your search query: ")

# Perform the Google search
perform_google_search(user_query)
