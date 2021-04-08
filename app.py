import multiprocessing
import japronto
import orjson as json


with open("large-file.json", "r") as data:
    json_data = json.loads(data.read())


def get_headers():
    return {
        'Server': 'Japronto/0.1.1',
    }


def json_view(request):
    return request.Response(json={'hello': json_data})


def async_json(request):
    return request.Response(json={"data": json_data})


def plaintext_view(request):
    return request.Response(
        body=b'Hello, world!',
        mime_type='text/plain',
        headers=get_headers(),
    )


app = japronto.Application()
app.router.add_route('/json', json_view, 'GET')
app.router.add_route('/plaintext', plaintext_view, 'GET')
app.router.add_route('/async_json', async_json, 'GET')


if __name__ == '__main__':
    app.run('0.0.0.0', 8080, worker_num=multiprocessing.cpu_count(),
            debug=True)
