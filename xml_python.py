import xml.etree.ElementTree as ET


xml_data = """
<user>
     <id>423</id>
    <first_name>Johnn</first_name>
    <last_name>Doe</last_name>
    <email>johndoe@example.com</email>
    <age>30</age>
    <address>
        <street>Main street 1</street>
        <city>New York</city>
        <zip>2001</zip>
    </address>
</user>
"""

root = ET.fromstring(xml_data)
print("User ID:", root.find("id").text) 
print("User email:", root.find("email").text)
print("User age:", root.find("age").text)