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

An API endpoint that invokes a matrix multiplication on the server side with a configurable matrix size. Returns the
time taken to generate matrixes with random values as well as the time taken to perform matrix multiplication. Designed
to test the computational performance of the deployment platform.

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

An API endpoint to access the **Swagger UI** for the webserver to test out the API endpoints.
