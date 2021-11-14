# Must Need to know before working on Mail Merging Project



##### File Writing
```
with open("my_file_2.txt", mode = "w") as file:
    contents = file.write("new Text")

with open("my_file_2.txt", mode = "a") as file:
    contents = file.write("new Text")

```


##### File reading

```
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

```



##### replace() Method


```
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

```


##### strip() Method

```
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
```


