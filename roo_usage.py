from dejan import get_roo

def main():
    # Mapping of search engines to their corresponding identifiers
    search_engines = {
        2: "google.com/desktop",
        3: "google.com.au/desktop",
        4: "google.com/mobile",
        5: "google.com.au/mobile"
    }
    
    # Choose the search engine by setting the appropriate identifier
    search_engine = 2  # Change this number to select a different search engine:
                       # 2: google.com/desktop
                       # 3: google.com.au/desktop
                       # 4: google.com/mobile
                       # 5: google.com.au/mobile
    
    # Fetch data as a pandas DataFrame
    roo_data = get_roo(search_engine, as_dataframe=True)
    
    # Display the first few rows of the DataFrame
    print(f"Data for search engine {search_engine} ({search_engines[search_engine]}):")
    print(roo_data.head())

if __name__ == "__main__":
    main()
