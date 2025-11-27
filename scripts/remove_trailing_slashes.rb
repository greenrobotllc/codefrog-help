#!/usr/bin/env ruby
# Script to remove trailing slashes from void elements in HTML files
# This fixes HTML5 validation warnings

# Void elements in HTML5 that should not have trailing slashes
VOID_ELEMENTS = %w[
  area base br col embed hr img input link meta param source track wbr
].freeze

def process_file(file_path)
  content = File.read(file_path)
  original_content = content.dup
  
  VOID_ELEMENTS.each do |element|
    # Pattern 1: <element ... /> -> <element ...>
    # Matches void elements with attributes and trailing slash
    content.gsub!(/<#{element}\s+([^>]*?)\s*\/>/i) do
      attrs = $1.strip
      "<#{element} #{attrs}>"
    end
    
    # Pattern 2: <element /> -> <element>
    # Matches self-closing void elements without attributes
    content.gsub!(/<#{element}\s*\/>/i, "<#{element}>")
  end
  
  # Only write if content changed
  if content != original_content
    File.write(file_path, content)
    puts "Processed: #{file_path}"
  end
end

# Process all HTML files in _site directory
if ARGV.empty?
  puts "Usage: #{$0} <directory>"
  puts "Example: #{$0} _site"
  exit 1
end

dir = ARGV[0]
unless File.directory?(dir)
  puts "Error: Directory not found: #{dir}"
  exit 1
end

html_files = Dir.glob(File.join(dir, "**", "*.html"))
puts "Found #{html_files.length} HTML files to process..."

html_files.each do |file|
  process_file(file)
end

puts "Done! Processed #{html_files.length} files."

