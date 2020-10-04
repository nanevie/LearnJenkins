/*
checkout poll: false, scm: [$class: 'GitSCM', 
branches: [[name: '* /master']], 
doGenerateSubmoduleConfigurations: false, 
extensions: [], submoduleCfg: [], 
userRemoteConfigs: [[credentialsId: 'GithubSSH2', 
url: 'https://github.com/ParthaK8/codesamples']]]
*/

def myCheckout(myGitUrl, myBranch, myLocalDir) {
    checkout changelog: false, poll: false, scm: [$class: 'GitSCM',
    branches: [[name: myBranch]],
    doGenerateSubmoduleConfigurations: false,
    extensions: [[$class: 'RelativeTargetDirectory',
    relativeTargetDir: myLocalDir]],
    submoduleCfg: [],
    userRemoteConfigs: [[credentialsId: 'GithubSSH',
    url: myGitUrl]]
    ]
}

node () {
    stage ('Clone Git') {
        echo "Cloning git"
        def parthak8_url = "git@github.com:ParthaK8/codesamples"
        def parthak8_branch = "*/testoper-testing"
        def local_dir = "parthak8"
        myCheckout(parthak8_url, parthak8_branch, local_dir)

        // set an environment variable, value of local_dir
        env.LOCAL_DIR = local_dir
        
        // Verify
        sh "ls -la"
        sh "ls -la ${LOCAL_DIR}"
        def CWDABSPATH
        CWDABSPATH = sh (
        script: "echo `pwd`",
                returnStdout: true
        ).trim()
        println "Current Working Directory: " + CWDABSPATH
        env.BASEPATH = CWDABSPATH  // set env var for BASEPATH
    }

    stage ('compile with gradle') {


    }

    stage ('compose the app') {

    }
}