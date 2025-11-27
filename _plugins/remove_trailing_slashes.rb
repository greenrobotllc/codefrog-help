# Jekyll plugin to remove trailing slashes from void elements
# This fixes HTML5 validation warnings about trailing slashes on void elements
# Uses Jekyll hooks to process rendered HTML output

module Jekyll
  module RemoveTrailingSlashes
    # Void elements in HTML5 that should not have trailing slashes
    VOID_ELEMENTS = %w[
      area base br col embed hr img input link meta param source track wbr
    ].freeze

    def self.remove_trailing_slashes(html)
      return html unless html.is_a?(String)

      result = html.dup
      
      VOID_ELEMENTS.each do |element|
        # Pattern 1: <element ... /> -> <element ...>
        # Matches void elements with attributes and trailing slash
        result.gsub!(/<#{element}\s+([^>]*?)\s*\/>/i) do |match|
          attrs = $1
          # Clean up any extra spaces before the closing
          attrs = attrs.strip
          "<#{element} #{attrs}>"
        end
        
        # Pattern 2: <element /> -> <element>
        # Matches self-closing void elements without attributes
        result.gsub!(/<#{element}\s*\/>/i, "<#{element}>")
      end
      
      result
    end
  end
end

# Hook into page rendering to process HTML output
Jekyll::Hooks.register :pages, :post_render do |page|
  if page.output_ext == '.html' && page.output
    page.output = Jekyll::RemoveTrailingSlashes.remove_trailing_slashes(page.output)
  end
end

# Hook into post rendering to process HTML output
Jekyll::Hooks.register :posts, :post_render do |post|
  if post.output_ext == '.html' && post.output
    post.output = Jekyll::RemoveTrailingSlashes.remove_trailing_slashes(post.output)
  end
end

# Hook into documents rendering to process HTML output
Jekyll::Hooks.register :documents, :post_render do |doc|
  if doc.output_ext == '.html' && doc.output
    doc.output = Jekyll::RemoveTrailingSlashes.remove_trailing_slashes(doc.output)
  end
end

