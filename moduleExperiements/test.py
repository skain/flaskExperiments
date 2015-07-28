import swift.application.users
import simplejson as json

u = swift.application.users.SwiftUser()
u.email = 'email@gmail.com'
u.user_name = 'jdoe'
print json.dumps(u.__dict__)