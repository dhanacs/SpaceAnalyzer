import os
from dropbox.client import DropboxClient, DropboxOAuth2FlowNoRedirect
from flask import Flask, render_template, request, session, redirect, url_for

from SpaceAnalyzer import helperMethods
from SpaceAnalyzer import sqlMethods
from helperMethods import BFS, spaceUsage, getFileTypeSizes, getColors, getSecretKey
from sqlMethods import saveToDB, retrieveFromDB, searchInDB

app = Flask(__name__)

# Authorization page
@app.route('/', methods = ['GET'])
def index():
    if 'errorLabel' not in session:
        return render_template("main.html")
    else:
        return render_template("main.html", error = session["errorLabel"])

# Account info page
@app.route('/account', methods = ['GET', 'POST'])
def account():
    # Logout
    if request.args.get('logout') is not None:
        session.clear()
        return redirect(url_for('index'))

    # Save the token in session
    if 'accessToken' not in session:
        session['accessToken'] = request.form["accessToken"]

    # Get the account metadata
    try:
        accessToken = session['accessToken']
        client = DropboxClient(accessToken)
        accountInfo = client.account_info()
        session["userID"] = accountInfo["uid"]
        return render_template("account.html", accountInfo = accountInfo)
    except:
        session.clear()
        if not accessToken:
            session["errorLabel"] = "0"
        else:
            session["errorLabel"] = "1"
        return redirect(url_for('index'))

# Process files
@app.route('/process', methods = ['GET', 'POST'])
def process():
    # Save file metadata to DB for the first time
    if 'accessToken' not in session:
        session.clear()
        return redirect(url_for('index'))
    elif 'cached' not in session:
        client = DropboxClient(session['accessToken'])
        folderMetadata = client.metadata('/')
        contents = folderMetadata["contents"]
        names = []; types = []; sizes = []; paths = [];
        BFS(client, contents, names, types, sizes, paths)
        saveToDB(session["userID"], names, types, sizes, paths)
        session["cached"] = 1

    # File Search from search page
    if request.method == 'POST':
        keyWord = request.form["keyword"]
        paths = []; sizes = []
        searchInDB(session["userID"], paths, sizes, keyWord)
        data = sorted(zip(sizes, paths))
        searchCount = len(paths)
        return render_template("search.html", data = data, searchCount = searchCount)

    # Button clicks from account page
    if request.args.get('list') is not None:
        names = []; types = []; sizes = []
        retrieveFromDB(session["userID"], types, sizes, names)
        data = sorted(zip(types, sizes, names))
        return render_template("files.html", data = data)
    elif request.args.get('filesearch') is not None:
        return render_template("search.html")
    elif request.args.get('analyze') is not None:
        names = []; types = []; sizes = []
        retrieveFromDB(session["userID"], types, sizes, names)
        used, free = spaceUsage()
        types, totalSizes = getFileTypeSizes(names, sizes)
        colors = getColors(len(types))
        data = sorted(zip(totalSizes, colors, types))
        return render_template("analysis.html", used = used, free = free, rows = data)
    else:
        session.clear()
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.secret_key = getSecretKey()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)