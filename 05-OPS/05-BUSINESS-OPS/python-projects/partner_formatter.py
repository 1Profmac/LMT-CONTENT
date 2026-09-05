import csv

# Open the CSV file and read the partner contacts
with open("partners.csv") as file:
    reader = csv.DictReader(file)
    partners = list(reader)

# Print a header
print("=" * 50)
print("50+TechBridge Partner Contacts")
print(f"Total partners: {len(partners)}")
print("=" * 50)

# Loop through each partner and print formatted info
for partner in partners:
    print(f"\n  Name:    {partner['name']}")
    print(f"  Org:     {partner['organization']}")
    print(f"  Email:   {partner['email']}")
    print(f"  Type:    {partner['type']}")
    print(f"  City:    {partner['city']}")
    print("-" * 50)

# Show a summary by type
print("\n--- Summary by Type ---")
types = {}
for partner in partners:
    t = partner["type"]
    if t in types:
        types[t] += 1
    else:
        types[t] = 1

for t, count in types.items():
    print(f"  {t}: {count}")
