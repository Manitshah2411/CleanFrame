from cleanframe.utils import normalise_headers

# Checks the basic expected behavior of the method
def test_normalise_headers_basic():
    headers = [" User ID ", "Total Sales", " Age"]
    result = normalise_headers(headers)

    assert result == ["user_id", "total_sales", "age"]
    
# Checks that if the passed argument is an empty list than the output should also be an empty list
def test_normalise_headers_empty_list():
    headers = []
    result = normalise_headers(headers)
    assert result == []
      
# Checks no unnecessary changes on perfect inputs
def test_normalise_headers_idempotent():
    headers = ['user_id', 'age']
    result = normalise_headers(headers)
    assert result == headers
    
# Checks multiple spaces replacing by an underscore(_)    
def test_normalise_headers_multiple_spaces():
    headers = [" Total   Sales "]
    result = normalise_headers(headers)
    assert result == ["total___sales"]