"""STDF Data Analyzer"""

import statistics
from typing import List, Dict, Any
from .parser import STDFParser, TestResult


class STDFAnalyzer:
    """Advanced STDF data analysis"""

    def __init__(self, parser: STDFParser):
        self.parser = parser
        self.test_results = parser.test_results

    def analyze_by_test(self) -> Dict[int, Dict[str, Any]]:
        """Analyze results grouped by test number"""
        test_groups: Dict[int, List[float]] = {}

        for result in self.test_results:
            if result.test_num not in test_groups:
                test_groups[result.test_num] = []
            test_groups[result.test_num].append(result.result)

        analysis = {}
        for test_num, values in test_groups.items():
            if values:
                analysis[test_num] = {
                    'count': len(values),
                    'mean': statistics.mean(values),
                    'median': statistics.median(values),
                    'stdev': statistics.stdev(values) if len(values) > 1 else 0.0,
                    'min': min(values),
                    'max': max(values)
                }

        return analysis

    def find_outliers(self, sigma: float = 3.0) -> List[TestResult]:
        """Find outlier test results using sigma method"""
        test_groups: Dict[int, List[TestResult]] = {}

        for result in self.test_results:
            if result.test_num not in test_groups:
                test_groups[result.test_num] = []
            test_groups[result.test_num].append(result)

        outliers = []
        for test_num, results in test_groups.items():
            if len(results) < 3:
                continue

            values = [r.result for r in results]
            mean = statistics.mean(values)
            stdev = statistics.stdev(values)

            for result in results:
                if abs(result.result - mean) > sigma * stdev:
                    outliers.append(result)

        return outliers

    def calculate_cpk(self, test_num: int) -> float:
        """Calculate Cpk (Process Capability Index) for a specific test"""
        results = [r for r in self.test_results if r.test_num == test_num]

        if not results or len(results) < 2:
            return 0.0

        values = [r.result for r in results]
        mean = statistics.mean(values)
        stdev = statistics.stdev(values)

        if stdev == 0:
            return 0.0

        # Use first result's limits
        usl = results[0].high_limit  # Upper Specification Limit
        lsl = results[0].low_limit   # Lower Specification Limit

        cpu = (usl - mean) / (3 * stdev)
        cpl = (mean - lsl) / (3 * stdev)

        return min(cpu, cpl)

    def get_failing_tests(self) -> List[TestResult]:
        """Get all failing test results"""
        return [r for r in self.test_results if not r.pass_fail]

    def generate_report(self) -> str:
        """Generate comprehensive analysis report"""
        analysis = self.analyze_by_test()
        failing = self.get_failing_tests()
        outliers = self.find_outliers()

        report = f"""
{'='*60}
STDF Data Analysis Report
{'='*60}

File: {self.parser.filepath}
Total Tests: {len(self.test_results)}
Unique Test Numbers: {len(analysis)}

Test Statistics:
{'-'*60}
"""

        for test_num, stats in analysis.items():
            cpk = self.calculate_cpk(test_num)
            report += f"""
Test #{test_num}:
  Count:    {stats['count']}
  Mean:     {stats['mean']:.4f}
  Median:   {stats['median']:.4f}
  Std Dev:  {stats['stdev']:.4f}
  Min:      {stats['min']:.4f}
  Max:      {stats['max']:.4f}
  Cpk:      {cpk:.2f}
"""

        report += f"""
{'-'*60}
Failing Tests: {len(failing)}
Outliers Detected: {len(outliers)}
{'-'*60}
"""

        return report
