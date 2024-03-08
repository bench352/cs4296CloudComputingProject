import time

import fastapi
import numpy as np
from loguru import logger

import const

router = fastapi.APIRouter(prefix="", tags=["Benchmarking"])


@router.get("/response", description="Return a fixed dummy response")
async def get_response():
    return {"user": "Chris Wong", "message": "Hello world!"}


@router.post("/calculation", description="Perform a computationally heavy matrix calculation")
async def perform_calculation(matrix_size: int):
    logger.info("Matrix multiplication request received, size=({},{})", matrix_size, matrix_size)

    randomization_start_time = time.time()
    matrix_a = np.random.rand(matrix_size, matrix_size)
    matrix_b = np.random.rand(matrix_size, matrix_size)

    randomization_time = time.time() - randomization_start_time

    logger.info("Generated 2 random matrices of size=({},{})", matrix_size, matrix_size)

    multiplication_time = time.time()

    result = np.dot(matrix_a, matrix_b)

    multiplication_time = time.time() - multiplication_time

    logger.info("Matrix multiplication completed")

    randomization_time_in_ms = randomization_time * 1000
    multiplication_time_in_ms = multiplication_time * 1000

    return {
        "message": "Calculation completed",
        "result_shape": result.shape,
        "randomization_time": f"{randomization_time_in_ms}ms",
        "multiplication_time": f"{multiplication_time_in_ms}ms"
    }


@router.get("/file", description="Return a file of a specified size")
def download_file(size: const.FileOptions):
    if size == const.FileOptions.ONE_GB:
        file_path = "./media/1gb.txt"
    else:
        file_path = "./media/500mb.txt"
    return fastapi.responses.StreamingResponse(open(file_path, "rb"), media_type="text/plain", headers={
        "Content-Disposition": f"attachment; filename={size.value}.txt"
    })
