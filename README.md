# soaper

#### Installation
```python
pip install soaper
```

#### Example

###### soap_request(url, data)

```python
from soaper import soap_request

url = 'www.example.org'
data = '''<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:m="http://www.example.org/stock/Reddy">
  <soap:Header>
  </soap:Header>
  <soap:Body>
    <m:GetStockPrice>
      <m:StockName>GOOG</m:StockName>
    </m:GetStockPrice>
  </soap:Body>
</soap:Envelope>'''

print(soap_request(url, data))
```
