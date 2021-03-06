import cgi
import urllib

from google.appengine.api import users
# [START import_ndb]
from google.appengine.ext import ndb
# [END import_ndb]

import webapp2

MAIN_PAGE_FOOTER_TEMPLATE = """\
    <form action="/sign?%s&%s" method="post">
      <div><textarea name="content" rows="3" cols="60"></textarea></div>
      <div><input type="submit" value="Sign Guestbook"></div>
    </form>
    <hr>
    <form>
      <p>Guestbook name: <input value="%s" name="guestbook_name"></p>
      <p>Guest name: <input value="%s" name="na"></p>
      <input type="submit" value="switch">
    </form>
    <a href="%s">%s</a>
  </body>
</html>
"""

DEFAULT_GUESTBOOK_NAME = 'defaul_guestbook'
DEFAULT_GUEST_NAME = 'defaul_user'

# We set a parent key on the 'Greetings' to ensure that they are all
# in the same entity group. Queries across the single entity group
# will be consistent.  However, the write rate should be limited to
# ~1/second.

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
    """Constructs a Datastore key for a Guestbook entity.
    We use guestbook_name as the key.
    """
    return ndb.Key('Guestbookv2', guestbook_name)


# [START greeting]
class Author(ndb.Model):
    """Sub model for representing an author."""
    identity = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)
    name = ndb.StringProperty(indexed=False)


class Greetingv2(ndb.Model):
    """A main model for representing an individual Guestbook entry."""
    author = ndb.StructuredProperty(Author)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
# [END greeting]


# [START main_page]
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('''<html><body><div>''')
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        guest_name = self.request.get('na',DEFAULT_GUEST_NAME)
        # Ancestor Queries, as shown here, are strongly consistent
        # with the High Replication Datastore. Queries that span
        # entity groups are eventually consistent. If we omitted the
        # ancestor from this query there would be a slight chance that
        # Greeting that had just been written would not show up in a
        # query.
        # [START query]
        greetings_query = Greetingv2.query(
            ancestor=guestbook_key(guestbook_name)).order(+Greetingv2.date)
        greetings = greetings_query.fetch(100)
        # [END query]

        user = users.get_current_user()
        for greeting in greetings:
            if greeting.author:
                author = greeting.author.email
                name = greeting.author.name
                if user and user.user_id() == greeting.author.identity:
                    author += ' (You)'
                else:
                    author = name
                self.response.write('<b>%s</b> wrote:' % author)
            
            else:
                self.response.write('user <b>%s</b> wrote:' % name)

            self.response.write('<blockquote>%s</blockquote>' %
                                cgi.escape(greeting.content))
        self.response.write('''</div>''')
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        # Write the submission form and the footer of the page
        sign_query_params = urllib.urlencode({'guestbook_name':
                                              guestbook_name})
        sign_query_params2 = urllib.urlencode({'na':guest_name})
        self.response.write(MAIN_PAGE_FOOTER_TEMPLATE %
                            (sign_query_params, sign_query_params2, cgi.escape(guestbook_name),cgi.escape(guest_name),
                             url, url_linktext))
# [END main_page]

# [START guestbook]
class Guestbook(webapp2.RequestHandler):
    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each
        # Greeting is in the same entity group. Queries across the
        # single entity group will be consistent. However, the write
        # rate to a single entity group should be limited to
        # ~1/second.
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        guest_name = self.request.get('na',DEFAULT_GUEST_NAME)
        greeting = Greetingv2(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = Author(identity=users.get_current_user().user_id(), email=users.get_current_user().email(), name=users.get_current_user().email())
        else:
            greeting.author = Author(identity='0',email="No-email",name=guest_name)
        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name,'na':guest_name}
        self.redirect('/?' + urllib.urlencode(query_params))
# [END guestbook]

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
], debug=True)
