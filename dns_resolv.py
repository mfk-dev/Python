import dns.resolver

# DNS Lookup Function
def dns_lookup():
    domain = input("Enter the domain to lookup: ")

    if not domain:
        return

    record_types = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT']

    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"\n{record} Records:")

            for rdata in answers:
                print(f" > {rdata.to_text()}")
        except dns.resolver.NoAnswer:
            continue
        except dns.resolver.NXDOMAIN:
            print(f"\nError: The domain '{domain}' does not exist :)")
            break
        except Exception as e:
            continue
        
        input("\nPress Enter to continue...")

dns_lookup()
