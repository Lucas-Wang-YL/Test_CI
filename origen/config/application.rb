require 'origen'

module TestProgram
  class Application < Origen::Application
    
    # Application configuration
    config.name = 'test_program'
    config.initials = 'TP'
    
    # Tester configuration - Advantest 93K
    config.target_default = :v93k
    
    # Pattern output directory
    config.pattern_prefix = 'test_'
    config.pattern_output_directory = "#{Origen.root}/output/patterns"
    
    # Test program information
    def version
      '1.0.0'
    end
    
    def test_engineer
      ENV['USER'] || 'test_engineer'
    end
  end
end
