# 0x16. API advanced

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/314/WIxXad8.png">
</p>

The purpose of this project is to learn the following concepts:
- How to read API documentation to find the endpoints you’re looking for
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using ```python3``` (version 3.4.3)
- All your files should end with a new line
- Your code should use the ```PEP 8``` style
- All your files must be executable
- The length of your files will be tested using ```wc```
- All your modules should have a documentation (```python3 -c 'print(__import__("my_module").__doc__)'```)
- You must use the Requests module for sending HTTP requests to the Reddit API

---
File | Task
---|---
0-subs.py | Function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit
1-top_ten.py | Function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit
2-recurse.py | Recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit
100-count.py | Recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords

## Author
Francesca Cantor