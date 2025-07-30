import dns.message
import dns.query
import dns.name
import dns.edns
import dns.resolver
import sys

def check_ecs_support(domain):
    try:
        resolver = dns.resolver.Resolver()
        resolver.timeout = 3
        resolver.lifetime = 5

        # Use one of the public resolvers to make a test (Google DNS)
        nameserver = "8.8.8.8"

        query = dns.message.make_query(domain, dns.rdatatype.A)

        # Add EDNS0 option for ECS
        subnet_option = dns.edns.ECSOption(address="192.0.2.0", srclen=24)
        query.use_edns(options=[subnet_option])

        response = dns.query.udp(query, nameserver, timeout=5)

        ecs_supported = any(
            isinstance(opt, dns.edns.ECSOption)
            for opt in response.options
        )

        if ecs_supported:
            print(f"[+] {domain} supports EDNS Client Subnet (ECS).")
        else:
            print(f"[-] {domain} does NOT support EDNS Client Subnet (ECS).")

    except Exception as e:
        print(f"[!] Error testing {domain}: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ecs_detector.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    check_ecs_support(domain)
