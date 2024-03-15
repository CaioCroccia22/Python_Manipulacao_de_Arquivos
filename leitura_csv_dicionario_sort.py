courses = []

with open("dados/courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.rstrip().split(",")
        course = {}
        #  Dicionario nesse caso vai ficar dentro de uma lista
        course["language"] = language
        course["category"] = category
        courses.append(course)

def get_language(course):
    return course["language"]

def get_category(course):
    return course["category"]


# Ordena pelas linguagens
for course in sorted(courses, key=get_language):
    print(f"{course['language']} - {course['category']}")

#Para colocar em descrescente so colocar 

# Não funciona pq a chave esta igual a none
# for course in sorted(courses):
#     print(f'{course["language"]} - {course["category"]}')