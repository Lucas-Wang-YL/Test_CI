"""STDF File Parser for semiconductor test data"""

import struct
from typing import Dict, List, Any, BinaryIO
from dataclasses import dataclass
from enum import IntEnum


class RecordType(IntEnum):
    """STDF Record Types"""
    FAR = 0x00_0A  # File Attribute Record
    MIR = 0x01_0A  # Master Information Record
    MRR = 0x01_14  # Master Results Record
    PCR = 0x01_1E  # Part Count Record
    PTR = 0x0F_05  # Parametric Test Record
    FTR = 0x0F_14  # Functional Test Record
    PIR = 0x05_0A  # Part Information Record
    PRR = 0x05_14  # Part Results Record


@dataclass
class STDFRecord:
    """Base STDF Record"""
    rec_type: int
    rec_sub: int
    rec_len: int
    data: bytes


@dataclass
class TestResult:
    """Parsed test result"""
    test_num: int
    test_name: str
    result: float
    unit: str
    low_limit: float
    high_limit: float
    pass_fail: bool


class STDFParser:
    """STDF file parser for semiconductor test data"""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.records: List[STDFRecord] = []
        self.test_results: List[TestResult] = []
        self.file_info: Dict[str, Any] = {}

    def parse(self) -> Dict[str, Any]:
        """Parse STDF file and extract test data"""
        with open(self.filepath, 'rb') as f:
            self._read_records(f)
            self._extract_test_results()

        return {
            'file_info': self.file_info,
            'total_records': len(self.records),
            'test_results': self.test_results,
            'statistics': self._calculate_statistics()
        }

    def _read_records(self, f: BinaryIO) -> None:
        """Read all records from STDF file"""
        while True:
            header = f.read(4)
            if len(header) < 4:
                break

            rec_len, rec_type, rec_sub = struct.unpack('<HBB', header)
            data = f.read(rec_len)

            record = STDFRecord(rec_type, rec_sub, rec_len, data)
            self.records.append(record)

            # Parse specific record types
            self._parse_record(record)

    def _parse_record(self, record: STDFRecord) -> None:
        """Parse specific record types"""
        rec_id = (record.rec_type << 8) | record.rec_sub

        if rec_id == RecordType.MIR:
            self._parse_mir(record.data)
        elif rec_id == RecordType.PTR:
            self._parse_ptr(record.data)

    def _parse_mir(self, data: bytes) -> None:
        """Parse Master Information Record"""
        # Simplified MIR parsing
        if len(data) >= 8:
            setup_time = struct.unpack('<I', data[0:4])[0]
            start_time = struct.unpack('<I', data[4:8])[0]
            self.file_info['setup_time'] = setup_time
            self.file_info['start_time'] = start_time

    def _parse_ptr(self, data: bytes) -> None:
        """Parse Parametric Test Record (simplified)"""
        if len(data) < 8:
            return

        try:
            test_num = struct.unpack('<I', data[0:4])[0]
            result = struct.unpack('<f', data[4:8])[0]

            # Simplified - in real STDF, need to parse full PTR structure
            test_result = TestResult(
                test_num=test_num,
                test_name=f'Test_{test_num}',
                result=result,
                unit='V',
                low_limit=0.0,
                high_limit=5.0,
                pass_fail=(0.0 <= result <= 5.0)
            )
            self.test_results.append(test_result)
        except struct.error:
            pass

    def _extract_test_results(self) -> None:
        """Extract and organize test results"""
        # Additional processing can be added here
        pass

    def _calculate_statistics(self) -> Dict[str, Any]:
        """Calculate test statistics"""
        if not self.test_results:
            return {
                'total_tests': 0,
                'pass_count': 0,
                'fail_count': 0,
                'yield_rate': 0.0
            }

        pass_count = sum(1 for t in self.test_results if t.pass_fail)
        fail_count = len(self.test_results) - pass_count

        return {
            'total_tests': len(self.test_results),
            'pass_count': pass_count,
            'fail_count': fail_count,
            'yield_rate': (pass_count / len(self.test_results) * 100) if self.test_results else 0.0
        }

    def export_csv(self, output_path: str) -> None:
        """Export test results to CSV"""
        import csv

        with open(output_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Test Number', 'Test Name', 'Result', 'Unit', 'Low Limit', 'High Limit', 'Pass/Fail'])

            for test in self.test_results:
                writer.writerow([
                    test.test_num,
                    test.test_name,
                    test.result,
                    test.unit,
                    test.low_limit,
                    test.high_limit,
                    'PASS' if test.pass_fail else 'FAIL'
                ])

    def get_summary(self) -> str:
        """Get human-readable summary"""
        stats = self._calculate_statistics()
        return f"""
STDF File Analysis Summary
{'=' * 50}
File: {self.filepath}
Total Records: {len(self.records)}
Total Tests: {stats['total_tests']}
Pass Count: {stats['pass_count']}
Fail Count: {stats['fail_count']}
Yield Rate: {stats['yield_rate']:.2f}%
{'=' * 50}
"""
