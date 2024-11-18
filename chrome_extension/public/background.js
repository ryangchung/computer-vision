const API_URL = "http://127.0.0.1:8000/check-productivity";
const REDIRECT_URL = chrome.runtime.getURL("blocked.html");

chrome.webNavigation.onCompleted.addListener(async (details) => {
  try {
    if (details.frameId !== 0) {
      return;
    }

    const { url } = details;

    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ url: url }),
    });

    if (response.ok) {
      const result = await response.json();

      if (result && (result.productive === 0 || result.productive === false) && result.url) {
        chrome.tabs.update(details.tabId, { url: REDIRECT_URL });
      }
    }
  } catch (error) {
    console.error("Error checking productivity:", error);
  }
});