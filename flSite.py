from flask import Flask, render_template,request
import sqlite3
import os



app= Flask(__name__)



def get_list_employees():
    result=[]
    x = open("phoneBook.txt", "r", encoding="UTF-8")
    list = x.read().split("|")
    for y in list:
        person = y.split(";")
        result.append(person)
    return result

def search_by_initials(search,param="all"):

    listEmplyees = get_list_employees()
    searchResult = []
    search = search.encode()
    search = search.decode("utf-8").strip().lower()
    for x in listEmplyees:
        y = x[0].split(" ")
        if param == "all":
            for z in y:
                if z == '':
                    continue
                z = z.lower()
                if z.startswith(search):
                    searchResult.append(x)

        else:
            if y[0] == '':
                continue
            z = y[0].lower()
            if z.startswith(search):
                searchResult.append(x)
        searchResult = searchResult

    if searchResult == [] or search == "":
        searchResult = listEmplyees
    return  searchResult

@app.route("/",methods=['GET', 'POST'])
def index():
    result=get_list_employees()
    return render_template('index.html',list=result)


@app.route("/search/",methods=['GET', 'POST'])
def search():
    alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
                'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

    input=search_by_initials(str(request.args.get('search')))
    return render_template('search.html',search=input,alphabet=alphabet)


def alphabet():
    alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
                'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

    input = search_by_initials(str(request.args.get('search')),param='firstname')
    return render_template('template.html', search=input, alphabet=alphabet)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=80)
