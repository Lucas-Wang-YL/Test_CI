# frozen_string_literal: true

require 'spec_helper'

describe 'TestProgram' do
  describe 'Version' do
    it 'has a version number' do
      expect(TestProgram::VERSION).not_to be_nil
      expect(TestProgram::VERSION).to eq('1.0.0')
    end

    it 'reports Origen version' do
      expect(TestProgram::ORIGEN_VERSION).not_to be_nil
    end
  end

  describe 'Application' do
    it 'loads application config' do
      expect(TestProgram::Application).to be_a(Class)
    end

    it 'has a name configured' do
      app = TestProgram::Application.new
      expect(app.config.name).not_to be_nil
    end

    it 'has version method' do
      app = TestProgram::Application.new
      expect(app.version).to eq('1.0.0')
    end
  end

  describe 'DUT Model Class' do
    it 'is defined' do
      expect(TestProgram::Dut).to be_a(Class)
    end

    it 'includes Origen::TopLevel' do
      expect(TestProgram::Dut.included_modules).to include(Origen::TopLevel)
    end
  end
end
