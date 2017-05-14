from django.views import generic
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponse
from django.forms.models import model_to_dict

from scan.models import Template

import json, logging, random

DATA = [{'name': 'name-%s' % i, 'age': i, 'id': 'id-%s' % i} for i in range(5)]

_logger = logging.getLogger(__name__)


class AjaxView(generic.View):
    def dispatch(self, request, *args, **kwargs):
        if not request.is_ajax():
            _logger.debug('request without ajax, return 403 Forbidden')
            return HttpResponseForbidden()
        return super(AjaxView, self).dispatch(request, *args, **kwargs)


class InfoView(AjaxView):
    def get(self, request):
        t_obj = Template.objects.all().order_by('-id')[:10]
        _logger.debug('get info list view')
        data = [model_to_dict(i) for i in t_obj]
        return JsonResponse({'items': data})

    def post(self, request):
        d = json.loads(request.body)
        d['status'] = d.get('status', random.choice(['ld', 'ac']))
        _logger.info('create a new info')
        a = Template.objects.create(**d)
        return JsonResponse({'item': model_to_dict(a)})


class InfoDetailView(AjaxView):
    def get(self, request, p_id):
        a = Template.objects.get(pk=p_id)
        _logger.debug('get detail of %r' % a)
        return JsonResponse({'item': model_to_dict(a)})

    def delete(self, request, p_id):
        Template.objects.get(pk=p_id).delete()
        _logger.info('delete obj of Template<id: %s>' % p_id)
        return HttpResponse(status=204)

    def patch(self, request, p_id):
        data = json.loads(request.body)
        data['id'] = data['id'] or p_id
        a = Template(**data)
        a.save()
        _logger.info('update object %r' % a)
        return JsonResponse({'item': model_to_dict(a)})

    def put(self, request, p_id):
        return self.patch(request, p_id)
