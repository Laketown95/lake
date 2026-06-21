import requests
import sys

def main():
    """
    Calculates the total cost of bitcoins in USD based on the current price.
    """
    try:
        # Check if a command-line argument is provided
        if len(sys.argv) != 2:
            print("Usage: python bitcoin.py <number of bitcoins>")
            sys.exit(1)

        # Get the number of bitcoins from the command-line argument
        try:
            num_bitcoins = float(sys.argv[1])
        except ValueError:
            print("Error: Invalid input. Please provide a valid number.")
            sys.exit(1)

        # Fetch the current Bitcoin price from the CoinCap API
        try:
            response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
            response.raise_for_status()  # Raise an exception for bad status codes
            data = response.json()
            price_usd = float(data["data"]["priceUsd"])
        except requests.exceptions.RequestException as e:
            print(f"Error: Could not fetch Bitcoin price: {e}")
            sys.exit(1)

        # Calculate the total cost
        total_cost = num_bitcoins * price_usd

        # Format the total cost with commas and four decimal places
        formatted_cost = "{:,.4f}".format(total_cost)

        # Print the formatted cost
        print(f"${formatted_cost}")

    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
