import pytest

@pytest.fixture(scope='session', autouse=True)
def get_token():
    headers = {}

    headers["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6MSwiYXBwS2V5IjoibGV0c2JpbSIsImV4cGlyZSI6MTYyNTEyMTMxM30.EDF6KlLyvkFVuxKY5zNlrCYLcVu24LgkFLSczovOPww"

    yield headers
