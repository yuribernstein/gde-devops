pipeline {
    agent any

    environment {
        // Define environment variables
        GIT_URL = 'https://github.com/yuribernstein/gde-devops.git'
        PARAM = 'Hello!'
    }

    triggers {
        GenericTrigger(
            genericVariables: [
                [key: 'BRANCH_NAME', value: '$.ref', expressionType: 'JSONPath'],
                [key: 'COMMIT_ID', value: '$.after', expressionType: 'JSONPath']
            ],
            causeString: 'Triggered by $BRANCH_NAME with commit $COMMIT_ID',
            token: 'your-webhook-token',
            printContributedVariables: true,
            printPostContent: true
        )
    }

    

    stages {

        stage('Parse Payload') {
            steps {
                echo "Branch from payload: ${env.BRANCH_NAME}"
                echo "Commit ID from payload: ${env.COMMIT_ID}"
                // You can add more logic here based on the payload
            }
        }
        stage('Checkout') {
            steps {
                // sh 'Hello ${env.PARAM}'
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
