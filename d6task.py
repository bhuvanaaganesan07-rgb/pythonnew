items=[]

while True:
    item=input("Add item or done to finish: ")
    if item.lower()=="done":
        break
    items.append(item)

    print("Shopping list:")
    for i, item in enumerate(items, 1):
        print(f"{i} . {items}")

    print(f"Total: {len(items)} items")