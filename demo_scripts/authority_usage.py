# authority_usage.py

from dejan import get_authority

def main():
    # Example domain
    domain = "dejanmarketing.com"
    
    try:
        # Fetch the authority metric
        authority = get_authority(domain)
        print(f"Domain Authority for {domain}: {authority:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
