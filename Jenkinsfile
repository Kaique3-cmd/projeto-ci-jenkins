pipeline {
    agent any

    environment {
        APP_NAME = "projeto-ci-engcomp"
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('1. Checkout do Código') {
            steps {
                echo "Baixando código-fonte do repositório Git..."
                checkout scm
            }
        }

        stage('2. Preparação do Ambiente') {
            steps {
                echo "Criando ambiente virtual e instalando dependências..."
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('3. Análise Estática (Lint)') {
            steps {
                echo "Verificando padrões de código com Flake8..."
                sh '''
                    . venv/bin/activate
                    flake8 app/ --max-line-length=100
                '''
            }
        }

        stage('4. Testes Automatizados') {
            steps {
                echo "Executando suíte de testes unitários com Pytest..."
                sh '''
                    . venv/bin/activate
                    PYTHONPATH=app pytest --junitxml=relatorio-testes.xml
                '''
            }
            post {
                always {
                    junit 'relatorio-testes.xml'
                }
            }
        }

        stage('5. Build da Imagem Docker') {
            steps {
                echo "Empacotando aplicação validada em imagem Docker..."
                sh "docker build -t ${APP_NAME}:${IMAGE_TAG} ."
            }
        }
    }

    post {
        success {
            echo "PIPELINE CONCLUÍDA COM SUCESSO! (Build #${env.BUILD_NUMBER})"
        }
        failure {
            echo "FALHA NA INTEGRAÇÃO! O commit quebrou a build ou os testes."
        }
    }
}
