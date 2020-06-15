# ISVS PDFs Generation with Docker

The ISVS document generation is based on pandocker: [https://github.com/dalibo/pandocker/blob/latest/LICENSE](https://github.com/dalibo/pandocker/blob/latest/LICENSE).

## On your Machine

- Install Docker
- `cd` to the ISVS root folder `IoT-Security-Verification-Standard-ISVS/`
- Run the following and give a version number (**do not `cd` into `tools/docker` to run it**):

    ```sh
    $ ./tools/docker/run_docker_isvs_generation_on_local.sh 1.2
    ```