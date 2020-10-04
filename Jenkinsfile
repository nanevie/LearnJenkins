/*
checkout changelog: false, poll: false, scm: [$class: 'GitSCM', 
branches: [[name: '*/master']], 
doGenerateSubmoduleConfigurations: false, 
extensions: [], 
submoduleCfg: [], 
userRemoteConfigs: [[credentialsId: 'GitSSH', 
url: 'https://github.com/ParthaK8/codesamples']]
]
*/
def myCheckout(myGitURL, myBRANCH, myLocalDir) {
    checkout changelog: false, poll: false, scm: [$class: 'GitSCM', 
    branches: [[name: myBranch]], 
    doGenerateSubmoduleConfigurations: false, 
    extensions: [[$class: 'RelativeTargetDirectory',
    relativeTargetDir: myLocalDir]], 
    submoduleCfg: [], 
    userRemoteConfigs: [[credentialsId: 'GitSSH', 
    url: myGitUrl]]
    ]
}

node () { 
    stage ('Clone Git') {
        echo 'Cloning Git... ParthaK8/codesamples'
        def parthak8_url = "git@github.ibm.com:ParthaK8/codesamples"
        def parthak8_branch = "*/jenkins-test"
        def local_dir = "parthak8"
        myCheckout(parthak8_url, parthak8_branch, local_dir)

        // set an environment variable, value of local_dir
        env.LOCAL_DIR = local_dir 

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

    stage ('Compile using gradle') {
        echo "Starting compilation"

    }

    stage ('Run Unit-tests') {
        echo "Running Unit-tests"

    }

}
