# Tools

## Overview

This directory contains tools that are used to generate the necessary files for ISVS releases.

## Exporting to JSON, CSV and XML

### Instructions

Use the "export.py" script to export ISVS to the required format.

### File reference

- export.py: Python script to generate a CSV, JSON or XML version of the ISVS.
- isvs.py: Python script used by export.py

## Exporting to PDF, DOCX, EPUB and MOBI 

### Instructions 

Make sure the local Docker daemon is running. 

Execute ```./tools/docker/run_docker_isvs_generation_on_local.sh``` from the main folder (do not run the script directly from the docker folder). The files are generated inside the root folder.

## Notes and remaining work 

The export and Docker scripts should be updated if the ISVS structure changes: 

* If the name of the document folder is modified (ex. from "en" to "Document-en");
* If the name convention for chapters changes (ex. from "V1 - XXX" to "0x01 - XXX");
* If more languages are added; 
* If the structure of the MD requirements tables inside the chapters changes; 
* If more chapters (ex. "Introduction.md") are added.  

Additionally, the Docker container should eventually be uploaded to docker.com, so that it can be pulled as a whole and not built locally. This should be ideally be done when the structure and the contents of the ISVS are fixed, so that the correct scripts are included in the container.