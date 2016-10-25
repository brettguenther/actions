from flask import Flask, request, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'


@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/hello')
def hello():
    return 'Hello, World'

# url: https://example.com/ping/{{ value }}
# form_url: https://example.com/ping/{{ value }}/form.json

@app.route("/zendesk/", methods=['GET', 'POST'])
def zendesk():
    import json
    if request.method == 'POST':
        # content = request.get_json()
        data = request.data
        dataDict = json.loads(data)
        post_info = dataDict
    else:
        post_info = "not a post"
    target = open("log_testing.txt", 'w')
    target.write(post_info)
    return "completed zd method"
    # return render_template("index.html",
    #                             req_info = post_info)

@app.route("/ping_test", methods=['GET', 'POST'])
def ping_test():
    qs = request.args.get("q")
    target = open("log_testing.txt", 'w')
    target.write(qs)
    return "completed ping method"

if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id
