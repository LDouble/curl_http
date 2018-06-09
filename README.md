# A wrapper for PyCURL

Curl_http allows you to use the PyCURL more convenient and easier. Many common operations are wrapped as functions,such as how to keep cookie without function and how to use proxy.

## Feature Support
- Sessions with Cookie Persistence
- Automatic Content Decoding
- HTTP(S) Proxy Support
- Connection Timeouts
- Header Manager
- ...
## Installation

Use pip:

    pip install curl_http
    
## Supported python versions

 - Python 2
 - Python 3

## Usage
```Python
from curl_http import HTTP

http = HTTP()
http.set_header("Host", "it592.com")  # set the request header
http.set_timeout(10)  # set the timeout = 5 seconds
http.set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36")
# set the useragent
http.set_proxy("114.212.12.4","31228")  # set the proxy
http.set_cookie("name", "DoubleL")  # set custom cookie
http.set_foreign_ip("0.0.0.0")
http.request("www.baidu.com", referer="")  # Get method,referer is optional
http.request("www.baidu.com", {"name":123}, referer="")  # Post method, # Get method,referer is optional
http.get_header(key="")  # get the response header,key is optional
http.get_code()  # get the response code
http.get_cookie(key="")  # get the cookie,key is optional

```
