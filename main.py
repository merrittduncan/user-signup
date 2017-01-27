#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2

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

class MainHandler(webapp2.RequestHandler):

    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):
        message = self.request.get('message')
        rotation = int(self.request.get('rotation'))
        encrypted_message = caesar.encrypt(message, rotation)
        escaped_message = cgi.escape(encrypted_message)
        self.response.write("Secret Message: " + encrypted_message)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
