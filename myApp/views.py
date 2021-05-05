from django.shortcuts import render
from .models import Student
from myApp.forms import StudentForm
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .util import is_json
from .mixin import SerializerMixin,HttpResponesMixin
import json

@method_decorator(csrf_exempt,name='dispatch')
class AllStudent(View,SerializerMixin,HttpResponesMixin):

    def get(self,request,*args,**kwargs):
        qs=Student.objects.all()
        json_data=self.fun(qs)
        return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs):
        data=request.body
        valid=is_json(data)
        if not valid:
            json_data=json.dumps({"msg":"invalid"})
            return  self.render_to_http_response(json_data,status=404)
        p_data=json.loads(data)
        form=StudentForm(p_data)
    # to create forms with python.........    
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Resouce is created successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps({'msg':'Errors in form'})
            return self.render_to_http_response(json_data,status=404)





@method_decorator(csrf_exempt,name='dispatch')
class ParticularStudent(View,SerializerMixin,HttpResponesMixin):

    def get_rec_by_id(self,id):
        try:
            stud=Student.objects.get(id=id)
        except Exception:
            stud=None
        return stud

    def get(self,request,id,*args,**kwargs):
        try:
            stud=Student.objects.get(id=id)
        except Student.DoesNotExist:
            json_data=json.dumps({'msg':'Record not found'})
            return self.render_to_http_response(json_data,status=404)
        else:
            json_data=self.fun([stud])
            return self.render_to_http_response(json_data)


    def put(self,request,id,*args,**kwargs):
        stud=self.get_rec_by_id(id)
        if stud is None:
            json_data=json.dumps({'msg':'Invalid'})
            return self.render_to_http_response(json_data,status=404)
        data=request.body
        valid=is_json(data)
        if not valid:
            json_data=json.dumps({'msg':'Not a json data'})
            return self.render_to_http_response(json_data,status=404)
        provided_data=json.loads(data)
        original_data={'name':stud.name,'rollno':stud.rollno,'marks':stud.marks,'address':stud.address}
        original_data.update(provided_data)
        form=StudentForm(original_data,instance=stud)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Updation is successful'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps({'msg':'Error in form submission'})
            return self.render_to_http_response(json_data,status=404)

    def delete(self,request,id,*args,**kwargs):
        stud=self.get_rec_by_id(id)
        if stud is None:
            json_data=json.dumps({'msg':'Invalid'})
            return self.render_to_http_response(json_data,status=404)
        status,item=stud.delete()
        if status==1:
            print("succesfully deleted:")
            json_data=json.dumps({'msg':'succesfully deleted'})
            return self.render_to_http_response(json_data,status=210)
        else:
            print("unable to delete")