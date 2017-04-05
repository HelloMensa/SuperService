import web
import view, config
from view import render

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return render.base(view.listing())

if __name__ == "__main__":
	web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()