from logger import setup_logger

logger = setup_logger()

def print_result(generated_text: str):
    logger.info("Generated Text:")
    print("-" * 40)
    print(generated_text)
    print("-" * 40)

def validate_generated_text(text: str):
    if not text.strip():
        logger.warning("Generated text is empty.")
        return False
    if len(text) > 500:  # Arbitrary limit
        logger.warning("Generated text is too long.")
        return False
    logger.info("Generated text passed validation.")
    return True

