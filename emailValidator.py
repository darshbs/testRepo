import re

def fun(s):
    """Returns True if s is a valid email, else False."""
    return bool(re.match(r'^[\w\.-]+@[a-zA-Z0-9]+\.[a-z]{1,3}$', s))

def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':

    emails = ["user@example.com",
"invalid-email",
"hello.world@domain.co"]

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)