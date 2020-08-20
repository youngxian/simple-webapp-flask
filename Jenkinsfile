pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Hello World'
                sh """ pwd """
            }
        }
        stage('Deploy') {
            steps {
                echo 'Hello World'
                script {
                   def fields = env.getEnvironment()
                   fields.each {
                        key, value -> println("${key} = ${value}");
                    }
 
                    println(env.PATH)
               }
            }
        }
        stage('Test') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
