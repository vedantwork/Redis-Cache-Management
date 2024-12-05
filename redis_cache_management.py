from time import time_ns
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.core.cache import cache
import json,requests,base64
from restapi.common_func import commonfunc
from django.http import HttpResponse,JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import traceback
import datetime


# setdata finction
# In setdata(), when the user hits any specific api the response comes for the server and gets
# stored into the cache, on the second time when the api is hit the data will come from the cache instead of the server
 
# getdata finction
# In getdata() the api response will come frfom the store cache instead of the server, which will indireclty reduce the response time 

# deletedata finction
# In deletedata() the cache will get deleted as soon as the user clicks on view report button or calls /restapi/report/getreportdata/ api


class redisCacheManagement():
    @classmethod
    @csrf_exempt
    def setredisdata(self,request):
        encrypt = 0
        try:
            if request.method == 'POST':
                try:
                    data = json.loads(request.body.decode('utf-8'), strict=False)
                except Exception as e:
                    data = data
                # current_time = datetime.datetime.now()
                # time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                # data['cachetime']= time
                cache.set(data['key'],data['value'],timeout=3888000)  #3888000 = 45 days (The cache will be stored for 45 days in redis)
                data=cache.get(data['key'])
                response = {"message":"success","error_code":"100","data":data}
                if encrypt == 1:
                    response = commonfunc.b64encode(json.dumps(response, sort_keys=True, indent=1, cls=DjangoJSONEncoder))
                return JsonResponse(response,safe=False)
            else:
                response = {'message': 'invalid method','error_code': '104','data': {}}
                if encrypt == 1:
                    response = commonfunc.b64encode(json.dumps(response, sort_keys=True, indent=1, cls=DjangoJSONEncoder))
                return JsonResponse(response,safe=False)
        except Exception as e:
                return JsonResponse({"error_code":"103","data":'',"message":traceback.format_exc()},safe=0)


    @classmethod
    @csrf_exempt
    def getredisdata(self,request):
        encrypt = 0
        try:
            if request.method == 'POST':
                try:
                    data = json.loads(request.body.decode('utf-8'), strict=False)
                except:                 
                    encrypt = 1
                    encoded_string = request.body.decode('utf-8')
                    req = commonfunc.b64decode(encoded_string)
                    data = json.loads(req, strict=False)
                if cache.get(data['key']):  
                    data=cache.get(data['key'])         
                    # print("Time Remaining ===>>> ",cache.pttl(data['key'])) 
                    if "group_data" in data:            
                        response = {"message":"success","error_code":"100","data":data['data'],'group_data':data['group_data']}
                        if encrypt == 1:
                            response = commonfunc.b64encode(json.dumps(response, sort_keys=True, indent=1, cls=DjangoJSONEncoder))
                        return JsonResponse(response,safe=False)
                else:
                    response = {"message":"data not found ","error_code":"102","data":{}}
                    if encrypt == 1:
                        response = commonfunc.b64encode(json.dumps(response, sort_keys=True, indent=1, cls=DjangoJSONEncoder))
                    return JsonResponse(response,safe=False)
            else:
                response = {'message': 'invalid method','error_code': '104','data': {}}
                if encrypt == 1:
                    response = commonfunc.b64encode(json.dumps(response, sort_keys=True, indent=1, cls=DjangoJSONEncoder))
                return JsonResponse(response, safe=False)
        except Exception as e:
            return JsonResponse({"error_code":"103","data":'',"message":traceback.format_exc()},safe=0)

    @classmethod
    @csrf_exempt
    def deleteredisdata(self,request):
        if request.method == 'POST':
            try:
                encrypt = 0
                try:
                    data = json.loads(request.body.decode('utf-8'), strict=False)
                except:
                    encrypt = 1
                    encoded_string = request.body.decode('utf-8')
                    req = commonfunc.b64decode(encoded_string)
                    data = json.loads(req, strict=False)            
                for i in data:
                    print("Redis key's ===>>>> ",i)        # will print all the keys by which the cache data is being stored
                    cache.expire(i, timeout=1)  
                response = {"message":"sccess","error_code":"100","data":data}
                if encrypt == 1:
                    response = commonfunc.encrypt(json.dumps(response))
                return JsonResponse(response, safe=False)
            except Exception as e:
                return JsonResponse({"error_code":"103","data":'',"message":traceback.format_exc()},safe=0)
        else:
            response = {'message': 'invalid method','error_code': '104','data': {}}
            return JsonResponse(response, safe=False)





            # Add this in the start of your code
            
            # user_id = data['user_id']
            # fp_log_id = data['fp_log_id']
            # NOTE-- getting data from Redis cache--  
              
            # rp_user_id = data['user_id']
            # redis_geturl = reverse('getredisdata')
            # redis_geturl_postdata = {"key":"your_key_name"+"_"+str(rp_user_id)}
            # redis_getapicall = requests.post(urls.BASE_URL[:-1]+redis_geturl, data=json.dumps(redis_geturl_postdata))
            # redis_get_data = redis_getapicall.json()

            # response ={}
            # if "error_code" in redis_get_data:
            # 	if redis_get_data['error_code'] == '100':
            # 		response = redis_get_data
            # else:
            # 	redis_get_data = commonfunc.decrypt(redis_get_data)
            # 	response = json.loads(redis_get_data)
            # 	if response['error_code'] == '100':
            # 		response = response
            # if response:
            # 	if encrypt == 1:
            # 		response = commonfunc.encrypt(json.dumps(response))
            # 	return JsonResponse(response,safe=False)
            
            
            


            # Add this at the end of your code  
            
            # set_redis_url = reverse('setredisdata')						
            # set_redis_posteddata = {"key":"your_key_name"+"_"+str(rp_user_id),"value":response}
            # set_redis_api_call = requests.post(urls.BASE_URL[:-1]+set_redis_url, data=json.dumps(set_redis_posteddata,default=str))
            # set_redis_data = set_redis_api_call.json()   
            # if encrypt == 1:
            # 	response = commonfunc.encrypt(json.dumps(response,default=str))
            # return JsonResponse(response,safe=False)
        
