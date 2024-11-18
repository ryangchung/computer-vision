chrome.webRequest.onBeforeRequest.addListener(
  function(details) {
    const shouldBlock = true;

    if (shouldBlock) {
      return { redirectUrl: chrome.runtime.getURL("blocked.html") };
    } else {
      return { cancel: false };
    }
  },
  { urls: ["<all_urls>"] },
  ["blocking"]
);
