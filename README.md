<div align="center">

<!-- TODO: add link to website once it is ready -->
<h1>Tax Sparrow</h1>

Simple, yet powerful compliance solutions for Indian businesses

[![Server Tests](https://github.com/netmanthan/taxsparrow/actions/workflows/server-tests.yml/badge.svg)](https://github.com/netmanthan/taxsparrow/actions/workflows/server-tests.yml)

</div>



## Introduction

Tax Sparrow has been designed to make compliance with Indian rules and regulations simple, swift and reliable. To this end, it has been carefully integrated with GST APIs to simplify recurring compliance processes.


## Key Features

- End-to-end GST e-Waybill management
- Automated GST e-Invoice generation and cancellation
- Autofill Party and Address details by entering their GSTIN
- Configurable features based on business needs
- Powerful validations to ensure correct compliance

## Installation


1. Download the app using the Bench CLI.

    ```bash
    bench get-app --branch [branch name] https://github.com/netmanthan/taxsparrow.git
    ```

    
2. Install the app on your site.

    ```bash
    bench --site [site name] install-app taxsparrow
    ```


