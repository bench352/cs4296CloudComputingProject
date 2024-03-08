# Web Server for CS4296 Cloud Computing Project

This web server has been developed to benchmark the performance of the chosen deployment method.

## API Endpoints

### `/api/test/response`

An API endpoint that returns a fixed dummy response. Designed to test the network latency of the deployment platform.

**Parameters**

No parameters

**Example Response**

```json
{
  "user": "Chris Wong",
  "message": "Hello world!"
}
```

### `/api/test/calculation`

A computationally heavy and memory-intensive API endpoint that invokes a matrix multiplication on the server side with a
configurable matrix size. Returns the time taken to generate matrixes with random values and perform matrix
multiplication. Designed to test the computational performance of the deployment platform.

**Parameters**

| Parameter Name | Type  | Description                    | Example Value |
|----------------|-------|--------------------------------|---------------|
| `matrix_size`  | Query | The size of the matrix (N * N) | `1000`        |

**Example Response**

```json
{
  "message": "Calculation completed",
  "result_shape": [
    1000,
    1000
  ],
  "randomization_time": "8.697271347045898ms",
  "multiplication_time": "27.978897094726562ms"
}
```

### `/api/test/file`

An API endpoint for downloading a dummy text file with the chosen size. Designed to test the network performance of the
deployment platform.

**Parameters**

| Parameter Name | Type  | Description                                | Accepted Value  |
|----------------|-------|--------------------------------------------|-----------------|
| `size`         | Query | The size of the text file to be downloaded | `500mb` / `1gb` |

**Response**

A text file with the specified size.

### `/docs`

An API endpoint to access the **Swagger UI** for the webserver to test the API endpoints.

## Reveal Process Time for Each Request

The web server includes a middleware to log the time taken to process each request. The process time is provided via the
response header `x-process-time` in milliseconds. Here is an example that uses the `curl` command to make a query to the
server and get the response as well as the processing time (note the `-v` flag to enable verbose mode):

```bash
curl -v \
  'http://localhost:8000/api/test/response' \
  -H 'accept: application/json'
```

Here is an example of the response:

```plaintext
* Trying 127.0.0.1:8000...
* Connected to localhost (127.0.0.1) port 8000 (#0)
> GET /api/test/response HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.81.0
> accept: application/json
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< date: Fri, 08 Mar 2024 14:06:07 GMT
< server: uvicorn
< content-length: 46
< content-type: application/json
< x-process-time: 0.2830028533935547ms
<
* Connection #0 to host localhost left intact
{"user":"Chris Wong","message":"Hello world!"}
```