# Project overview

> Local library is a web application to manage your ebooks and track your reading roadmap

## Technical Information

1. Language: Python 3.7.3
2. Framework: Flask
3. DB: PostgreSQL

## Specification

1. Book Category

> Type of subject. For instance : IT, Business, Marketing

2. Book

> Title, Author, Status( New, Reading, Archived )
> Deleted --> Physical Deletion

3. Security

> Bearer Token
> REST APIs

## Roadmap

### Sprint 1 : Initial Phase

**Todo**

- Install Flask
- Setup Routes
- Deploy on Dev server ( Heroku )

## Development

1. Getting start

```bash
# Upgrade lastest version of setuptools
python3 -m pip install --user --upgrade setuptools wheel

. .venv/bin/activate
pip3 install flask
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
```


## References

- https://packaging.python.org/tutorials/packaging-projects/