# Create a folder
$ mkdir actions-runner && cd actions-runner# Download the latest runner package
$ curl -o actions-runner-linux-x64-2.326.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.326.0/actions-runner-linux-x64-2.326.0.tar.gz# Optional: Validate the hash
$ echo "9c74af9b4352bbc99aecc7353b47bcdfcd1b2a0f6d15af54a99f54a0c14a1de8  actions-runner-linux-x64-2.326.0.tar.gz" | shasum -a 256 -c# Extract the installer
$ tar xzf ./actions-runner-linux-x64-2.326.0.tar.gz


# Create the runner and start the configuration experience
$ ./config.sh --url https://github.com/williamyatacodev/90daysdevops-cd-ci --token AC56G7YBPTOLKCAYTDAPN3DIP36CKCopied! # Last step, run it!
$ ./run.sh