#!/usr/bin/env python3
"""Example usage of STDF parser"""

from stdf.parser import STDFParser
from stdf.analyzer import STDFAnalyzer
from stdf.generator import STDFGenerator


def example_generate_and_parse():
    """Generate sample STDF file and parse it"""
    print("=" * 60)
    print("Example: Generate and Parse STDF File")
    print("=" * 60)

    # Generate sample file
    print("\n1. Generating sample STDF file...")
    generator = STDFGenerator('example_test_data.stdf')
    generator.generate_sample_file(num_tests=20)
    print("   ✓ Generated: example_test_data.stdf")

    # Parse the file
    print("\n2. Parsing STDF file...")
    parser = STDFParser('example_test_data.stdf')
    result = parser.parse()
    print(f"   ✓ Found {result['total_records']} records")
    print(f"   ✓ Extracted {result['statistics']['total_tests']} test results")

    # Display summary
    print("\n3. Summary:")
    print(parser.get_summary())

    # Export to CSV
    print("\n4. Exporting to CSV...")
    parser.export_csv('example_results.csv')
    print("   ✓ Exported to: example_results.csv")

    return parser


def example_analysis():
    """Perform advanced analysis"""
    print("\n" + "=" * 60)
    print("Example: Advanced Analysis")
    print("=" * 60)

    # Generate and parse
    parser = STDFParser('example_test_data.stdf')
    parser.parse()

    # Create analyzer
    analyzer = STDFAnalyzer(parser)

    # Analyze by test
    print("\n1. Test-by-test analysis:")
    analysis = analyzer.analyze_by_test()
    for test_num, stats in list(analysis.items())[:3]:  # Show first 3
        print(f"\n   Test #{test_num}:")
        print(f"      Mean:   {stats['mean']:.4f}")
        print(f"      StdDev: {stats['stdev']:.4f}")
        cpk = analyzer.calculate_cpk(test_num)
        print(f"      Cpk:    {cpk:.2f}")

    # Find outliers
    print("\n2. Outlier detection:")
    outliers = analyzer.find_outliers(sigma=3.0)
    print(f"   Found {len(outliers)} outliers (3-sigma method)")

    # Get failing tests
    print("\n3. Failing tests:")
    failing = analyzer.get_failing_tests()
    print(f"   Found {len(failing)} failing tests")

    # Generate report
    print("\n4. Generating comprehensive report...")
    report = analyzer.generate_report()
    with open('example_analysis_report.txt', 'w') as f:
        f.write(report)
    print("   ✓ Report saved to: example_analysis_report.txt")


def example_cli_usage():
    """Show CLI usage examples"""
    print("\n" + "=" * 60)
    print("CLI Usage Examples")
    print("=" * 60)

    examples = [
        "# Parse STDF file with summary",
        "python -m stdf.cli parse test_data.stdf --summary",
        "",
        "# Export to CSV",
        "python -m stdf.cli parse test_data.stdf --csv results.csv",
        "",
        "# Analyze with report",
        "python -m stdf.cli analyze test_data.stdf --report report.txt",
        "",
        "# Generate sample file",
        "python -m stdf.cli generate sample.stdf --tests 50",
    ]

    for line in examples:
        print(f"  {line}")


if __name__ == '__main__':
    # Run examples
    example_generate_and_parse()
    example_analysis()
    example_cli_usage()

    print("\n" + "=" * 60)
    print("Examples completed successfully!")
    print("=" * 60)
    print("\nGenerated files:")
    print("  - example_test_data.stdf")
    print("  - example_results.csv")
    print("  - example_analysis_report.txt")
