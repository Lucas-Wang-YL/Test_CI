# frozen_string_literal: true

# Functional test pattern
Pattern.create do
  ss 'Functional Test Pattern'
  ss 'Testing basic device functionality'

  # Reset sequence
  $dut.reset_device

  # Clock test - toggle clock pin
  ss '--- Clock Test ---'
  20.times do
    $dut.pin(:clk).drive(1)
    tester.cycle
    $dut.pin(:clk).drive(0)
    tester.cycle
  end

  # Data pattern test
  ss '--- Data Pattern Test ---'
  [0x00, 0xFF, 0xAA, 0x55, 0x0F, 0xF0].each do |pattern|
    $dut.write_data(pattern)
    $dut.read_data(pattern)
  end

  ss '--- Functional Test Complete ---'
end
