import os 
import requests
from bs4 import BeautifulSoup

class Website:
    
    url: str
    title: str 
    text: str

    def __init__(self, url):
        try:
            
            self.url = url
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            self.title = soup.title.string if soup.title else "No title found"
    
            if soup.body:
                for irrelevant in soup.body(["script", "style", "img", "input"]):
                    irrelevant.decompose()
                self.text = soup.body.get_text(separator="\n", strip=True)
            else:
                self.text = ""
    
            links = [link.get('href') for link in soup.find_all('a')]
            self.links = [link for link in links if link]
                   
        except requests.exceptions.RequestException as e:
            self.title = f"Erro ao acessar URL: {e}"
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def get_title_text(self):
        return f"Webpage Title:\n {self.title}\n Webpage Contents:\n{self.text}\n\n"
        
    def get_links(self):
        return f"Webpage links: {self.links}" 
