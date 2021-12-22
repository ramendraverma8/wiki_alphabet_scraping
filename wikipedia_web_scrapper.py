from bs4 import BeautifulSoup
import requests
import os
import codecs
if os.path.exists("output.txt"):
  os.remove("Output.txt")
else:
    pass

file = codecs.open("Output.txt", "a", "utf-8")
letter = input("Input the first letter of your name: ")

# Geting page content 
page = requests.get(f"https://en.wikipedia.org/wiki/{letter}")

# Get page html source

soup = BeautifulSoup(page.content,"html.parser")

# Get name of first three(3) index

links= soup.find_all("li", class_="toclevel-1")[:3]

# Format extracted names to proper form

index_names = []
for item in links:
    href_val = item.find_all("a")[0]["href"]
    index_names.append(href_val[1:].replace("_", " "))

# Get content where the text to be displayed is present

parser_output=soup.find("div", class_="mw-parser-output")

# Traverse threw page until content does not end for the index's

index_element=parser_output.find_all("h2", string=index_names)
for ele in index_element:
    element = ele
    heading = element.find(text=True)

    # Print the heading of index(content) and saving in file

    print(heading)
    
    file.write("\n")
    file.write(heading)
    file.write("\n")


    # Print the content of index

    while(element.find_next_sibling(not "h2").name != "h2"):

        # Excluding table as it contains images

        if(element.find_next_sibling(not "h2").name != "table"):

            # Extracting texts from content and removing tags

            con = ''.join([ para.text for para in (element.find_next_sibling())])

            # Printing the text and saving in file

            print(con)
            
            file.write(con)
            file.write("\n")

        # Traversing to next content of index

        element = element.find_next_sibling(not "h2")

# Saving the output file

file.close()
