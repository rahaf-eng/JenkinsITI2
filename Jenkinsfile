pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-python-app"
        CONTAINER_NAME = "my-python-app-container"
    }

    stages {
        // 1. مرحلة السحب من جيت هاب
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        // 2. مرحلة بناء الصورة (Build)
        stage('Build') {
            steps {
                echo 'Building Docker Image...'
                // بناء صورة الدوكر من الـ Dockerfile
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        // 3. مرحلة الاختبار (Test)
        stage('Test') {
            steps {
                echo 'Running Application Tests inside a temporary container...'
                // تشغيل الاختبارات للتأكد من سلامة الكود قبل النشر النهائي
                sh "docker run --rm ${IMAGE_NAME}:latest pytest test_app.py"
            }
        }

        // 4. مرحلة النشر والتشغيل (Deploy)
        stage('Deploy') {
            steps {
                echo 'Deploying application to Docker Desktop...'
                // مسح الحاوية القديمة لو كانت شغالها لمنع تضارب الـ Ports
                sh "docker rm -f ${CONTAINER_NAME} || true"
                // تشغيل الحاوية الجديدة وربطها ببورت 5000
                sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 ${IMAGE_NAME}:latest"
                echo 'Application is live!'
            }
        }
    }

    post {
        success {
            echo 'Pipeline finished successfully! Ready for screenshots.'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
