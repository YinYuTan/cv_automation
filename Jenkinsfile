pipeline{
    agent any

    stages{
        stage('Checkout'){
            steps{
                checkout scm
            }
        }
        // stage('Checking Python Version') {
        //     steps {
        //         script {
        //             echo "Checking Python version..."
        //             bat 'python --version'
        //         }
        //     }
        // }
        stage('Installing Virtual Environment'){
            steps{
                script{
                    bat "python -m venv venv"   // Create venv
                }
            }
        }
        stage('Install Dependencies'){
            steps{
                script{
                    bat """
                        call venv\\Scripts\\activate
                        python -m pip install --upgrade pip
                        pip install -r ./requirements.txt
                        pip install --upgrade robotframework-seleniumlibrary
                    """
                }
            }
        }
        stage('Check Installed Dependencies'){
            steps{
                script{
                    bat """
                        call venv\\Scripts\\activate
                        pip list
                    """
                }
            }
        }
        stage('Run Robot'){
            steps{
                script{
                    bat """
                        call venv\\Scripts\\activate
                        robot --outputdir results Robot/prediction.robot
                    """
                }
            }
        }
    }
}