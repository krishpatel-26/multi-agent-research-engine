import re
import unicodedata

def normalize_claim(text: str) -> str:
    """Normalize claim text for conservative comparison and deduplication."""
    value = unicodedata.normalize("NFKC", text).casefold()
    value = re.sub(r"\s+", " ", value).strip()
    value = re.sub(r"^[\W_]+|[\W_]+$", "", value)
    return value

def normalized_source_key(source: str) -> str:
    """Normalize a source identifier without assuming URL equivalence."""
    return unicodedata.normalize("NFKC", source).strip().casefold()
