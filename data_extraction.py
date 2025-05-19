import re

def extract_data(text, selected_fields):
    """
    Extracts various data types from text using regular expressions.
    
    Args:
        text (str): The input text to search through
        selected_fields (list): List of field names to extract
        
    Returns:
        dict: A dictionary containing lists of extracted data for each selected type
    """
    results = {}
    
    # Define all possible patterns
    patterns = {
        'emails': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'urls': r'https?://(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?(?=\s|$)',
        'phone_numbers': r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
        'credit_cards': r'\b(?:\d[ -]*?){13,16}\b',
        'time_24hr': r'\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9]\b',
        'time_12hr': r'\b(?:1[0-2]|0?[1-9]):[0-5][0-9]\s?(?:[AP]M|[ap]m)\b',
        'html_tags': r'<[^>]+>',
        'hashtags': r'#\w+',
        'currency': r'\$[0-9]+(?:,[0-9]{3})*(?:\.[0-9]{2})?'
    }
    
    # Only extract the selected fields
    for field in selected_fields:
        if field in patterns:
            results[field] = re.findall(patterns[field], text)
    
    return results

def display_sample_data():
    """Displays the sample data with all possible extractable items marked"""
    sample_text = """
    Contact us at support@example.com or sales@company.co.uk for assistance.
    Visit our website at https://www.example.com or https://subdomain.example.org/page.
    Call us at (123) 456-7890, 123-456-7890, or 123.456.7890.
    Payment options: 1234 5678 9012 3456 or 1234-5678-9012-3456.
    Store hours: 14:30 (24hr) or 2:30 PM (12hr).
    HTML content: <p>Hello</p> <div class="sample">Content</div>.
    Social media: #example #ThisIsAHashtag.
    Product prices: $19.99 or $1,234.56.
    """
    print("\n=== SAMPLE DATA ===")
    print(sample_text)
    print("=== POTENTIAL EXTRACTIONS ===")
    print("Emails: support@example.com, sales@company.co.uk")
    print("URLs: https://www.example.com, https://subdomain.example.org/page")
    print("Phone Numbers: (123) 456-7890, 123-456-7890, 123.456.7890")
    print("Credit Cards: 1234 5678 9012 3456, 1234-5678-9012-3456")
    print("24hr Time: 14:30")
    print("12hr Time: 2:30 PM")
    print("HTML Tags: <p>, <div class=\"sample\">")
    print("Hashtags: #example, #ThisIsAHashtag")
    print("Currency: $19.99, $1,234.56")
    print("==================\n")
    return sample_text

def get_user_fields():
    """Prompts user to select which fields to extract"""
    available_fields = {
        '1': 'emails',
        '2': 'urls',
        '3': 'phone_numbers',
        '4': 'credit_cards',
        '5': 'time_24hr',
        '6': 'time_12hr',
        '7': 'html_tags',
        '8': 'hashtags',
        '9': 'currency',
        'a': 'all'
    }
    
    print("\nAvailable fields to extract:")
    print("1: Emails")
    print("2: URLs")
    print("3: Phone Numbers")
    print("4: Credit Card Numbers")
    print("5: Time (24-hour format)")
    print("6: Time (12-hour format)")
    print("7: HTML Tags")
    print("8: Hashtags")
    print("9: Currency Amounts")
    print("a: ALL fields")
    print("\nEnter numbers separated by commas (e.g., '1,3,8'):")
    
    while True:
        choices = input("Your selection: ").strip().lower().split(',')
        selected = []
        
        if 'a' in choices:
            return [f for f in available_fields.values() if f != 'all']
        
        for choice in choices:
            if choice in available_fields and available_fields[choice] != 'all':
                selected.append(available_fields[choice])
        
        if selected:
            return list(set(selected))  # Remove duplicates
        print("Invalid selection. Please try again.")

def main():
    print("=== DATA EXTRACTION TOOL ===")
    print("Choose an option:")
    print("1: Use sample data")
    print("2: Enter custom text")
    
    choice = input("Your choice (1 or 2): ").strip()
    
    if choice == '1':
        text = display_sample_data()
    elif choice == '2':
        print("\nEnter your text (press Ctrl+D when done):")
        text = ""
        try:
            while True:
                text += input() + "\n"
        except EOFError:
            pass
    else:
        print("Invalid choice. Using sample data by default.")
        text = display_sample_data()
    
    selected_fields = get_user_fields()
    extracted_data = extract_data(text, selected_fields)
    
    print("\n=== EXTRACTION RESULTS ===")
    for field, values in extracted_data.items():
        print(f"{field.capitalize()}: {', '.join(values) if values else 'None found'}")

if __name__ == "__main__":
    main()