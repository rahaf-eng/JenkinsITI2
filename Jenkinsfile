pipeline {
    agent any

    stages {
        // 1. مرحلة السحب من جيت هاب
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        // 2. مرحلة الـ Build (تجهيز البيئة الافتراضية)
        stage('Build') {
            steps {
                echo 'Setting up Python Virtual Environment...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        // 3. مرحلة الاختبار (Test)
        stage('Test') {
            steps {
                echo 'Running Application Tests...'
                sh '''
                    . venv/bin/activate
                    pytest test_app.py
                '''
            }
        }

        // 4. مرحلة النشر والتشغيل (Deploy)
        stage('Deploy') {
            steps {
                echo 'Deploying application (Running Flask App in background)...'
                // تشغيل التطبيق في الخلفية عشان جينكينز ما يفضلش معلق
                sh '''
                    . venv/bin/activate
                    nohup python3 app.py > flask.log 2>&1 &
                '''
                echo 'Application is live!'
            }
        }
    }

    post {
        success {
            echo 'Pipeline finished successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
