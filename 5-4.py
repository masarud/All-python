me = {
    "height":"6",
    "fav_colors":"green",
    "fav_author":"tanaka"
}

answer = input("Type height, fav_color or fav_author")
if answer in me:
    result = me[answer]
    print(result)