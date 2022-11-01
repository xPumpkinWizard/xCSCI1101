window.addEventListener("load", function ()
{
    // Get click element referances
    let clickCounterElement = document.getElementById("click-counter");
    let clickButtonElement = document.getElementById("click-button");

    // counter value
    let counter = 0;

    // click button function
    let clickButtonFunction = function ()
    {
        // Increment counter 
        counter++;

        // Update counter value 
        clickCounterElement.innerHTML = counter;
    };

    // Atach button function
    clickButtonElement.addEventListener("click", clickButtonFunction)
});