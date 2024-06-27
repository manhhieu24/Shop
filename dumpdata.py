import json
import os
import django
from django.core.management import call_command

# Thiết lập môi trường Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

# Đường dẫn tới file JSON
output_file = 'data.json'

# Mở file với mã hóa UTF-8 và ghi dữ liệu
with open(output_file, 'w', encoding='utf-8') as f:
    call_command('dumpdata', stdout=f, format='json')

print(f'Data has been dumped to {output_file}')
