# CS4296 Cloud Computing Project

## Web Server

This web server has been developed to benchmark the performance of the chosen deployment method. This web server is
developed using **Python** and **FastAPI**.

### API Documentation

The API documentation of the web server can be found [here](./web-server/README.md).

### Installation

#### On A Bare Metal Computer (Linux)

1. Make sure you have Git and Python installed on your machine. If not, install it using the following command:

   ```bash
   sudo apt-get update
   sudo apt-get install git python3 python3-pip python3.10-venv -y
   ```

2. Git Clone the repository

   ```bash
   git clone https://github.com/bench352/cs4296CloudComputingProject.git
   ```

3. Change directory to the git repository

   ```bash
   cd cs4296CloudComputingProject
   ```

4. Run the installation script. This script will install the webserver in `/usr/local/bin/web-server` and start it as
   a systemd service.

    ```bash
    sudo bash ./setup.sh
    ```

5. Access your web server at `http://localhost:8000` or `http://<your-server-ip>:8000`. You can also check the status of
   the web server using the following command:

    ```bash
    sudo systemctl status webserver
    ```

> **Uninstallation**: An uninstallation script is also provided in the repository. It will remove both the systemd
> service for the webserver and the webserver itself. You can uninstall the web server using the following command:
>
>  ```bash
>  sudo bash ./uninstall.sh
>  ```

#### Using Docker

The Docker image is available
at [Docker Hub](https://hub.docker.com/r/bench352/cs4296-web-server-for-project). You can run the image
on your machine using the following command:

```bash
docker run -d --rm -p 8000:8000 --name cs4296-web-server bench352/cs4296-web-server-for-project:latest
```

Then access the web server at `http://localhost:8000` or `http://<your-server-ip>:8000`.
