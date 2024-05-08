pipeline {
    agent any

    environment {
        // Define environment variables
        GIT_URL = 'https://github.com/yuribernstein/gde-devops.git'
        PARAM = 'Hello!'
        payload = readJSON text: env.PAYLOAD
    }
    
    stages {
        
        stage('Checkout') {
            steps {
                echo "Hello ${env.PARAM}"
                git branch:'main', url:env.GIT_URL
                echo payload
            }
        }
        
        stage('Build') {
            steps {
                sh 'echo build stage is running!'
            }
        }
    }
}
