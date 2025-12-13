#!/usr/bin/env python3
"""Command-line interface for STDF parser"""

import argparse
import sys
from pathlib import Path
from .parser import STDFParser
from .analyzer import STDFAnalyzer
from .generator import STDFGenerator


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description='STDF (Standard Test Data Format) Parser and Analyzer'
    )
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Parse command
    parse_parser = subparsers.add_parser('parse', help='Parse STDF file')
    parse_parser.add_argument('file', help='STDF file path')
    parse_parser.add_argument('--csv', help='Export to CSV file')
    parse_parser.add_argument('--summary', action='store_true', help='Show summary')

    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze STDF file')
    analyze_parser.add_argument('file', help='STDF file path')
    analyze_parser.add_argument('--report', help='Save report to file')

    # Generate command
    generate_parser = subparsers.add_parser('generate', help='Generate sample STDF file')
    generate_parser.add_argument('output', help='Output file path')
    generate_parser.add_argument('--tests', type=int, default=10, help='Number of tests')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    try:
        if args.command == 'parse':
            stdf_parser = STDFParser(args.file)
            result = stdf_parser.parse()

            if args.summary:
                print(stdf_parser.get_summary())

            if args.csv:
                stdf_parser.export_csv(args.csv)
                print(f'Results exported to: {args.csv}')

        elif args.command == 'analyze':
            stdf_parser = STDFParser(args.file)
            stdf_parser.parse()

            analyzer = STDFAnalyzer(stdf_parser)
            report = analyzer.generate_report()

            if args.report:
                with open(args.report, 'w') as f:
                    f.write(report)
                print(f'Report saved to: {args.report}')
            else:
                print(report)

        elif args.command == 'generate':
            generator = STDFGenerator(args.output)
            generator.generate_sample_file(num_tests=args.tests)
            print(f'Sample STDF file generated: {args.output}')

        return 0

    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
