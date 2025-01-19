def categorize_by_vendor(vendor_name):
    """
    Categorize invoices by vendor name.

    Args:
        vendor_name (str): The name of the vendor.

    Returns:
        str: The category of the vendor. Returns 'Unknown' if the vendor is not found in the categories.
    """
    # Define categories for known vendors
    categories = {
        'VendorA': 'Category1',
        'VendorB': 'Category2',
        # Add more vendor categories as needed
    }
    
    # Return the category for the given vendor name, or 'Unknown' if the vendor is not in the categories
    return categories.get(vendor_name, 'Unknown')