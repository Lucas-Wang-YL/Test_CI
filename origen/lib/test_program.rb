# frozen_string_literal: true

require 'origen'
require_relative '../config/application'

module TestProgram
  # Simple DUT (Device Under Test) model
  class Dut
    include Origen::TopLevel

    # Define pins
    def initialize(_options = {})
      add_pin :clk
      add_pin :data, size: 8
      add_pin :enable
      add_pin :reset
    end

    # Write data to device
    def write_data(value)
      pin(:enable).drive(1)
      pin(:data).drive(value)
      tester.cycle
      pin(:enable).drive(0)
    end

    # Read data from device
    def read_data(expected_value)
      pin(:enable).drive(1)
      tester.cycle
      pin(:data).assert(expected_value)
      pin(:enable).drive(0)
    end

    # Reset device
    def reset_device
      pin(:reset).drive(1)
      5.times { tester.cycle }
      pin(:reset).drive(0)
      tester.cycle
    end
  end
end
