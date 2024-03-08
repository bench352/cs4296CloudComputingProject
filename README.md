# CS4296 Cloud Computing Project

## Web Server

This web server has been developed to benchmark the performance of the chosen deployment method. This web server is
developed using **Python** and **FastAPI**.

### API Documentation

The API documentation of the web server can be found [here](./web-server/README.md).

### Installation

#### On A Bare Metal Server (Linux based)

1. Git Clone the repository

   ```bash
   git clone https://github.com/bench352/cs4296CloudComputingProject.git
   ```

2. Change directory to the git repository

   ```bash
   cd cs4296CloudComputingProject
   ```

3. Run the installation script

    ```bash
    ./setup.sh
    ```

4. On the `web-server` directory, make a `media` directory

    ```bash
    mkdir web-server/media
    ```

5. Start the web server (on the `web-server` directory)

    ```bash
    python3.10 main.py
    ```

6. Access your web server at `http://localhost:8000` or `http://<your-server-ip>:8000`.

#### Using Docker

The Docker image is available
at [Docker Hub](https://hub.docker.com/repository/docker/bench352/cs4296-web-server-for-project). You can run the image
on your machine using the following command:

```bash
docker run -d --rm -p 8000:8000 bench352/cs4296-web-server-for-project:latest
```

Then access the web server at `http://localhost:8000` or `http://<your-server-ip>:8000`.
