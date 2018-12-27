function center_element(element, horizontal=true, vertical=true)
{
    /* only move absolutely positioned elements */
    if (get_css(element, "position") !== "absolute")
        throw "Element not absolutely positioned.";

    let elem_height = dimension_to_num(get_css(element, "height"));
    let elem_width = dimension_to_num(get_css(element, "width"));

    /* get the relatively positioned parent so we can get its dimensions */
    let relative_parent = get_relative_parent(element);
    if (relative_parent === null)
        throw "Absolutely positioned element has no relative parent.";

    let parent_height = dimension_to_num(get_css(relative_parent, "height"));
    let parent_width = dimension_to_num(get_css(relative_parent, "width"));

    /* set new styles */
    let new_location;
    if (horizontal)
    {
        new_location  = parent_width / 2;
        new_location -= elem_width   / 2;
        element.style.left = new_location + "px";
    }
    if (vertical)
    {
        new_location  = parent_height / 2;
        new_location -= elem_height   / 2;
        element.style.top = new_location + "px";
    }
}

function service_center_requests(parent_element)
{
    let to_center;

    /* both directions */
    to_center = parent_element.querySelectorAll(".center-me");
    for (let i = 0; i <  to_center.length; i++)
        center_element(to_center[i], true, true);

    /* horizontal only */
    to_center = parent_element.querySelectorAll(".horiz-center-me");
    for (let i = 0; i <  to_center.length; i++)
        center_element(to_center[i], true, false);

    /* vertical only */
    to_center = parent_element.querySelectorAll(".vert-center-me");
    for (let i = 0; i <  to_center.length; i++)
        center_element(to_center[i], false, true);
}
