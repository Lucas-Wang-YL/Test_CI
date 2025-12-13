"""STDF File Generator for testing purposes"""

import struct
import random
from datetime import datetime
from typing import List


class STDFGenerator:
    """Generate sample STDF files for testing"""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.records: List[bytes] = []

    def generate_sample_file(self, num_tests: int = 10) -> None:
        """Generate a sample STDF file with test data"""
        # Add FAR (File Attribute Record)
        self._add_far()

        # Add MIR (Master Information Record)
        self._add_mir()

        # Add test records
        for i in range(num_tests):
            self._add_ptr(i + 1)

        # Add MRR (Master Results Record)
        self._add_mrr()

        # Write to file
        self._write_file()

    def _add_far(self) -> None:
        """Add File Attribute Record"""
        cpu_type = 2  # Sun
        stdf_ver = 4  # STDF V4
        data = struct.pack('<BB', cpu_type, stdf_ver)
        self._add_record(0x00, 0x0A, data)

    def _add_mir(self) -> None:
        """Add Master Information Record"""
        setup_time = int(datetime.now().timestamp())
        start_time = setup_time
        stat_num = 1
        mode_cod = ord('P')

        data = struct.pack('<IIBB', setup_time, start_time, stat_num, mode_cod)
        self._add_record(0x01, 0x0A, data)

    def _add_ptr(self, test_num: int) -> None:
        """Add Parametric Test Record"""
        result = random.uniform(1.0, 4.0)  # Random voltage 1-4V
        head_num = 1
        site_num = 1
        test_flg = 0

        # Simplified PTR structure
        data = struct.pack('<IBBBf', test_num, head_num, site_num, test_flg, result)
        self._add_record(0x0F, 0x05, data)

    def _add_mrr(self) -> None:
        """Add Master Results Record"""
        finish_time = int(datetime.now().timestamp())
        disp_cod = ord('A')

        data = struct.pack('<IB', finish_time, disp_cod)
        self._add_record(0x01, 0x14, data)

    def _add_record(self, rec_type: int, rec_sub: int, data: bytes) -> None:
        """Add a record to the file"""
        rec_len = len(data)
        header = struct.pack('<HBB', rec_len, rec_type, rec_sub)
        self.records.append(header + data)

    def _write_file(self) -> None:
        """Write all records to file"""
        with open(self.filepath, 'wb') as f:
            for record in self.records:
                f.write(record)


if __name__ == '__main__':
    # Example usage
    generator = STDFGenerator('sample.stdf')
    generator.generate_sample_file(num_tests=20)
    print('Sample STDF file generated: sample.stdf')
