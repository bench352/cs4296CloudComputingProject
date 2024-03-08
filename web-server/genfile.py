from loguru import logger

ONE_GB = 1024 * 1024 * 1024  # 1GB
FIVE_HUNDRED_MEGABYTES = 1024 * 1024 * 500  # 500MB


def generate_files():
    with open("./media/1gb.txt", "w") as f:
        f.write("A" * ONE_GB)

    with open("./media/500mb.txt", "w") as f:
        f.write("A" * FIVE_HUNDRED_MEGABYTES)

    logger.info("Test files generated successfully!")


if __name__ == "__main__":
    generate_files()
