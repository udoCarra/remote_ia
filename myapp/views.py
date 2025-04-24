from django.shortcuts import render

import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import VastAIInstance

VAST_API_KEY = 'your_vast_api_key'
VAST_API_URL = 'https://vast.ai/api/v0.1'

def create_instance(request):
    response = requests.post(f'{VAST_API_URL}/create', headers={'Authorization': f'Bearer {VAST_API_KEY}'})
    if response.status_code == 200:
        instance_data = response.json()
        instance_id = instance_data['id']
        status = instance_data['status']
        instance = VastAIInstance.objects.create(instance_id=instance_id, status=status)
        return JsonResponse({'status': 'instance created', 'instance_id': instance_id})
    else:
        return JsonResponse({'error': 'Failed to create instance'}, status=400)

def check_instance_status(request, instance_id):
    instance = VastAIInstance.objects.get(instance_id=instance_id)
    response = requests.get(f'{VAST_API_URL}/status/{instance_id}', headers={'Authorization': f'Bearer {VAST_API_KEY}'})
    if response.status_code == 200:
        status_data = response.json()
        instance.status = status_data['status']
        instance.save()
        return JsonResponse({'status': instance.status})
    else:
        return JsonResponse({'error': 'Failed to check status'}, status=400)

def display_image(request, instance_id):
    instance = VastAIInstance.objects.get(instance_id=instance_id)
    return render(request, 'display_image.html', {'image_url': instance.image_url})
