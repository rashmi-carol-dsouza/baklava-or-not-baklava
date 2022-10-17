# Baklava Or Not Baklava

## Dataset 

The dataset can be found on [Google Drive](https://drive.google.com/drive/folders/1DdizakDGlQOXAfpexEXuClc6e-3O-ytL?usp=sharing)

## Running Locally

### Web App

#### Install Deps

To run the web app locally, navigate to the `web-app` directory and run `npm install` to install frontend depenencies.

#### Configure API Path

The frontend app needs to know which API to call when uploading photos. This can be configured locally by creating a `.env` file ([learn more](https://dev.to/danawoodman/storing-environment-variables-in-sveltekit-2of3)).

You can then specify the API endpoint by adding the following to the file:

```
VITE_API_URL=http://127.0.0.1:5000
```

This will ensure that the frontend uses the API offered by the `baklava-recognition-service` as the API Endpoint.
You need to have this API running (see instructions to run the service) for it to work locally.

Alternatively you could you use the production URL to have the frontend work with the production API locally.