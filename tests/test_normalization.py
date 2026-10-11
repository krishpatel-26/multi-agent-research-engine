from app.normalization import normalize_claim, normalized_source_key

def test_claim_normalization_handles_case_and_whitespace():
    assert normalize_claim("  The   FACT is TRUE! ") == "the fact is true"

def test_claim_normalization_uses_unicode_normalization():
    assert normalize_claim("ＡI") == "ai"

def test_source_key_trims_whitespace_and_casefolds():
    assert normalized_source_key("  Source-A ") == "source-a"

def test_empty_claim_normalizes_to_empty_string():
    assert normalize_claim("  !!! ") == ""
