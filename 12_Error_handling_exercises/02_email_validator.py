class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def is_domain_invalid(domain, valid_domains):
    result = True
    for valid_domain in valid_domains:
        if domain.endswith(valid_domain):
            result = False
            break
    return result


valid_domains = {'.com', '.bg', '.net', '.org'}

while True:
    email_address = input()
    if email_address == 'End':
        break

    if '@' not in email_address:
        raise MustContainAtSymbolError('Email must contain @ !')

    username, domain = email_address.split('@')

    if len(username) <= 4:
        raise NameTooShortError('Email must be at least 4 characters!')

    if is_domain_invalid(domain, valid_domains):
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join(valid_domains)}!')

    print('Email address is valid.')
