pipeline {
    agent any

    environment {
        // Define environment variables
        GIT_URL = 'https://github.com/yuribernstein/gde-devops.git'
        PARAM = 'Hello!'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo "Hello ${env.PARAM}"
                git branch:'main', url:env.GIT_URL
            }
        }
        
        stage('Build') {
            steps {
                sh 'echo build stage is running!'
            }
        }
    }
}
