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