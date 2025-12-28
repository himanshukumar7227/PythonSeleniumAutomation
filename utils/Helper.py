import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def highlight(element, driver, duration=0.3):
    """
    Highlights (blinks) a Selenium WebDriver element by applying a temporary border.
    :param element: The WebElement to highlight.
    :param driver: The WebDriver instance.
    :param duration: The time (in seconds) to keep the element highlighted.
    """
    original_style = element.get_attribute("style")

    # Use JavaScript to apply a visible border and background
    driver.execute_script(
        "arguments[0].setAttribute('style', arguments[1]);",
        element,
        "border: 4px solid blue; border-style: dashed;"
    )

    if duration > 0:
        time.sleep(duration)
        # Revert the style back to the original
        driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            original_style
        )
def textAssertion(elementActual,elementExpected, driver):
    try:
        assert elementActual==elementExpected, "Opps! didn't found."
    except Exception as e:
        print(e)

def clickFunction(element,Driver):
    highlight(element,Driver,0.9)
    element.click()

def selectOptions(elemnt):
    dropdown = Select(elemnt)
    texts = [opt.text.strip() for opt in dropdown.options]
    for text in texts:
        print(text)
        dropdown.select_by_visible_text(text)

def prompt(driver):
    value = driver.execute_script("""
    return new Promise(resolve => {

        // ================== POPUP CONTAINER ==================
        let popup = document.createElement("div");
        popup.style = `
            position:fixed;
            top:120px;
            left:120px;
            width:280px;
            background:white;
            border-radius:10px;
            box-shadow:0 10px 30px rgba(0,0,0,0.4);
            z-index:9999;
            font-family:Arial;
        `;

        popup.innerHTML = `
            <div id="header" style="
                background:#667eea;
                color:white;
                padding:10px;
                cursor:move;
                border-radius:10px 10px 0 0;">
                🔹 Enter Test Input
            </div>
            <div style="padding:15px;">
                <input id="popupInput"
                       placeholder="Type here"
                       style="width:100%;padding:8px;
                              border-radius:6px;border:1px solid #ccc;">
                <button id="submitBtn"
                        style="margin-top:10px;width:100%;
                               padding:8px;background:#667eea;
                               color:white;border:none;
                               border-radius:6px;cursor:pointer;">
                    Submit
                </button>
            </div>
        `;

        document.body.appendChild(popup);

        // ================== INPUT CONTROL ==================
        const input = document.getElementById("popupInput");
        const submitBtn = document.getElementById("submitBtn");

        input.focus();                         // ✅ UPDATED: auto focus (no click needed)

        input.addEventListener("keydown", e => {  // ✅ UPDATED: ENTER key submits
            if (e.key === "Enter") {
                submitBtn.click();
            }
        });

        submitBtn.onclick = () => {             // existing logic kept
            let val = input.value;
            popup.remove();
            resolve(val);
        };

        // ================== DRAG LOGIC ==================
        let isDown = false, offsetX = 0, offsetY = 0;
        const header = document.getElementById("header");

        header.onmousedown = e => {
            isDown = true;
            offsetX = popup.offsetLeft - e.clientX;
            offsetY = popup.offsetTop - e.clientY;
        };

        document.onmouseup = () => isDown = false;

        document.onmousemove = e => {
            if (!isDown) return;
            popup.style.left = (e.clientX + offsetX) + "px";
            popup.style.top  = (e.clientY + offsetY) + "px";
        };

    });
    """)

    print("User entered:", value)

    return value
