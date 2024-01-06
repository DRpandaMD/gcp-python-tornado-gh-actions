# gcp-python-tornado-gh-actions
Python Tornado App built with ChatGPT, Focusing on implementing GH actions to build and deploy.

## And the Point is?

A rough copy of this exists elsewhere in my repos.  The point here is to clean this up removing some unused files from another project, and redeploy this into GCP using GitHub Actions.  I already have a working CI/CD deployment model for Cloud Build -> Cloud in another repo. 


## Starting with GitHub Actions

My initial impressions thus far is that the suggested actions are not really that clear and can be a little confusing.  I suggest just starting with a blank template and going from there.  I think a bit more AI is needed on the backend to help steer you in the right direction to make the interface usable.  The sheer number of options and versions make it difficult to decipher where I should go.  So lets start with some 'boiler plate code':

```yaml
# First Pass at building a CI/CD pipline using Github Actions
name: Build and Deploy to Cloud Run

on:
  push:
    branches: [ "*" ]
  pull_request:
    branches: [ "*" ]

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout Code
      uses: actions/checkout@v3

    - name: Set Up Google Cloud SDK
```

Breaking it down: 

* The top level name is just the name of our pipeline.
* on push -- we are going to run this on push or pull requests on "*" (any) branch
* jobs - is the job we want to define
  * 'build-deploy' can be any name
  * obvioiusly our first step is to checkout the code into the runner -- very Jenkins like