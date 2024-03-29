from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response, xResponse


def hello_world(request):
    print('Incoming request')
    return xResponse('<body><h1>Hello World!</h1></body>')

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    return config.make_wsgi_app()
