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
                 status = sh(script: 'NAME=${NAME} ./source_venv.sh', returnStatus: true)
                 echo ${status}
                 echo "running all selenium tests from fourth assignment"
                 status = sh(script: 'python3 fourth_assignment.sh', returnStatus: true)
                 echo "status is ${status}"
                }
            }
        }
    }
}
