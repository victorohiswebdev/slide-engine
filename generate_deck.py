import os
import subprocess
import time
from playwright.sync_api import sync_playwright

def generate_slide_pdf():
    print("🌐 Starting local server to compile Tailwind CSS...")
    # Spin up a lightweight local server on port 8080
    server = subprocess.Popen(["python", "-m", "http.server", "8080"])
    
    # Give the server 2 seconds to boot up
    time.sleep(2)

    try:
        print("🚀 Firing up local browser engine...")
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome") 
            page = browser.new_page()
            
            print("📄 Loading page and bypassing strict network limits...")
            
            # 1. Tell Playwright to stop waiting for the strict "load" event. 
            # "domcontentloaded" means it just waits for the HTML/CSS to exist.
            page.goto(
                "http://localhost:8080/slide-deck.html", 
                timeout=90000, 
                wait_until="domcontentloaded"
            )
            
            # 2. Force a raw 10-second wait to allow Unsplash images and Tailwind to visually paint
            print("⏳ Giving images 10 seconds to visually render...")
            page.wait_for_timeout(10000) 
            
            print("📸 Capturing presentation slides...")
            page.pdf(
                path="slide-deck.pdf",
                print_background=True,
                width="1920px",
                height="1080px",
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}
            )
            
            browser.close()
            print("✅ Success! Your slide deck is ready: slide-deck.pdf")
            
    finally:
        # Guarantee the server shuts down when the PDF is done
        server.terminate()
        print("🛑 Local server closed.")

if __name__ == "__main__":
    generate_slide_pdf()