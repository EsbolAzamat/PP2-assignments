import json

with open("sample-data.json", "r") as f:
    data = json.load(f)

interface = data["imdata"]

print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20} {'Speed':8} {'MTU':6}")
print("-------------------------------------------------- --------------------  ------  ------")

for item in interface:
    atr = item["l1PhysIf"]["attributes"]

    dn = atr["dn"]
    speed = atr["speed"]
    mtu = atr["mtu"]
    print(f"{dn:50} {" ":20} {speed:8} {mtu:6}")

