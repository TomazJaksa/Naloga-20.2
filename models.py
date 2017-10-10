from google.appengine.ext import ndb

class Guestbook(ndb.Model):
	name =  ndb.StringProperty()
	surname = ndb.StringProperty()
	email = ndb.StringProperty()
	message = ndb.TextProperty()
	nastanek = ndb.DateTimeProperty(auto_now_add=True)
	deleted = ndb.BooleanProperty(default=False)
