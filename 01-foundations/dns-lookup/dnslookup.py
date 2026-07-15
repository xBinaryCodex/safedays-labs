import dns.resolver
import argparse

RECORD_TYPES = ["A", "AAAA", "MX", "TXT", "NS"]

def lookup(domain, record_type):

    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [rdata.to_text() for rdata in answers]
    except dns.resolver.NoAnswer:
        return []
    except dns.resolver.NXDOMAIN:
        return None
    except dns.exception.DNSException:
        return []

def profile(domain):
    print(f"\nDNS profile for {domain}")
    print("=" * 40)

    for record_type in RECORD_TYPES:
        results = lookup(domain, record_type)

        if results is None:
            print(f"  '{domain}' does not exist (NXDOMAIN).")
            return
        if results:
            print(f"\n[{record_type}]")
            for record in results:
                print(f"  {record}")
        else:
            print(f"\n[{record_type}]  (none)")

def check_email_security(domain):
    print(f"\nEmail security for {domain}")
    print("=" * 40)

    txt_records = lookup(domain, "TXT")
    spf = None
    if txt_records:
        for record in txt_records:
            if "v=spf1" in record:
                spf = record
    
    dmarc_records = lookup("_dmarc." + domain, "TXT")
    dmarc = None
    if dmarc_records:
        dmarc = dmarc_records[0]

    print("  SPF  :", "PRESENT" if spf else "MISSING")
    print("  DMARC:", "PRESENT" if dmarc else "MISSING")

    if not spf  or dmarc:
        print("\n [!] Missing SPF or DMARC means this domain is easier to spoof in phishing.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DNS lookup and email-security recon tool.")
    parser.add_argument("domain", help="Domain to lookup. e.g. github.com")
    parser.add_argument("--email", action="store_true", help="Also run the SPF/DMARC email-security check")
    args = parser.parse_args()

    profile(args.domain)
    if args.email:
        check_email_security(args.domain)