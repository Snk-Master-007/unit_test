pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                sh '''
                    docker stop test-container || true
                    docker rm test-container || true
                    docker build -t test-app .
                    docker run -d -p 8001:8001 --name test-container test-app
                '''
            }
        }
    }
}