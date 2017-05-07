from django.views import generic
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseNotFound

import json

DATA = [{'name': 'name-%s' % i, 'age': i, 'id': 'id-%s' % i} for i in range(5)]


class AjaxView(generic.View):
    def dispatch(self, request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseForbidden()
        return super(AjaxView, self).dispatch(request, *args, **kwargs)


class InfoView(AjaxView):
    def get(self, request):
        return JsonResponse({'items': DATA})

    def post(self, request):
        d = json.loads(request.body)
        DATA.append(d)
        return JsonResponse({'item': d})


class InfoDetailView(AjaxView):
    def get(self, request, p_id):
        for i in DATA:
            if i['id'] == p_id:
                return JsonResponse({'item': i})
        return HttpResponseNotFound()

    def patch(self, request, p_id):
        data = json.loads(request.body)
        data.pop('id', None)
        for i in DATA:
            if i['id'] == p_id:
                i.update(data)
                return JsonResponse({'item': i})
        return HttpResponseNotFound()

    def put(self, request, p_id):
        data = json.loads(request.body)
        data['id'] = data.get('id', p_id)
        for i in range(len(DATA)):
            if DATA[i]['id'] == p_id == data['id']:
                DATA[i] = data
                return JsonResponse({'item': DATA[i]})
        return HttpResponseNotFound()