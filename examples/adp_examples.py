"""Example usage of ADP client."""

import asyncio
from axcpy.adp import ADPClient


async def main() -> None:
    """Main example function."""
    # Initialize client
    async with ADPClient(
        base_url="https://axcelerate.example.com/adp",
        api_key="your-api-key-here",
    ) as client:
        # List all cases
        print("Listing cases...")
        cases = await client.cases.list()
        print(f"Found {len(cases)} cases")

        # Get specific case
        if cases:
            case_id = cases[0]["id"]
            print(f"\nGetting case {case_id}...")
            case = await client.cases.get(case_id)
            print(f"Case: {case}")

        # Search documents
        print("\nSearching documents...")
        results = await client.search.query(
            query="contract AND date:[2020 TO 2023]",
            case_id=123,
        )
        print(f"Search results: {results}")


if __name__ == "__main__":
    asyncio.run(main())
