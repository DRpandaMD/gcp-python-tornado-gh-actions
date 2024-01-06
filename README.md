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


### Adding Auth

In order for Github to do things inside GCP we need to Authenticate.

We are going to use and follow DWIF seen here: https://github.com/google-github-actions/auth?tab=readme-ov-file#preferred-direct-workload-identity-federation

Updating the yaml file we have :

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
      uses: 'actions/checkout@v3'

    - name: Set Up Google Auth
      uses: 'google-github-actions/auth@v2'
      with:
        project_id: 'cloud-devops-viking-test-area'
        workload_identity_provider: 'projects/1025514410896/locations/global/workloadIdentityPools/drpandamd-gh/providers/python-tornado-ghactions' 

```

In order to use any of this you have to set this up.  The easiest way is through the CLI.  You can take a look at the `shellhelper.sh` file.  Or glance below.

```bash
gcloud iam workload-identity-pools create "drpandamd-gh" \
  --project="cloud-devops-viking-test-area" \
  --location="global" \
  --display-name="drpandamd-gh-actions pool"

gcloud iam workload-identity-pools describe "drpandamd-gh" \
  --project="cloud-devops-viking-test-area" \
  --location="global" \
  --format="value(name)"


gcloud iam workload-identity-pools providers create-oidc "python-tornado-ghactions" \
  --project="cloud-devops-viking-test-area" \
  --location="global" \
  --workload-identity-pool="drpandamd-gh" \
  --display-name="My GitHub repo Provider" \
  --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.repository=assertion.repository" \
  --issuer-uri="https://token.actions.githubusercontent.com"

gcloud iam workload-identity-pools providers describe "python-tornado-ghactions" \
  --project="cloud-devops-viking-test-area" \
  --location="global" \
  --workload-identity-pool="drpandamd-gh" \
  --format="value(name)"
```

Follow up TODO: Continue Debuggin and fleshing out the CI/CD yaml .