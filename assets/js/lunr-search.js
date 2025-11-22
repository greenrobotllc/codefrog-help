/**
 * Lunr.js search implementation for Jekyll help documentation
 * This builds the search index client-side from search.json
 */

(function() {
  'use strict';

  // Check if Lunr is available
  if (typeof lunr === 'undefined') {
    console.error('Lunr.js is not loaded. Please include lunr.min.js before this script.');
    return;
  }

  let searchIndex = null;
  let searchData = null;
  let searchInitialized = false;

  /**
   * Initialize search by loading data and building index
   */
  function initializeSearch(searchJsonUrl, searchInputId, resultsContainerId) {
    if (searchInitialized) {
      return Promise.resolve();
    }

    const searchInput = document.getElementById(searchInputId);
    const resultsContainer = document.getElementById(resultsContainerId);

    if (!searchInput || !resultsContainer) {
      console.error('Search elements not found');
      return Promise.reject('Search elements not found');
    }

    return fetch(searchJsonUrl)
      .then(function(response) {
        if (!response.ok) {
          throw new Error('Failed to load search data: ' + response.status);
        }
        return response.text();
      })
      .then(function(text) {
        // Try to parse JSON, with better error reporting
        let data;
        try {
          data = JSON.parse(text);
        } catch (e) {
          console.error('Invalid JSON in search.json:', e);
          console.error('JSON content:', text.substring(0, 500));
          throw new Error('Invalid JSON in search.json: ' + e.message);
        }
        searchData = data;

        // Build Lunr index - documents must be added inside the builder function
        searchIndex = lunr(function() {
          this.ref('id');
          this.field('title', { boost: 10 });
          this.field('content', { boost: 1 });
          
          // Add documents to index inside the builder
          searchData.forEach(function(doc) {
            this.add(doc);
          }, this);
        });

        searchInitialized = true;
        setupSearchHandlers(searchInput, resultsContainer);
      })
      .catch(function(error) {
        console.error('Error initializing search:', error);
        resultsContainer.innerHTML = '<li>Search unavailable</li>';
      });
  }

  /**
   * Setup search input handlers
   */
  function setupSearchHandlers(searchInput, resultsContainer) {
    let searchTimeout;

    // Search on input with debounce
    searchInput.addEventListener('input', function() {
      clearTimeout(searchTimeout);
      const query = this.value.trim();

      if (query.length === 0) {
        resultsContainer.style.display = 'none';
        resultsContainer.innerHTML = '';
        return;
      }

      searchTimeout = setTimeout(function() {
        performSearch(query, resultsContainer);
      }, 150);
    });

    // Handle Enter key to navigate to first result
    searchInput.addEventListener('keydown', function(e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        const firstResult = resultsContainer.querySelector('li a');
        if (firstResult) {
          window.location.href = firstResult.href;
        }
      }
    });

    // Hide results when clicking outside
    document.addEventListener('click', function(e) {
      if (!searchInput.contains(e.target) && !resultsContainer.contains(e.target)) {
        resultsContainer.style.display = 'none';
      }
    });
  }

  /**
   * Perform search and display results
   */
  function performSearch(query, resultsContainer) {
    if (!searchIndex || !searchData) {
      return;
    }

    try {
      const results = searchIndex.search(query);
      const maxResults = 20;
      const limitedResults = results.slice(0, maxResults);

      if (limitedResults.length === 0) {
        resultsContainer.innerHTML = '<li>No results found</li>';
        resultsContainer.style.display = 'block';
        return;
      }

      let html = '';
      limitedResults.forEach(function(result) {
        const item = searchData.find(function(d) {
          return d.id === result.ref;
        });
        if (item) {
          html += '<li><a href="' + escapeHtml(item.url) + '">' + 
                  escapeHtml(item.title) + '</a></li>';
        }
      });

      resultsContainer.innerHTML = html;
      resultsContainer.style.display = 'block';
    } catch (err) {
      console.error('Search error:', err);
      resultsContainer.innerHTML = '<li>Search error occurred</li>';
      resultsContainer.style.display = 'block';
    }
  }

  /**
   * Escape HTML to prevent XSS
   */
  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Auto-initialize if elements exist
  if (document.getElementById('search-input') && document.getElementById('results-container')) {
    const searchJsonUrl = document.querySelector('meta[name="search-json-url"]')?.content || 
                         '/search.json';
    initializeSearch(searchJsonUrl, 'search-input', 'results-container');
  }

  // Export for manual initialization
  window.LunrSearch = {
    init: initializeSearch
  };
})();

