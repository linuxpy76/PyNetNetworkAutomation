# Lesson 2

## Exercise 3

### Create a list of five IP addresses. Print the initial list of addresses.

* Use the .append() method to add an IP address onto the end of the list

* Use the .extend() method to add two more IP addresses to the end of the list.

* Use list concatenation to add two more IP addresses to the end of the list.

* Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

* Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

* Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.

## Exercise 4

### Using a context manager, open the file named "show_arp.txt". Read the contents of this file in (using the f.readlines() method) and save the file contents to a variable named 'show_arp'.

* Print out the Python data type of 'show_arp' variable.
* Print out the length of the 'show_arp' variable.
* Print out the header line from the 'show_arp' variable.
* Print out both the first and the last line of the tabular data from the 'show_arp' variable.
* Split the header line into fields using the .split() method. Save this into a variable named fields. Print out this 'fields' variable.
* Print out the Python data type of this 'fields' variable.
* Print out the current number of entries in the 'fields' variable.
* Print out the first field and the last field.

If you print out the fields variable you will observe that some fields are unneeded or incorrect (due to the splitting on whitespace).

For example, there are fields containing 'Age' and '(min)', but that is only one column in the tabular output. Similarly, 'Hardware' and 'Addr' were split into two fields, but there is only one corresponding column in the table output.

Consequently, you should delete the field containing '(min)' from the list. Similarly, you should combine the 'Hardware' and 'Addr' entries into a single field named 'Hardware_Addr'. At the end of your modifications, you should only see the following six fields in the 'fields' variable.
['Protocol', 'Address', 'Age', 'Hardware_Addr', 'Type', 'Interface']
Finally, print out the fields variable after you have made the above corrections.