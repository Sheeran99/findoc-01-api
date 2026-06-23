import requests

def main():
    response = requests.get("https://api.github.com")
    print(f"状态码:{response.status_code}")
    print("环境一切正常！")

if __name__ == "__main__":
    main()