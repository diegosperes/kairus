from sanic.response import json

from kairus.application import app
from kairus.models.event import Event
from kairus.tasks import mapping


@app.route('/events', methods=['POST'])
def slack_events(request):
    data = {}
    try:
        event = Event(request.json)
        task = mapping.get(event.type)
        data = task(event)
    except Exception:
        pass

    return json(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
