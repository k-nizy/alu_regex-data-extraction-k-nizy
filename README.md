# alu_regex-data-extraction-k-nizy
 The regular expressions are designed to handle the most common formats while avoiding false positives.

# ALU Regex Data Extraction Tool

A powerful Python tool for extracting specific data patterns from text using regular expressions. Designed as a solution for junior full-stack developers to process large volumes of text data efficiently.

# Features

- Extracts "8 different data types" from text:
  - Email addresses
  - URLs
  - Phone numbers (multiple formats)
  - Credit card numbers
  - Time (12-hour and 24-hour formats)
  - HTML tags
  - Hashtags
  - Currency amounts
- Interactive menu system
- Sample data demonstration
- Custom text input option
- Selective field extraction

# Installation

   Clone the repository:

   git clone https://github.com/yourusername/alu_regex-data-extraction-yourusername.git
   cd alu_regex-data-extraction-yourusername

Ensure you have Python 3.6+ installed:


python --version
No additional dependencies required!

Usage

Run the script:

python data_extraction.py

And You'll be presented with two options:

Use sample data: Shows example text with all extractable data types

Enter custom text: Paste or type your own text to analyze

After choosing your text source, select which data types to extract by entering the corresponding numbers separated by commas.

Regex Patterns Used
Data Type	Pattern
Emails	\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b
URLs	https?://(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?(?=\s|$)
Phone Numbers	\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}
Credit Cards	\b(?:\d[ -]*?){13,16}\b
24hr Time	\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9]\b
12hr Time	\b(?:1[0-2]|0?[1-9]):[0-5][0-9]\s?(?:[AP]M|[ap]m)\b
HTML Tags	<[^>]+>
Hashtags	#\w+
Currency	\$[0-9]+(?:,[0-9]{3})*(?:\.[0-9]{2})?

Sample Output

=== DATA EXTRACTION TOOL ===
Choose an option:
1: Use sample data
2: Enter custom text
Your choice (1 or 2): 1

=== SAMPLE DATA ===
[Sample text displays here]

=== POTENTIAL EXTRACTIONS ===
[Lists all extractable items]
Available fields to extract:
1: Emails
2: URLs
3: Phone Numbers
4: Credit Card Numbers
5: Time (24-hour format)
6: Time (12-hour format)
7: HTML Tags
8: Hashtags
9: Currency Amounts
a: ALL fields

Enter numbers separated by commas (e.g., '1,2,8'):
Your selection: 1,2,8

=== EXTRACTION RESULTS ===
Emails: support@example.com, sales@company.co.uk
URLs: https://www.example.com, https://subdomain.example.org/page
Hashtags: #example, #ThisIsAHashtag


How to Use This System
   Launching the Tool
After installation, run the tool from your terminal:


python data_extraction.py
   Choosing Your Input Method
You'll see this menu:

=== DATA EXTRACTION TOOL ===
Choose an option:
1: Use sample data
2: Enter custom text
Your choice (1 or 2):
Option 1 (Sample Data):

The system will display pre-loaded text containing examples of all extractable data types

You'll see exactly what patterns the tool can detect

Option 2 (Custom Text):

Type or paste your text directly into the terminal

Press Ctrl+D (Mac/Linux) or Ctrl+Z then Enter (Windows) when finished

    Selecting Data to Extract
After choosing your text source, you'll see this selection menu:

Available fields to extract:
1: Emails
2: URLs
3: Phone Numbers
4: Credit Card Numbers
5: Time (24-hour format)
6: Time (12-hour format)
7: HTML Tags
8: Hashtags
9: Currency Amounts
a: ALL fields

Enter numbers separated by commas (e.g., '1,3,8'):
Examples of valid inputs:

1,3,8 → Extracts emails, phone numbers, and hashtags

a → Extracts all available data types

2,5,9 → Extracts URLs, 24-hour times, and currency amounts

   Viewing Results
The system will display formatted results like this:

=== EXTRACTION RESULTS ===
Emails: user@example.com, admin@test.org
URLs: https://example.com, http://test.org/page
Phone Numbers: (123) 456-7890, 555-123-4567




Contributing
Contributions are welcome! Please:

Fork the repository

Create a feature branch

Submit a pull request

