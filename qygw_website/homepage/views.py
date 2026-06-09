from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import os
from .models import Kehu
import json

def index(request):
    vue_index_path = os.path.join(settings.BASE_DIR, 'frontend', 'index.html')
    if os.path.exists(vue_index_path):
        with open(vue_index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return HttpResponse(content, content_type='text/html')
    return render(request, 'homepage/index.html')

@csrf_exempt
def submit_contact(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            
            kehu = Kehu(
                name=data.get('name', ''),
                phone=data.get('phone', ''),
                email=data.get('email', ''),
                company=data.get('company', ''),
                inquiry_type=data.get('inquiry_type', ''),
                message=data.get('message', '')
            )
            kehu.save()
            
            return JsonResponse({
                'success': True,
                'message': '留言提交成功！'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'提交失败：{str(e)}'
            })
    else:
        return JsonResponse({
            'success': False,
            'message': '请使用POST方法提交'
        })
