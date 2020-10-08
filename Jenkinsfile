pipeline {
    agent any

    stages {
        stage('Create File With Name') {
            steps {
                script {
                 status = sh(script: 'NAME=${NAME} ./fifthAssignment.sh', returnStatus: true)
                 echo "status is ${status}"
                }
            }
        }

          stage('Run Selenium tests') {
            steps {
                script {
                 echo "sourcing venv"
                 sh(script: 'cd ${WORKSPACE} && ./source_venv.sh')
                 echo "running all selenium tests from fourth assignment"
                 status = sh(script: 'cd ${WORKSPACE} && python fourth_assignment.sh', returnStatus: true)
                 echo "status is ${status}"
                }
            }
        }
    }

        post {
        always {
            echo "ALWAYS. Runs all the time."
        }
        success {
            echo "SUCCESS"
        }
        failure {
            echo "FAILURE!!"
        }
    }
}
