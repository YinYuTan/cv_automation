pipeline{
    agent any

    stages{
        stage('Checkout'){
            steps{
                checkout scm
            }
        }
        stage('Checking Python Version') {
            steps {
                script {
                    // echo "Checking Python version..."
                    bat 'python --version'
                }
            }
        }
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
        stage('Download Model') {
            steps {
                bat '''
                    if not exist models mkdir models

                    set "MODEL_PATH=models\\multiclass_img2_model_v9.h5"

                    if exist %MODEL_PATH% (
                        for %%I in (%MODEL_PATH%) do set "SIZE=%%~zI"
                        if %SIZE% GEQ 530000000 (
                            echo Model already exists and is complete. Skipping download.
                        ) else (
                            echo Incomplete model found. Re-downloading...
                            del %MODEL_PATH%
                            curl -o %MODEL_PATH% https://jenkins-models-test.s3.ap-southeast-1.amazonaws.com/multiclass_img2_model_v9.h5
                        )
                    ) else (
                        echo Model not found. Downloading...
                        curl -o %MODEL_PATH% https://jenkins-models-test.s3.ap-southeast-1.amazonaws.com/multiclass_img2_model_v9.h5
                    )
                '''
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

    post {
        always {
            archiveArtifacts artifacts: 'results/**', allowEmptyArchive: true

            step([$class: 'RobotPublisher',
                outputPath: 'results',
                outputFileName: 'output.xml',
                reportFileName: 'report.html',
                logFileName: 'log.html'
            ])
        }
    }
}