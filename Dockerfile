FROM python:3.9-slim

WORKDIR /app

# نسخ ملف المكتبات وتثبيتها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي كود المشروع
COPY . .

# فتح البورت الخاص بالتطبيق
EXPOSE 5000

# أمر تشغيل التطبيق
CMD ["python", "app.py"]
