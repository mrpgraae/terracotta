from typing import Any

from flask import Flask, render_template, current_app, Blueprint

client_api = Blueprint('client_api', 'terracotta.client')


@client_api.route('/', methods=['GET'])
def get_map() -> Any:
    return render_template(
        'map.html', hostname=current_app.config['terracotta_hostname']
    )


def create_app(hostname: str) -> Flask:
    client_app = Flask('terracotta.client')
    client_app.config['terracotta_hostname'] = hostname
    client_app.register_blueprint(client_api)
    return client_app


def run_app(hostname: str, port: int = 5100) -> None:
    create_app(hostname).run(port=port)
