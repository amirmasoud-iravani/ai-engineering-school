from text_analyzer import analyze_text, normalize_token, tokenize


def test_normalize_token() -> None:
    assert normalize_token("فارسی.") == "فارسی"


def test_tokenize() -> None:
    assert tokenize("AI, AI!") == ["ai", "ai"]


def test_analyze_text() -> None:
    report = analyze_text("زبان فارسی زبان")
    assert report["tokens"] == 3
    assert report["unique_tokens"] == 2
    assert report["top_tokens"][0] == ("زبان", 2)
