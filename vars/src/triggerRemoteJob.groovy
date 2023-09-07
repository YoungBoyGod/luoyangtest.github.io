// vars/triggerRemoteJob.groovy

def call(String remoteJobUrl, String authToken, Map params = [:]) {
    // 构建远程 Job 的 URL，包括参数和认证令牌
    def remoteJobTriggerUrl = "${remoteJobUrl}/buildWithParameters?token=${authToken}"

    // 创建 HTTP 请求，触发远程 Job
    def response = sh(script: "curl -X POST ${remoteJobTriggerUrl} -d ${params.toQueryString()}", returnStatus: true)

    if (response != 0) {
        error "Failed to trigger remote Job."
    }
}
//@Library('your-shared-library') _
//
//pipeline {
//    agent any
//
//    stages {
//        stage('Build') {
//            steps {
//                // 构建并生成构建制品
//
//                // 调用 Shared Library 中的 triggerRemoteJob 函数触发 Jenkins B 上的远程 Job
//                triggerRemoteJob(
//                        remoteJobUrl: 'http://jenkins-b-url/job/job-name',
//                        authToken: 'your-auth-token',
//                        params: [
//                                param1: 'value1',
//                                param2: 'value2'
//                        ]
//                )
//            }
//        }
//    }
//}