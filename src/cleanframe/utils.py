def normalise_headers(headers):
    normalised_headers = []
    
    for h in headers:
        cleaned = h.strip().lower().replace(' ','_')
        normalised_headers.append(cleaned)
        
    return normalised_headers