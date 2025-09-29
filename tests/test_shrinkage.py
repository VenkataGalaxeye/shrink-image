# tests/test_enlarge.py


from pathlib import Path
import pytest
from shrink.shrink import enlarge
from PIL import Image


def test_shrink_creates_file(tmp_path):
    # Arrange
    input_file = tmp_path / "test.png"

    # Create a minimal PNG image
    img = Image.new("RGB", (10, 10), color="white")
    img.save(input_file)

    output_dir = tmp_path / "output"

    # Act
    result = enlarge(str(input_file), str(output_dir))

    # Assert
    result_path = Path(result)
    assert result_path.exists()
    assert str(result_path).startswith(str(output_dir))
    assert str(result_path).endswith("_shrunk.png")


def test_enlarge_invalid_file(tmp_path):
    # Act & Assert
    with pytest.raises(ValueError):
        enlarge(str(tmp_path / "nonexistent.png"), str(tmp_path))
