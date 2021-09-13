


function getword(tab){
    console.log("Hello");
    chrome.tabs.create({
        url: "https://www.google.com"
    });
}



const contextMenuItem = (() => ({
    test:
    {
        title:"hell000000o",
        contexts: ["selection"],
        onclick: getword
    }
}))();

chrome.contextMenus.create(contextMenuItem.test);