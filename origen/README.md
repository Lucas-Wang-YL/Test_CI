# Test Program - Origen Project

Advantest 93K test program development using Origen framework.

## Setup

```bash
# Install dependencies
bundle install

# Generate patterns
origen generate pattern/example_pattern.rb -t v93k

# Run tests
bundle exec rspec

# Check code style
bundle exec rubocop
```

## Project Structure

```
origen/
├── config/              # Application configuration
├── lib/                 # Ruby source code
├── pattern/             # Pattern definitions
├── target/              # Target configurations (v93k)
├── spec/                # RSpec tests
└── output/              # Generated files (not tracked)
```

## CI/CD

This project uses GitHub Actions for continuous integration:
- Pattern generation validation
- RSpec unit tests
- RuboCop code style checks
- Automated test reports

## Version

- Test Program: 1.0.0
- Ruby: 2.6.x
- Origen: 0.60.x
