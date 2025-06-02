import pytest
from threebodysolution.classifier import ShellDetector

def test_detector_initialization():
    detector = ShellDetector()
    assert hasattr(detector, "analyze")
