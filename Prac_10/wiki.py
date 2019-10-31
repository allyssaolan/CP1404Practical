import wikipedia

# wikipedia.search("Monty")
# wikipedia.summary("Monty")
search = input("Search: ")
while search != " ":
    try:
        print(wikipedia.summary(search))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    new_page = wikipedia.page(search)
    print(new_page.url)
    print(new_page.title)
    search = input("Search: ")

# wikipedia.page("Monty")
