from django.core.serializers import serialize
from django.http import HttpResponse
import json
class SerializerMixin(object):
    def fun(self,qs):
        json_data=serialize('json',qs)
        pdata=json.loads(json_data)
        final_list=[]
     #filter the unwanted data
        for ob in pdata:
            required_info=ob['fields']
            final_list.append(required_info)
        json_data=json.dumps(final_list)
        return json_data    

class HttpResponesMixin(object):
    def render_to_http_response(self,json_data,status=200):
        return HttpResponse(json_data,content_type='application/json',status=status)
