import web
import db
import config

t_globals = dict(
  datestr=web.datestr,
)
render = web.template.render('templates/', cache=config.cache, 
    globals=t_globals)
render._keywords['globals']['render'] = render

def listing(**k):
    l = [{created: "2013-1-2", body: "Hello"}, {created: "2013-1-3", body: "World"}]
    return render.listing(l)