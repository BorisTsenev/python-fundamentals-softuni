demo = "example"
substring = "amp"

if substring in demo:
    demo = demo.replace(substring, "")

print(demo)