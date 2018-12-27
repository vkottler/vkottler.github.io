function move_element(element)
{
    /* only move absolutely positioned elements */
    if (get_css(element, "position") !== "absolute")
        throw "Element not absolutely positioned.";

    let dx = element.getAttribute("dx");
    let dy = element.getAttribute("dy");

    /* ensure element has the necessary properties */
    if (dx === null || dy === null)
        throw "Element needs 'dx' and 'dy' to be moved.";

    dx = Number(dx);
    dy = Number(dy);

    /* ensure property values are Number type */
    if (isNaN(dx) || isNaN(dy))
        throw "'dx' and 'dy' must be Number type.";

    /* move the element */
    element.style.left = dx + "px";
    element.style.top = dy + "px";
}

function service_move_requests(parent_element)
{
    let to_move = parent_element.querySelectorAll(".move-me");
    for (let i = 0; i <  to_move.length; i++)
        move_element(to_move[i]);
}
