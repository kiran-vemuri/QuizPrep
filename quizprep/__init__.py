from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('learn', '/learn')
    config.add_route('qparser', '/trivia')
    config.add_route('pebbletopics','/pebbletopics')
    config.add_route('pebbletrivia','/pebbletopics/{topic}')
    config.add_route('usertrivia','/collections/{topic}')
    config.add_route('usertopics','/collections')
    config.add_route('contact','/contact')
    config.scan()
    return config.make_wsgi_app()
