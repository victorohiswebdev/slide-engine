import os
import subprocess
import time
from playwright.sync_api import sync_playwright

HTML_FILE = "slide-deck-fyp.html"
PDF_FILE = "slide-deck-fyp.pdf"

def generate_fyp_pdf():
    print("Starting local server...")
    server = subprocess.Popen(["python", "-m", "http.server", "8080"])
    time.sleep(2)

    try:
        print("Launching browser engine...")
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome")
            page = browser.new_page()

            print(f"Loading {HTML_FILE}...")
            page.goto(
                f"http://localhost:8080/{HTML_FILE}",
                timeout=90000,
                wait_until="domcontentloaded"
            )

            print("Waiting 10 seconds for fonts and visuals to render...")
            page.wait_for_timeout(10000)

            print("Capturing PDF...")
            page.pdf(
                path=PDF_FILE,
                print_background=True,
                width="1920px",
                height="1080px",
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}
            )

            browser.close()
            print(f"Done: {PDF_FILE}")

    finally:
        server.terminate()
        print("Server closed.")

if __name__ == "__main__":
    generate_fyp_pdf()
