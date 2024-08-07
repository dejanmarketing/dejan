## Dejan: SEO Machine Learning Utilities

Dejan is a growing collection of SEO-related machine learning utilities designed to assist with various tasks in the field of search engine optimization. This repository will be continuously updated with new tools and features aimed at helping SEO professionals streamline their workflows using advanced ML techniques.

### Installation

You can install the package using pip:

```bash
pip install dejan
```

### Current Utilities

#### roo

**Purpose:** Fetches and processes data from the Algoroo API, providing insights into search engine fluctuations.

**Search Engine Options:**

* 2: Google.com (Desktop)
* 3: Google.com.au (Desktop)
* 4: Google.com (Mobile)
* 5: Google.com.au (Mobile)

**Output:** The data can be returned either as a raw JSON object or as a pandas DataFrame for further analysis.

**Example Usage:**

```python
from dejan import roo

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
    roo_data = roo.get_roo(search_engine, as_dataframe=True)
    
    # Display the first few rows of the DataFrame
    print(f"Data for search engine {search_engine} ({search_engines[search_engine]}):")
    print(roo_data.head())

if __name__ == "__main__":
    main()

```

#### linkbert

**Purpose:** Uses the LinkBERT model to predict link tokens in the provided text, useful for analyzing link placement within content.

**Grouping Modes:**

* `subtoken`: Returns individual subword tokens classified as links.
* `token`: Merges any subtokens into whole tokens (words).
* `phrase`: Groups predictions into phrases, treating the entire phrase as a link if any part of it is classified as a link.

**Example Usage:**

```python
from dejan import linkbert

def main():
    # Initialize the LinkBERTInference model
    model = linkbert.LinkBERTInference()

    # Sample text for prediction
    text = "LinkBERT is a model developed by Dejan Marketing designed to predict natural link placement within web content."

    print("Input Text:")
    print(text)
    print("-" * 50)

    # Group by subtoken
    links_subtoken = model.predict_link_tokens(text, group="subtoken")
    print(f"Predicted link tokens (subtoken): {links_subtoken}")

    # Group by token
    links_token = model.predict_link_tokens(text, group="token")
    print(f"Predicted link tokens (token): {links_token}")

    # Group by phrase
    links_phrase = model.predict_link_tokens(text, group="phrase")
    print(f"Predicted link tokens (phrase): {links_phrase}")

if __name__ == "__main__":
    main()
```

#### dirtree

**Purpose:** Generates an ASCII representation of the directory tree structure from any given root directory, including all subdirectories and files.

**Usage:** This tool can be particularly useful for visualizing file structures in complex projects, making it easier to manage and navigate large SEO datasets.

**Example Usage:**

```python
from dejan import generate_ascii_tree

# Generate and print the directory tree for the current directory
generate_ascii_tree()
```

