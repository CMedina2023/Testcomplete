def Test1():
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btChrome].Navigate("https://demo.seleniumeasy.com/basic-first-form-demo.html")
    Aliases.browser.BrowserWindow.Maximize()
    #Clicks the 'textnode' control.
    Aliases.browser.pageSeleniumEasyDemoSimpleFormTo.textnodeTreemenu.textnodeAllExamples.textnodeTable.textnode.Click()
    #Clicks the 'linkTablePagination' link.
    Aliases.browser.pageSeleniumEasyDemoSimpleFormTo.textnodeTreemenu.textnodeAllExamples.textnodeTable.linkTablePagination.Click()
    #Waits until the browser loads the page and is ready to accept user input.
    Aliases.browser.pageTablePaginationDemo.Wait()
    #Clicks the 'link2' link.
    Aliases.browser.pageTablePaginationDemo.textnodeMypager.link2.Click()
