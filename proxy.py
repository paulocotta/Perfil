from selenium import webdriver

PROXY_HOST = "proxy_host"
PROXY_PORT = "proxy_port"
PROXY_USER = "proxy_username"
PROXY_PASS = "proxy_password"

# Configurações do proxy com as credenciais
PROXY = f"{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}"
webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",
}

# Inicialização do driver do Chrome com as configurações do proxy
driver = webdriver.Chrome()



from selenium import webdriver

PROXY_HOST = "proxy_host"
PROXY_PORT = "proxy_port"
PROXY_USER = "proxy_username"
PROXY_PASS = "proxy_password"

# Configurações do proxy com as credenciais
proxy = {
    "proxy": {
        "httpProxy": f"http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}",
        "ftpProxy": f"ftp://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}",
        "sslProxy": f"https://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}",
        "noProxy": None,
        "proxyType": "MANUAL",
        "class": "org.openqa.selenium.Proxy",
        "autodetect": False,
    }
}

# Inicialização do driver do Chrome com as configurações do proxy
options = webdriver.ChromeOptions()
options.set_capability("proxy", proxy)
driver = webdriver.Chrome(options=options)


from selenium import webdriver

PROXY_HOST = "proxy_host"
PROXY_PORT = "proxy_port"
PROXY_USER = "proxy_username"
PROXY_PASS = "proxy_password"

# Configurações do proxy com as credenciais
options = webdriver.ChromeOptions()
options.add_argument(f"--proxy-server=http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}")

# Inicialização do driver do Chrome com as configurações do proxy
driver = webdriver.Chrome(options=options)
