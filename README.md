
# QR Code Generator using serverless function

## Overview

This project is a demonstration of using DigitalOcean's Function as a Service (FaaS) platform to deploy and run serverless functions. The functions in this project uses majorly python runtime, specifically version 3.11.1 to generate QR Code. 

## Table of Contents

- [QR Code Generator using serverless function](#qr-code-generator-using-serverless-function)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Getting Started](#getting-started)
  - [Deployment](#deployment)
  - [Usage](#usage)
  - [Function Configuration](#function-configuration)
  - [Monitoring and Logging](#monitoring-and-logging)
  - [Contributing](#contributing)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- A DigitalOcean account (Sign up at [https://www.digitalocean.com/](https://www.digitalocean.com/))
- [DigitalOcean CLI](https://docs.digitalocean.com/reference/doctl/) (It is required for deployment. Although you can deploy a function using Digital Ocean Dashboard)
- Basic knowledge of serverless computing and Python.

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/aoamusat/qrcodefn.git
   cd qrcodefn
   ```

2. Install any project-specific dependencies if needed.

3. Follow the deployment instructions below to deploy your serverless functions to DigitalOcean.

## Deployment

Deployment of serverless functions to DigitalOcean can be done manually through the DigitalOcean dashboard or using the DigitalOcean CLI. This project make use of the CLI to deploy the functions:

1. **Install the [DigitalOcean CLI](https://docs.digitalocean.com/reference/doctl/) tool**

2. **Configure Your Function**: Specify the ```build.sh```, ```requirements.txt``` and ```__main__.py``` file for your serverless functions. You can specify environment variables in project.yml file in the root directory if needed. See the directory structure for more information:

```md
├── packages/
│   └── <package-name>/
│       ├── <function-name-1>/
│       └── <function-name-2>/
```
Refer to the documentation for more details: [Build Process](https://docs.digitalocean.com/products/functions/reference/build-process/)

3. **Define Routes**: Configure the routes that trigger your serverless functions. Define HTTP paths and methods that should invoke your functions.

4. **Deploy Your Function**: Trigger the deployment of your app either manually (```doctl serverless deploy qrcodefn```) or through a CI/CD pipeline.

5. **Monitor Your Functions**: Use [DigitalOcean's monitoring and logging](https://cloud.digitalocean.com/functions) features to keep an eye on the performance of your functions.

## Usage

Once your serverless functions are deployed, they can be accessed using the defined routes. You can make HTTP requests to these routes to invoke the functions. Below is a sample JavaScript example: 

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "data": "geo:8.3665421,3.0912434"
});

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://faas-lon1-917a94a7.doserverless.co/api/v1/web/fn-e575a662-b135-4bbf-92e9-0e337bce300b/qrpkg/qrcode", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

For example, if you have a function that processes data, you can send a GET request to its endpoint with the required payload.

## Function Configuration

You can configure your serverless functions using environment variables, secrets, and other settings provided by the DigitalOcean App Platform. Refer to DigitalOcean's documentation for detailed information on how to configure and customize your functions.

## Monitoring and Logging

DigitalOcean provides built-in monitoring and logging for your serverless functions. You can access logs and metrics to troubleshoot issues and monitor performance.

## Contributing

Contributions to this project are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Create a pull request to merge your changes into the main branch.