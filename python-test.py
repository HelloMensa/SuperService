import os
 
def application(env, start_response):
    os.chdir('/usr/local/src/python-test')
    retcode = os.system('sh dir.sh')
    if retcode == 0:
        ret = 'success!'
    else:
        ret = 'failure!'
        start_response('200 OK', [('Content-Type','text/html')])
    return [ret]