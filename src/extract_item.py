import pandas as pd

# Load the Excel file
file_path = 'src/paper_list.xlsx'  # Updated path as provided
xls = pd.ExcelFile(file_path)

# Function to process each sheet
def process_sheet(sheet_name):
    df = pd.read_excel(xls, sheet_name=sheet_name)
    # Drop rows where all values are NaN
    df = df.dropna(how='all')
    
    if sheet_name == 'L3':
        if len(df.columns) == 6:
            df.columns = ['Years', 'Data Agent', 'Paper', 'Link', 'Venue', 'Affiliation']
        relevant_cols = ['Data Agent', 'Paper', 'Link', 'Venue', 'Years', 'Affiliation']
        # Convert Years to integer to remove .0, handle NaN safely
        df['Years'] = df['Years'].apply(lambda x: int(x) if pd.notna(x) and x == x else '')
    elif sheet_name == 'survey':
        if len(df.columns) == 4:
            df.columns = ['Years', 'Paper', 'Link', 'Venue']
        relevant_cols = ['Paper', 'Link', 'Venue', 'Years']
        # Convert Years to integer to remove .0, handle NaN safely
        df['Years'] = df['Years'].apply(lambda x: int(x) if pd.notna(x) and x == x else '')
    else:
        if len(df.columns) == 7:
            df.columns = ['Category', 'Sub-domain', 'Data Agent', 'Paper', 'Link', 'Venue', 'Years']
        relevant_cols = ['Category', 'Sub-domain', 'Paper', 'Link', 'Venue', 'Years']
        # Forward fill Category and Sub-domain
        df['Category'] = df['Category'].ffill()
        df['Sub-domain'] = df['Sub-domain'].ffill()
        # Convert Years to integer to remove .0, handle NaN safely
        df['Years'] = df['Years'].apply(lambda x: int(x) if pd.notna(x) and x == x else '')
    
    df = df[relevant_cols].dropna(subset=['Link'], how='all')  # Keep if there's a link
    
    # Generate the formatted lines
    lines = []
    current_category = None
    current_subdomain = None
    
    for _, row in df.iterrows():
        if sheet_name == 'L3':
            data_agent = row['Data Agent'] if pd.notna(row['Data Agent']) else ''
            paper = row['Paper'] if pd.notna(row['Paper']) else ''
            link = row['Link'] if pd.notna(row['Link']) else ''
            venue = row['Venue'] if pd.notna(row['Venue']) else ''
            year = row['Years'] if pd.notna(row['Years']) else ''
            affiliation = row['Affiliation'] if pd.notna(row['Affiliation']) else ''
            
            data_agent = str(data_agent).strip()
            paper = str(paper).strip()
            link = str(link).strip()
            venue = str(venue).strip()
            year = str(year).strip()
            affiliation = str(affiliation).strip()
            
            if not link:
                continue
            
            if paper and paper != '/':
                line = f"- [{paper}]({link}) - *{venue} {year}*"
            else:
                line = f"- [{data_agent}]({link}) — *{affiliation}*"
            lines.append(line)
        elif sheet_name == 'survey':
            paper = row['Paper'] if pd.notna(row['Paper']) else ''
            link = row['Link'] if pd.notna(row['Link']) else ''
            venue = row['Venue'] if pd.notna(row['Venue']) else ''
            year = row['Years'] if pd.notna(row['Years']) else ''
            
            paper = str(paper).strip()
            link = str(link).strip()
            venue = str(venue).strip()
            year = str(year).strip()
            
            if not paper and not link:
                continue
            
            if paper and link:
                line = f"- [{paper}]({link}) - *{venue} {year}*"
            elif paper:
                line = f"- {paper} - *{venue} {year}*"
            else:
                line = f"- [{link}]({link}) - *{venue} {year}*"
            lines.append(line)
        else:
            category = row['Category'] if pd.notna(row['Category']) else ''
            subdomain = row['Sub-domain'] if pd.notna(row['Sub-domain']) else ''
            paper = row['Paper'] if pd.notna(row['Paper']) else ''
            link = row['Link'] if pd.notna(row['Link']) else ''
            venue = row['Venue'] if pd.notna(row['Venue']) else ''
            year = row['Years'] if pd.notna(row['Years']) else ''
            
            category = str(category).strip()
            subdomain = str(subdomain).strip()
            paper = str(paper).strip()
            link = str(link).strip()
            venue = str(venue).strip()
            year = str(year).strip()
            
            if not paper and not link:
                continue
            
            # Add category header if changed
            if category and category != current_category:
                lines.append(f"#### {category}")
                current_category = category
                current_subdomain = None  # Reset subdomain when category changes
            
            # Add subdomain header if changed
            if subdomain and subdomain != current_subdomain:
                lines.append(f"##### {subdomain}")
                current_subdomain = subdomain
            
            if paper and link:
                line = f"- [{paper}]({link}) - *{venue} {year}*"
            elif paper:
                line = f"- {paper} - *{venue} {year}*"
            else:
                line = f"- [{link}]({link}) - *{venue} {year}*"
            lines.append(line)
    
    # Write to txt file
    txt_filename = f"src/output/{sheet_name}.txt"
    with open(txt_filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    print(f"Generated: {txt_filename}")

# Process each sheet
sheets = ['L1', 'L2', 'L3', 'survey']
for sheet in sheets:
    process_sheet(sheet)

print("All files generated.")