package com.example

def sendEmailWithAttachment(String subject, String body, boolean attachLogFile = false) {
    def attachLog = attachLogFile || currentBuild.resultIsWorseThan(hudson.model.Result.SUCCESS)

    emailext (
            subject: subject,
            body: body,
            to: emailextrecipients([[$class: 'CulpritsRecipientProvider']]),
            attachLog: attachLog,
            compressLog: true
    )
}
@Library('my-shared-library') _ // 引用您的 Shared Library

//pipeline {
//    agent any
//
//    stages {
//        stage('Build') {
//            steps {
//                // 在此添加构建步骤
//            }
//        }
//    }
//
//    post {
//        always {
//            script {
//                def emailSubject = "${currentBuild.fullDisplayName}"
//                def emailBody = "${currentBuild.result}\n\n${BUILD_LOG, maxLines=100, escapeHtml=true}"
//
//                com.example.EmailUtils.sendEmailWithAttachment(emailSubject, emailBody)
//            }
//        }
//    }
//}