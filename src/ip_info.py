import requests


def get_ip_info(ip):
    url = f"http://ipinfo.io/{ip}/json"

    resp = requests.get(
                        url=url
    )

    print(resp.url)
    print(resp.json())


if __name__ == '__main__':
    ips = ['18.203.91.227', '35.197.77.7']

    for ip in ips:
        get_ip_info(ip)