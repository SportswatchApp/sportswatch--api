import os

from sportswatch import settings


def build_usecase(options):
    files = {
        'listener.py': 'from app.usecases import listener'
                       '\n\n\nclass Listener(listener.Listener, listener.SuccessListener):\n    pass\n',
        'usecase.py': 'class ' + options["type"] + ':\n    pass\n',
    }

    path = os.path.join(settings.BASE_DIR, 'app', 'usecases', options['name'])
    os.mkdir(path, 0o700)
    init_file = os.path.join(path, '__init__.py')
    file = open(init_file, "a")
    file.write('from .usecase import ' + options["type"] + '\nfrom .listener import Listener\n')
    if options['request']:
        files['request.py'] = 'from app.usecases import request\n\n\nclass Request(request.Request):\n    pass\n'
        file.write('from .request import Request\n')

    for filename in files:
        p = os.path.join(path, filename)
        file = open(p, 'a')
        file.write(files[filename])
