
```sh
gcloud init

gcloud config set projet PROJECT_ID

gcloud auth login

gcloud auth login --no-browser

gcloud auth application-default login

gcloud iam roles list --help

gcloud iam roles list --filter=custom

gcloud iam role list --filter="name ~ policyAdmin"

gcloud iam roles create MyCustomRole --organization="237684251" --file=custom-role.yaml

gcloud iam roles update customRoleExample \
  --project=$(gcloud config get-value project) \
  --file=custom_role.yaml

gcloud iam roles delete customRoleExample \
  --project=$(gcloud config get-value project)

gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT_ID \
        --member="serviceAccount:terraform-sa@GOOGLE_CLOUD_PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/compute.instanceAdmin.v1"

gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT_ID \
        --member="serviceAccount:terraform-sa@GOOGLE_CLOUD_PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/iam.serviceAccountUser"
gcloud projects get-iam-policy project-exampro-2024

gcloud iam service-accounts keys create terraform-key.json \
        --iam-account=terraform-sa$GOOGLE_CLOUD_PROJECT_ID.iam.gserviceaccount.com

gcloud services enable run.googleapis.com cloudbuild.googleapis.com

gcloud services list --enabled

gcloud services list --available | grep -i "compute"

gcloud services list --available | grep -i "storage"

gcloud services disable storage.googleapis.com

gcloud iam service-accounts create terraform-sa \
        --description="Service account for Terraform" \
        --display-name="Terraform Service Account"

gcloud storage cp hello.txt gs://my-really-cool-bucket-12321

gcloud compute instances create my-vm-e2 --machine-type=e2-medium --zone=us-central1-a

gcloud compute instances delete ace-api-test --zone=us-central1-a --quiet

gcloud run deploy --source .

gcloud run deploy ruby-http-function \
        --source . \
        --function hello_get \
        --base-image ruby34 \
        --region northamerica-northeast2 \
        --allow-unaunthenticated
        
gcloud deployment-manager deployments update --config <deployment-config-path>

gcloud pubsub topics delete my-topic

gcloud container clusters list --project de0360-de
v-lam-idm-dev

gcloud container clusters describe dev-ew4 --region europe-west4 --format="get(privateClusterConfig.enablePrivateEndpoint)"

```


