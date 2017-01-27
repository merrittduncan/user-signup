import webapp2
import re

user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
password_re = re.compile(r"^.{3,20}$")
email_re = re.compile("^[\S]+@[\S]+.[\S]+$")
page_header ="""
    <!DOCTYPE html>
    <html>
    <head>
        <title>User Signup</title>
    </head>
    <body>"""

page_footer = """
    </body>
    </html>
    """

def build_page(signup_table):
    username_input = "<tr><td>Username</td><td><input type='text' name='username'></td></tr>"

    password_input = "<tr><td>Password</td><td><input type='text' name='password'></td></tr>"

    verify_input = "<tr><td>Verify Password</td><td><input type='text' name='verify'></td></tr>"

    email_input = "<tr><td>Email (optional)</td><td><input type='text' name='email'></td></tr>"

    submit = "<input type='submit'/>"

    tableform = "<table>" + username_input + password_input + verify_input + email_input + "</table>"

    form = ("<form method='post'>" + tableform + submit + "</form>")

    header = "<h2>Signup</h2>"

    return header + form

def valid_username(username):
    return user_re.match(username)

def valid_username(password):
    return password_re.match(password)

def valid_username(email):
    return email_re.match(email)

class MainHandler(webapp2.RequestHandler):

    def get(self):
        content = build_page("")
        self.response.write(page_header + content + page_footer)

    def post(self):
        message = self.request.get('message')
        rotation = int(self.request.get('rotation'))
        encrypted_message = caesar.encrypt(message, rotation)
        escaped_message = cgi.escape(encrypted_message)
        self.response.write("Secret Message: " + encrypted_message)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
