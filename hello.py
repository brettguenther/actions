from flask import Flask, request, render_template, url_for, json
app = Flask(__name__)
import os

#getting environment variables
# os.getenv('KEY_THAT_MIGHT_EXIST', default_value)

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
        dataDict = json.dumps(data)
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

@app.route("/github_issue", methods=['GET', 'POST'])
def github_issue():
    import requests
    import json
    owner = os.environ['GITHUB_USER']
    github_base_url = os.environ['GITHUB_BASE_URL']
    auth_token = os.environ['GITHUB_TOKEN']
    repo = 'test'
    # if request.method == 'POST':
    #     data = request.data
    #     dataDict = json.dumps(data)
    #     if dataDict == '':
    #         #this is the intitial form call to get back params
    #
    #     else:
    #           #this is the case where the body contains contents of the form post
    #
    #
    # else:
    # from base_functions import ConfigSectionMap
    # github_info = ConfigSectionMap('/Users/Looker/looker_apps/actions/look_creds.ini','github')
    # owner = github_info['github_user']
    # github_base_url = github_info['github_base_url']
    # auth_token = github_info['github_token']
    label = request.args.get("label")
    labels_array = [label]
    issue_number = request.args.get("issue_number")
    github_issues_url = github_base_url + '/repos/{0}/{1}/issues'.format(owner,repo)
    github_labels_url = github_base_url + '/repos/{0}/{1}/issues/{2}/labels'.format(owner,repo,issue_number)
    r = requests.post(github_labels_url,auth=(owner, auth_token),data=json.dumps(labels_array))
    return r.text

@app.route("/github_form", methods=['GET', 'POST'])
def github_form():
    dat = [
        {'Name': 'Title', 'required': true, 'default':'test title'},
        {'Name': 'Comment', 'required': true, 'default':'test comment'}
    ]
    resp = Response(response=dat,status=200,mimetype="application/json")
    return(resp)

@app.route("/github_comment", methods=['GET', 'POST'])
def github_comment():
    import requests
    import json
    owner = os.environ['GITHUB_USER']
    github_base_url = os.environ['GITHUB_BASE_URL']
    auth_token = os.environ['GITHUB_TOKEN']
    repo = 'test'
    content = request.get_json()
    post_comment = content['form_params']['comment']#need to extract comment from post body in looker form
    print post_comment
    issue_number = request.args.get("issue_number")
    comment_body = {"body": post_comment}
    github_issue_comments_url = github_base_url + '/repos/{0}/{1}/issues/{2}/comments'.format(owner,repo,issue_number)
    r = requests.post(github_issue_comments_url,auth=(owner, auth_token),data=json.dumps(comment_body))
    return r.text

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
