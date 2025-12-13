"""Unit tests for STDF parser"""

import pytest
import tempfile
import os
from pathlib import Path
from stdf.parser import STDFParser
from stdf.generator import STDFGenerator
from stdf.analyzer import STDFAnalyzer


@pytest.fixture
def sample_stdf_file():
    """Generate a temporary STDF file for testing"""
    with tempfile.NamedTemporaryFile(mode='wb', suffix='.stdf', delete=False) as f:
        filepath = f.name

    generator = STDFGenerator(filepath)
    generator.generate_sample_file(num_tests=10)

    yield filepath

    # Cleanup
    if os.path.exists(filepath):
        os.remove(filepath)


def test_stdf_parser_initialization():
    """Test STDFParser initialization"""
    parser = STDFParser('test.stdf')
    assert parser.filepath == 'test.stdf'
    assert len(parser.records) == 0
    assert len(parser.test_results) == 0


def test_stdf_parse(sample_stdf_file):
    """Test parsing STDF file"""
    parser = STDFParser(sample_stdf_file)
    result = parser.parse()

    assert 'file_info' in result
    assert 'total_records' in result
    assert 'test_results' in result
    assert 'statistics' in result
    assert result['total_records'] > 0


def test_stdf_statistics(sample_stdf_file):
    """Test statistics calculation"""
    parser = STDFParser(sample_stdf_file)
    result = parser.parse()

    stats = result['statistics']
    assert 'total_tests' in stats
    assert 'pass_count' in stats
    assert 'fail_count' in stats
    assert 'yield_rate' in stats
    assert stats['total_tests'] == 10


def test_csv_export(sample_stdf_file):
    """Test CSV export functionality"""
    parser = STDFParser(sample_stdf_file)
    parser.parse()

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        csv_path = f.name

    try:
        parser.export_csv(csv_path)
        assert os.path.exists(csv_path)
        assert os.path.getsize(csv_path) > 0
    finally:
        if os.path.exists(csv_path):
            os.remove(csv_path)


def test_stdf_summary(sample_stdf_file):
    """Test summary generation"""
    parser = STDFParser(sample_stdf_file)
    parser.parse()

    summary = parser.get_summary()
    assert 'STDF File Analysis Summary' in summary
    assert 'Total Records' in summary
    assert 'Yield Rate' in summary


def test_analyzer_by_test(sample_stdf_file):
    """Test analyzer by test grouping"""
    parser = STDFParser(sample_stdf_file)
    parser.parse()

    analyzer = STDFAnalyzer(parser)
    analysis = analyzer.analyze_by_test()

    assert isinstance(analysis, dict)
    for test_num, stats in analysis.items():
        assert 'count' in stats
        assert 'mean' in stats
        assert 'median' in stats
        assert 'stdev' in stats


def test_outlier_detection(sample_stdf_file):
    """Test outlier detection"""
    parser = STDFParser(sample_stdf_file)
    parser.parse()

    analyzer = STDFAnalyzer(parser)
    outliers = analyzer.find_outliers(sigma=3.0)

    assert isinstance(outliers, list)


def test_cpk_calculation(sample_stdf_file):
    """Test Cpk calculation"""
    parser = STDFParser(sample_stdf_file)
    parser.parse()

    if parser.test_results:
        analyzer = STDFAnalyzer(parser)
        test_num = parser.test_results[0].test_num
        cpk = analyzer.calculate_cpk(test_num)

        assert isinstance(cpk, float)
        assert cpk >= 0


def test_failing_tests(sample_stdf_file):
    """Test finding failing tests"""
    parser = STDFParser(sample_stdf_file)
    parser.parse()

    analyzer = STDFAnalyzer(parser)
    failing = analyzer.get_failing_tests()

    assert isinstance(failing, list)


def test_generator():
    """Test STDF file generator"""
    with tempfile.NamedTemporaryFile(mode='wb', suffix='.stdf', delete=False) as f:
        filepath = f.name

    try:
        generator = STDFGenerator(filepath)
        generator.generate_sample_file(num_tests=5)

        assert os.path.exists(filepath)
        assert os.path.getsize(filepath) > 0

        # Verify it can be parsed
        parser = STDFParser(filepath)
        result = parser.parse()
        assert result['total_records'] > 0
    finally:
        if os.path.exists(filepath):
            os.remove(filepath)


def test_analysis_report(sample_stdf_file):
    """Test comprehensive analysis report"""
    parser = STDFParser(sample_stdf_file)
    parser.parse()

    analyzer = STDFAnalyzer(parser)
    report = analyzer.generate_report()

    assert 'STDF Data Analysis Report' in report
    assert 'Test Statistics' in report
    assert 'Failing Tests' in report
