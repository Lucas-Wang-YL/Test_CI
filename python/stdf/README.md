# STDF Parser

Standard Test Data Format (STDF) parser for semiconductor test data analysis.

## Features

- ✅ Parse STDF V4 binary files
- ✅ Extract test results and statistics
- ✅ Calculate yield rate and Cpk
- ✅ Detect outliers
- ✅ Export to CSV
- ✅ Generate sample files for testing
- ✅ Command-line interface

## Installation

```bash
cd python/stdf
pip install -r requirements.txt
```

## Usage

### Python API

```python
from stdf import STDFParser
from stdf.analyzer import STDFAnalyzer

# Parse STDF file
parser = STDFParser('test_data.stdf')
result = parser.parse()

# Get summary
print(parser.get_summary())

# Export to CSV
parser.export_csv('results.csv')

# Advanced analysis
analyzer = STDFAnalyzer(parser)
report = analyzer.generate_report()
print(report)

# Find outliers
outliers = analyzer.find_outliers(sigma=3.0)

# Calculate Cpk
cpk = analyzer.calculate_cpk(test_num=1)
```

### Command Line

```bash
# Parse STDF file
python -m stdf.cli parse test_data.stdf --summary

# Export to CSV
python -m stdf.cli parse test_data.stdf --csv results.csv

# Analyze with report
python -m stdf.cli analyze test_data.stdf --report report.txt

# Generate sample file
python -m stdf.cli generate sample.stdf --tests 20
```

## STDF Record Types Supported

- FAR (File Attribute Record)
- MIR (Master Information Record)
- MRR (Master Results Record)
- PTR (Parametric Test Record)
- PIR (Part Information Record)
- PRR (Part Results Record)

## Test Data Structure

```
TestResult:
  - test_num: Test number
  - test_name: Test name
  - result: Measured value
  - unit: Unit (V, A, Ω, etc.)
  - low_limit: Lower specification limit
  - high_limit: Upper specification limit
  - pass_fail: Pass/Fail status
```

## Statistics Calculated

- Total tests count
- Pass/Fail counts
- Yield rate (%)
- Mean, Median, Std Dev
- Min/Max values
- Cpk (Process Capability Index)
- Outlier detection (3-sigma method)

## Example Output

```
STDF File Analysis Summary
==================================================
File: test_data.stdf
Total Records: 100
Total Tests: 50
Pass Count: 48
Fail Count: 2
Yield Rate: 96.00%
==================================================
```

## Requirements

- Python 3.7+
- No external dependencies for basic parsing
- Optional: pandas, matplotlib for advanced analysis

## Author

Lucas Wang - Semiconductor Test Engineer
